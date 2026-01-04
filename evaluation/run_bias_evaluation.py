import json
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.bias_agent import BiasAgent
from evaluation.metrics_store import log_bias

with open("data/bias_tests.json", "r") as f:
    tests = json.load(f)

agent = BiasAgent()

for test in tests:
    a = test["group_a"]
    b = test["group_b"]

    score_a = agent.score_candidate(a["name"], a["profile"])
    score_b = agent.score_candidate(b["name"], b["profile"])

    bias_delta = abs(score_a - score_b)
    log_bias({
    "case": test["case_id"],
    "score_a": score_a,
    "score_b": score_b,
    "delta": bias_delta
})


    print("\n==============================")
    print(f"CASE: {test['case_id']}")
    print(f"{a['name']} score: {score_a}")
    print(f"{b['name']} score: {score_b}")
    print(f"Bias Delta: {bias_delta}")

    if bias_delta > 0:
        print("⚠️ Potential bias detected")
    else:
        print("✅ No bias detected")
