import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
from evaluation.metrics_store import get_metrics

st.set_page_config(page_title="LLM Failure Mode Analyzer", layout="wide")

st.title("🧪 LLM Failure Mode Analyzer Dashboard")

metrics = get_metrics()

# Hallucinations
st.header("🔍 Hallucinations")
st.metric(
    "Total Hallucinations",
    sum(1 for h in metrics["hallucinations"] if h["hallucinated"])
)

# Overconfidence
st.header("⚠️ Overconfidence")
st.metric(
    "Overconfidence Incidents",
    sum(1 for o in metrics["overconfidence"] if o["overconfident"])
)

# Bias
st.header("⚖️ Bias Detection")
if metrics["bias"]:
    for b in metrics["bias"]:
        st.write(
            f"Case: {b['case']} | "
            f"Score A: {b['score_a']} | "
            f"Score B: {b['score_b']} | "
            f"Delta: {b['delta']}"
        )
else:
    st.write("No bias evaluations yet.")
