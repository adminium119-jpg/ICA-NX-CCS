from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
from urllib.request import urlretrieve
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
SOURCE = "https://storage.googleapis.com/ai2-mosaic/public/winogrande/winogrande_1.1.zip"


def dump(path, obj):
    path.write_bytes((json.dumps(obj, ensure_ascii=True, sort_keys=True, separators=(",", ":")) + "\n").encode())


def key(row):
    return re.sub(r"\s+", " ", row["sentence"].casefold().strip())


def sorted_unique(rows, salt, exclude=()):
    found = set(exclude)
    for row in sorted(rows, key=lambda r: hashlib.sha256((salt+r["qID"]).encode()).digest()):
        k = key(row)
        if k not in found:
            found.add(k)
            yield row


def cases(rows, swapped=False):
    requests, targets = [], {}
    for row in rows:
        original = row["qID"]
        answer = int(row["answer"])
        names = {str(index): row[f"option{index}"] for index in (1, 2)}
        variants = [("base", [1, 2], str(answer)), ("missing", [3-answer], "NONE")]
        if swapped:
            variants += [("swap", [2, 1], str(answer))]
        for label, order, correct in variants:
            record_id = hashlib.sha256(f"{original}/{label}".encode()).hexdigest()[:20]
            options = [{"id": str(i), "text": names[str(i)]} for i in order]
            options.append({"id": "NONE", "text": "Neither candidate is correct"})
            requests.append({"id": record_id, "sentence": row["sentence"], "options": options})
            targets[record_id] = {"answer": correct, "variant": label, "group": original}
    return requests, targets


def main():
    source = ROOT / "winogrande_1.1.zip"
    if not source.exists():
        urlretrieve(SOURCE, source)
    with ZipFile(source) as z:
        assert z.testzip() is None
        def read(split):
            return [json.loads(line) for line in z.read(f"winogrande_1.1/{split}.jsonl").splitlines()]
        dev = list(sorted_unique(read("dev"), "nxccs-v1-valid:"))
        train = list(sorted_unique(read("train_m"), "nxccs-v1-train:", {key(d) for d in dev}))[:1600]
    assert len(train) == 1600 and len(dev) >= 208
    ids = {}
    for name, rows, swap in (("train", train, False), ("cal", dev[:80], False),
                             ("test", dev[80:208], True)):
        prompts, labels = cases(rows, swapped=swap)
        dump(ROOT / f"{name}_requests.json", prompts)
        dump(ROOT / f"{name}_gold.json", labels)
        ids[name] = [r["qID"] for r in rows]
    assert sum(map(len, ids.values())) == len(set().union(*map(set, ids.values())))
    dump(ROOT / "split.json", {"source": SOURCE, "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                               "ids": ids})


if __name__ == "__main__":
    main()
