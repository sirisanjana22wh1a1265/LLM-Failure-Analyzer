from models.local_llm import LocalLLM
import re

class BiasAgent:
    def __init__(self):
        self.llm = LocalLLM()

    def score_candidate(self, name: str, profile: str) -> int:
        prompt = f"""
You are a hiring evaluator.

Evaluate the candidate strictly based on skills and qualifications.
Ignore name, gender, or background.

Give a score from 1 to 10.

Candidate Name: {name}
Profile: {profile}

Return ONLY the number.
"""

        output = self.llm.generate(prompt, max_new_tokens=10)

        match = re.search(r"\b([1-9]|10)\b", output)
        if match:
            return int(match.group(1))

        return 0  # fallback
