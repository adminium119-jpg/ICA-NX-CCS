"""Finite latent-program comparison. Entity mentions are supplied to every arm."""
import itertools
import json
import math
from pathlib import Path
import random
from time import perf_counter

ROOT = Path(__file__).resolve().parent
PROGRAMS = [(op, permutation) for op in ("transfer", "noop")
            for permutation in itertools.permutations(range(3))]
VERBS = ("entrego", "recibio")


def execute(program, mentions, before):
    op, permutation = program
    source, target, obj = [mentions[i] for i in permutation]
    if op == "noop":
        return dict(before)
    if before.get(obj) != source:
        return None
    return {**before, obj: target}


def make_cases(prefix, count, seed, modifier=False):
    rng = random.Random(seed)
    cases = []
    for index in range(count):
        source, target, obj = (f"{prefix}s{index}", f"{prefix}d{index}", f"{prefix}o{index}")
        verb = VERBS[index % 2]
        negated = bool((index // 2) % 2)
        mentions = [source, obj, target] if verb == "entrego" else [target, obj, source]
        before = {obj: source}
        after = before.copy() if negated else {obj: target}
        permutation = (0, 2, 1) if verb == "entrego" else (2, 0, 1)
        program = ("noop" if negated else "transfer", permutation)
        # This key identifies a surface construction, without specifying its denotation.
        key = (verb, negated)
        prep = "a" if verb == "entrego" else "de"
        text = f"{mentions[0]} {'no ' if negated else ''}{verb} {'hoy ' if modifier else ''}{obj} {prep} {mentions[2]}"
        cases.append({"text": text, "mentions": mentions, "key": key, "before": before,
                      "after": after, "gold_program": PROGRAMS.index(program)})
    rng.shuffle(cases)
    return cases


def fit(observations, supervised=False):
    weights = {key: [1 / len(PROGRAMS)] * len(PROGRAMS)
               for key in {tuple(c["key"]) for c in observations}}
    likelihood = []
    for _ in range(20):
        counts = {key: [0.] * len(PROGRAMS) for key in weights}
        loss = 0.
        for row in observations:
            key = tuple(row["key"])
            compatible = ([row["gold_program"]] if supervised else [
                i for i, p in enumerate(PROGRAMS)
                if execute(p, row["mentions"], row["before"]) == row["after"]])
            total = sum(weights[key][i] for i in compatible)
            if total <= 0:
                raise ValueError("Observation outside candidate language")
            loss -= math.log(total)
            for i in compatible:
                counts[key][i] += weights[key][i] / total
        weights = {key: [x / sum(values) for x in values] for key, values in counts.items()}
        likelihood.append(loss / len(observations))
    return weights, likelihood


def evaluate(cases, weights=None):
    correct = wrong = hold = ambiguous = 0
    alternatives = []
    for row in cases:
        if weights is None:
            verb, negated = row["key"]
            program = ("noop" if negated else "transfer",
                       (0, 2, 1) if verb == "entrego" else (2, 0, 1))
            candidates = [PROGRAMS.index(program)]
        else:
            probabilities = weights.get(tuple(row["key"]))
            candidates = [] if probabilities is None else [
                i for i, probability in enumerate(probabilities) if probability > 1e-10]
        # Prediction precedes comparison with the reserved after-state.
        outputs = [execute(PROGRAMS[i], row["mentions"], row["before"]) for i in candidates]
        unique = {json.dumps(s, sort_keys=True) for s in outputs if s is not None}
        alternatives.append(len(candidates))
        ambiguous += len(candidates) > 1
        if not candidates or None in outputs or len(unique) != 1:
            hold += 1
        elif json.loads(next(iter(unique))) == row["after"]:
            correct += 1
        else:
            wrong += 1
    return {"cases": len(cases), "correct_transition": correct, "wrong": wrong,
            "hold": hold, "multiple_programs_retained": ambiguous,
            "mean_programs": sum(alternatives) / len(alternatives)}


def main():
    started = perf_counter()
    train = make_cases("train", 80, 1)
    # One physical observation can leave six noop role bindings indistinguishable.
    latent_input = [{k: v for k, v in r.items() if k != "gold_program"} for r in train]
    latent, losses = fit(latent_input)
    labeled, _ = fit(train, supervised=True)
    changed = [{**r, "gold_program": (r["gold_program"] + 1) % len(PROGRAMS)} for r in train]
    assert fit([{k: v for k, v in r.items() if k != "gold_program"} for r in changed])[0] == latent
    test = make_cases("test", 80, 2)
    modified = make_cases("modified", 80, 3, modifier=True)
    unknown = make_cases("unknown", 20, 4)
    for row in unknown:
        row["key"] = ("presto", row["key"][1])
        row["text"] = row["text"].replace("entrego", "presto").replace("recibio", "presto")
    assert set(m for c in train for m in c["mentions"]).isdisjoint(m for c in test for m in c["mentions"])
    report = {"candidate_programs": len(PROGRAMS), "train": len(train),
              "loss_first_last": [losses[0], losses[-1]], "arms": {}, "seconds": None,
              "controls": {"latent_ignores_gold": True, "train_test_entities_disjoint": True}}
    for name, model in (("rules", None), ("role_supervised", labeled), ("denotational", latent)):
        report["arms"][name] = {label: evaluate(cases, model) for label, cases in (
            ("new_entities", test), ("added_modifier", modified))}
    report["unknown_verb"] = evaluate(unknown, latent)
    assert report["arms"]["denotational"]["new_entities"]["multiple_programs_retained"] == 40
    assert report["unknown_verb"]["hold"] == 20
    report["seconds"] = perf_counter() - started
    for name, rows in (("train", train), ("test", test), ("modified", modified), ("unknown", unknown)):
        (ROOT / f"{name}.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    (ROOT / "results.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
