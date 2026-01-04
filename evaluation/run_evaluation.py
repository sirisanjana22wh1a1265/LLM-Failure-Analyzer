import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.local_llm import LocalLLM
from agents.hallucination_agent import detect_hallucination
from agents.overconfidence_agent import detect_overconfidence
from agents.judge_agent import JudgeAgent
from evaluation.answer_utils import extract_answer
from evaluation.metrics_store import (
    log_hallucination,
    log_overconfidence
)


llm = LocalLLM()
judge = JudgeAgent()

context = "The capital of France is Paris."
question = "What is the capital of France?"

prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

raw_answer = llm.generate(prompt, max_new_tokens=50)
clean_answer = extract_answer(raw_answer)

hallucination_result = detect_hallucination(context, clean_answer)
judge_result = judge.verify(context, clean_answer)

is_correct = "paris" in clean_answer.lower()

overconfidence_result = detect_overconfidence(
    clean_answer,
    is_correct=is_correct
)
log_hallucination(hallucination_result)
log_overconfidence(overconfidence_result)


print("CLEAN ANSWER:\n", clean_answer)
print("\nEMBEDDING HALLUCINATION RESULT:\n", hallucination_result)
print("\nJUDGE RESULT:\n", judge_result)
print("\nOVERCONFIDENCE RESULT:\n", overconfidence_result)

