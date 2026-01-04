def extract_answer(text: str) -> str:
    """
    Extracts the model's actual answer by taking content
    AFTER the last 'Answer:' marker.
    """

    if "Answer:" not in text:
        return text.strip()

    # Take everything after the LAST occurrence of "Answer:"
    answer_part = text.rsplit("Answer:", 1)[-1]

    # Remove any trailing exercises or extra prompts
    stop_tokens = ["Exercise", "Context:", "Question:"]
    for token in stop_tokens:
        if token in answer_part:
            answer_part = answer_part.split(token)[0]

    return answer_part.strip()
