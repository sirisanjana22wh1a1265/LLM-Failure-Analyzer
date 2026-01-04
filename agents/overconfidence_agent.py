CONFIDENCE_TERMS = [
    "definitely",
    "certainly",
    "absolutely",
    "100%",
    "no doubt",
    "undoubtedly",
    "clearly",
    "without a doubt"
]

def detect_overconfidence(answer: str, is_correct: bool):
    """
    Flags overconfidence when strong certainty language
    is used AND the answer is incorrect.
    """

    answer_lower = answer.lower()

    confidence_hits = [
        term for term in CONFIDENCE_TERMS if term in answer_lower
    ]

    return {
        "confidence_terms": confidence_hits,
        "confidence_score": len(confidence_hits),
        "overconfident": len(confidence_hits) > 0 and not is_correct
    }
