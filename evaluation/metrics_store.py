import json
import os

METRICS_FILE = "evaluation/metrics.json"

# Initialize file if not exists
if not os.path.exists(METRICS_FILE):
    with open(METRICS_FILE, "w") as f:
        json.dump({
            "hallucinations": [],
            "overconfidence": [],
            "bias": []
        }, f)

def _read_metrics():
    with open(METRICS_FILE, "r") as f:
        return json.load(f)

def _write_metrics(data):
    with open(METRICS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_hallucination(result):
    data = _read_metrics()
    data["hallucinations"].append(result)
    _write_metrics(data)

def log_overconfidence(result):
    data = _read_metrics()
    data["overconfidence"].append(result)
    _write_metrics(data)

def log_bias(result):
    data = _read_metrics()
    data["bias"].append(result)
    _write_metrics(data)

def get_metrics():
    return _read_metrics()
