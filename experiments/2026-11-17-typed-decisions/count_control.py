"""Counterbalance the removal probe's option count without updating models."""
from prepare import ROOT, dump
from predict import read


def main():
    gold = read("test_gold")
    tasks, expected = [], {}
    for row in read("test_requests"):
        truth = gold[row["id"]]
        if truth["variant"] != "base":
            continue
        options = [x for x in row["options"] if x["id"] in (truth["answer"], "NONE")]
        assert len(options) == 2
        tasks.append(dict(row, options=options))
        expected[row["id"]] = truth
    dump(ROOT / "count_requests.json", tasks)
    dump(ROOT / "count_gold.json", expected)


if __name__ == "__main__":
    main()
