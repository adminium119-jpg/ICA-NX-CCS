import unittest

from predict import read, softmax
from score import ARMS, first, selected


class DecisionInterfaceTests(unittest.TestCase):
    def test_strict_id_and_probability_contract(self):
        for split, expected in (("cal", 160), ("test", 384), ("count", 128)):
            rows, scores = read(split + "_requests"), read(split + "_predictions")
            self.assertEqual(set(scores), {x["id"] for x in rows})
            self.assertEqual(len(rows), expected)
            for row in rows:
                options = {o["id"] for o in row["options"]}
                for arm in ARMS:
                    dist = softmax(scores[row["id"]][arm])
                    self.assertEqual(set(dist), options)
                    self.assertAlmostEqual(sum(dist.values()), 1)

    def test_count_control_and_order_symmetry(self):
        rows, gold = read("test_requests"), read("test_gold")
        options = {r["id"]: {x["id"] for x in r["options"]} for r in rows}
        short, short_gold = read("count_requests"), read("count_gold")
        self.assertTrue(all({x["id"] for x in r["options"]} == {"NONE", short_gold[r["id"]]["answer"]}
                            for r in short))
        self.assertTrue(all({"NONE", g["answer"]} <= options[k] for k,g in gold.items()))
        result = read("results")
        self.assertEqual(result["arms"]["linear"]["option_swap_same_choice"], 128)
        self.assertEqual(result["single_candidate_count_control"]["linear"]["correct_single_candidate"], 0)

    def test_cannot_emit_when_no_cutoff_passes(self):
        self.assertEqual(first({"1": 0.5, "2": 0.5}), "NONE")
        self.assertEqual(selected({"1": .99, "NONE": .01}, 1.1), "HOLD")
        self.assertTrue(all(r["calibration_emissions"] == 0 for r in read("calibration").values()))


if __name__ == "__main__":
    unittest.main()
