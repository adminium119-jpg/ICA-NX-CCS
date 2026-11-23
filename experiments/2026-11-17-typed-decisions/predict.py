"""Local baselines and a constrained decision readout with no gold at inference."""
from concurrent.futures import ThreadPoolExecutor
import json
import math
import random
import re
import sys
from time import perf_counter
from urllib.request import Request, urlopen

from prepare import ROOT, dump


def read(name):
    return json.loads((ROOT / f"{name}.json").read_bytes())


def words(s):
    return re.findall(r"[\w']+", s.casefold())


def rule_scores(row):
    prefix = words(row["sentence"].split("_", 1)[0])
    scores = {}
    for option in row["options"]:
        label, text = option["id"], words(option["text"])
        if label == "NONE":
            scores[label] = -0.6
        else:
            ends = [j+len(text) for j in range(len(prefix)-len(text)+1)
                    if prefix[j:j+len(text)] == text]
            scores[label] = 1/(1+0.25*(len(prefix)-max(ends))) if ends else -1.0
    return scores


def features(row):
    a, _, b = row["sentence"].partition("_")
    left, right = words(a), words(b)
    whole = set(left + right)
    scores = rule_scores(row)
    group = {}
    for option in row["options"]:
        key, terms = option["id"], words(option["text"])
        if key == "NONE":
            group[key] = {"none": 1, "none_one_candidate": len(row["options"]) == 2,
                          **{f"none_context:{t}": 1 for t in sorted(whole)}}
        else:
            group[key] = {"candidate": 1, "one_candidate": len(row["options"]) == 2,
                          "recency": scores[key], "overlap": len(set(terms) & whole),
                          "size": len(terms),
                          f"head:{terms[-1] if terms else ''}": 1,
                          f"left:{left[-1] if left else ''}:{terms[0] if terms else ''}": 1,
                          f"right:{terms[-1] if terms else ''}:{right[0] if right else ''}": 1,
                          **{f"cross:{t}/{c}": 1 for t in sorted(set(terms))
                             for c in sorted(set(right[:5]))}}
    return group


def linear(weights, row):
    return {k: sum(weights.get(f, 0) * v for f, v in fs.items()) for k, fs in features(row).items()}


def softmax(scores, temp=1.0):
    maximum = max(scores.values())
    values = {key: math.exp((v-maximum)/temp) for key, v in scores.items()}
    total = sum(values.values())
    return {k: v/total for k, v in values.items()}


def fit():
    rows, gold = read("train_requests"), read("train_gold")
    examples = [(features(row), gold[row["id"]]["answer"]) for row in rows]
    weights = {}
    rng = random.Random(119)
    for epoch in range(5):
        rng.shuffle(examples)
        eta = 0.06/(1+0.4*epoch)
        for xs, target in examples:
            ps = softmax({key: sum(weights.get(f, 0)*v for f,v in feats.items())
                          for key, feats in xs.items()})
            for key, fs in xs.items():
                update = eta*((key == target)-ps[key])
                for f, value in fs.items():
                    weights[f] = weights.get(f, 0)*0.99995 + update*value
    dump(ROOT / "linear_model.json", weights)


INSTRUCTION = ("Choose the phrase that best fills the underscore in the sentence. "
               "Select NONE if none of the given phrases is correct. "
               "Answer with exactly one capital option letter.")


def typed(row):
    codes = dict(zip("ABC", row["options"]))
    lines = "\n".join(f"{letter}: {option['text']}" for letter, option in codes.items())
    prompt = ("<|im_start|>system\n" + INSTRUCTION + "<|im_end|>\n"
              "<|im_start|>user\n" + row["sentence"] + "\n" + lines + "<|im_end|>\n"
              "<|im_start|>assistant\n")
    grammar = "root ::= " + " | ".join(json.dumps(code) for code in codes)
    payload = {"prompt": prompt, "n_predict": 1, "temperature": 1, "top_k": 0, "top_p": 1,
               "min_p": 0, "n_probs": 24, "post_sampling_probs": True,
               "grammar": grammar, "seed": 119}
    request = Request("http://127.0.0.1:18761/completion", data=json.dumps(payload).encode(),
                      headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=45) as response:
        raw = json.load(response)["completion_probabilities"]
    probabilities = {x["token"]: x["prob"] for x in raw[0]["top_probs"] if x["token"] in codes}
    if set(probabilities) != set(codes) or not all(0 < x <= 1 for x in probabilities.values()):
        raise ValueError(f"Invalid constrained option probabilities in {row['id']}: {probabilities}")
    total = sum(probabilities.values())
    return {codes[k]["id"]: math.log(v/total) for k, v in probabilities.items()}


def predict(split):
    rows = read(f"{split}_requests")
    weights = read("linear_model")
    def execute(row):
        start = perf_counter()
        scores = typed(row)
        return row["id"], {"typed": scores, "typed_elapsed_ms": (perf_counter()-start)*1000,
                           "rules": rule_scores(row), "linear": linear(weights, row)}
    result = {}
    with ThreadPoolExecutor(max_workers=2) as workers:
        for key, output in workers.map(execute, rows):
            result[key] = output
            if len(result) % 32 == 0:
                print(f"{split}: {len(result)}/{len(rows)}", flush=True)
    assert len(result) == len(rows)
    dump(ROOT / f"{split}_predictions.json", result)


if __name__ == "__main__":
    if sys.argv[1] == "fit":
        fit()
    else:
        predict(sys.argv[1])
