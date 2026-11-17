from collections import defaultdict
import hashlib
import math
from statistics import median
import sys

from predict import read, softmax
from prepare import ROOT, dump


ARMS = ("rules", "linear", "typed")


def nll(scored, truth):
    return -math.log(max(scored[truth], 1e-15))


def first(probs):
    highest = max(probs.values())
    winners = [key for key, val in probs.items() if val == highest]
    return winners[0] if len(winners) == 1 else "NONE"


def selected(probs, cutoff):
    pick = first(probs)
    return pick if pick != "NONE" and probs[pick] >= cutoff else "HOLD"


def calibrate():
    rows, gold = read("cal_predictions"), read("cal_gold")
    assert rows.keys() == gold.keys()
    tuning = {}
    for arm in ARMS:
        temp = min((.25, .5, .75, 1, 1.5, 2, 3, 4, 6, 8),
                   key=lambda t: sum(nll(softmax(row[arm], t), gold[key]["answer"])
                                   for key, row in rows.items()))
        ps = {key: softmax(row[arm], temp) for key, row in rows.items()}
        best, cutoff = 0, 1.1
        for candidate in sorted({p[first(p)] for p in ps.values() if first(p) != "NONE"}):
            emissions = [(key, selected(p, candidate)) for key, p in ps.items()
                         if selected(p, candidate) != "HOLD"]
            correct = sum(choice == gold[key]["answer"] for key, choice in emissions)
            if len(emissions) >= 8 and len(emissions) - correct <= 0.15*len(emissions) and len(emissions) > best:
                best, cutoff = len(emissions), candidate
        tuning[arm] = {"temperature": temp, "cutoff": cutoff, "calibration_emissions": best}
    dump(ROOT / "calibration.json", tuning)


def evaluate():
    model = read("calibration")
    rows, gold = read("test_predictions"), read("test_gold")
    assert rows.keys() == gold.keys()
    counts = {}
    for arm in ARMS:
        profile = model[arm]
        result = {}
        choices = defaultdict(dict)
        for variant in ("base", "missing", "swap"):
            logs = [(key, row, gold[key]["answer"]) for key, row in rows.items()
                    if gold[key]["variant"] == variant]
            scored = [(key, softmax(row[arm], profile["temperature"]), y) for key, row, y in logs]
            decisions = [(selected(p, profile["cutoff"]), y) for _, p, y in scored]
            for key, p, _ in scored:
                choices[gold[key]["group"]][variant] = first(p)
            n = len(scored)
            result[variant] = {"cases": n,
                "correct_top": sum(first(p) == y for _, p, y in scored),
                "emitted": sum(out != "HOLD" for out, _ in decisions),
                "wrong_emitted": sum(out not in {"HOLD", y} for out, y in decisions),
                "brier": sum(sum((v-(k == y))**2 for k,v in p.items()) for _, p, y in scored)/n,
                "nll": sum(nll(p, y) for _,p,y in scored)/n}
        result["option_swap_same_choice"] = sum(x["base"] == x["swap"] for x in choices.values())
        counts[arm] = result
    probes = read("count_predictions")
    labels = read("count_gold")
    assert probes.keys() == labels.keys()
    control = {arm: {"cases": len(probes), "correct_single_candidate": sum(
        first(softmax(x[arm], model[arm]["temperature"])) == labels[key]["answer"]
        for key,x in probes.items())}
        for arm in ARMS}
    report = {"calibration": model, "arms": counts, "single_candidate_count_control": control,
              "typed_http_median_ms": median(row["typed_elapsed_ms"] for row in rows.values()),
              "seals": {name: hashlib.sha256((ROOT / f"{name}.json").read_bytes()).hexdigest()
                        for name in ("cal_predictions", "test_predictions", "count_predictions",
                                     "calibration", "split")}}
    dump(ROOT / "results.json", report)
    for arm, result in counts.items():
        print(arm, result, "one candidate present", control[arm])
    print("calibration", model)
    print("typed_http_median_ms", report["typed_http_median_ms"])


if __name__ == "__main__":
    {"calibrate": calibrate, "evaluate": evaluate}[sys.argv[1]]()
