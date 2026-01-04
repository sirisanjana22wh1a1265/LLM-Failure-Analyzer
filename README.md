LLM Failure Mode Analyzer

A production-style evaluation system to detect and analyze failure modes in Large Language Models (LLMs), including hallucinations, overconfidence, and bias — with persistent metrics and an interactive dashboard.

1. Overview

Large Language Models often fail in subtle but dangerous ways:

Generating answers not supported by context (hallucinations)

Expressing high confidence in incorrect answers

Producing inconsistent judgments across demographic attributes

This project addresses these issues by building an LLM evaluation and monitoring pipeline inspired by real-world Responsible AI and production ML systems.

2. Key Features

a. Hallucination Detection

Embedding-based similarity check between context and answer

Flags answers not grounded in the provided context

b. LLM-as-a-Judge Verification

Secondary LLM pass to verify if the answer is fully supported

Robust verdict extraction to handle prompt-echo and over-generation

c. Overconfidence Detection

Detects strong certainty language (e.g., “definitely”, “100% sure”)

Flags cases where confidence contradicts correctness

d. Bias Detection (Paired Prompts)

Evaluates identical profiles with different demographic signals

Quantifies bias using score deltas

Transparent, measurable, and reproducible

e. Interactive Dashboard

Built using Streamlit

Visualizes hallucinations, overconfidence incidents, and bias metrics

Metrics are persisted across runs using lightweight JSON storage

3. Tech Stack

Python

Hugging Face Transformers (Phi-2 local LLM)

Sentence Embeddings

Streamlit

JSON-based persistent metrics

Rule-based + LLM-based evaluation

4. How to Run

a. Setup environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

b. Run evaluations
python evaluation/run_evaluation.py
python evaluation/run_bias_evaluation.py


This generates and updates:

evaluation/metrics.json

c. Launch dashboard
streamlit run dashboard/app.py