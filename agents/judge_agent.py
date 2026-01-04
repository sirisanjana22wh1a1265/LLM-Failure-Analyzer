from models.local_llm import LocalLLM

class JudgeAgent:
    def __init__(self):
        self.llm = LocalLLM()

    def verify(self, context: str, answer: str):
        with open("prompts/judge_prompt.txt", "r") as f:
            prompt_template = f.read()

        prompt = prompt_template.format(
            context=context,
            answer=answer
        )

        raw_output = self.llm.generate(prompt, max_new_tokens=150)

        verdict = None
        for line in raw_output.splitlines():
            line_clean = line.strip().upper()
            if line_clean.startswith("VERDICT:"):
                verdict = line_clean.replace("VERDICT:", "").strip()

        # verdict now contains the LAST verdict
        return {
            "raw_verdict": raw_output.strip(),
            "supported": verdict == "SUPPORTED"
        }
