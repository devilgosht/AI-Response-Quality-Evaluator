from difflib import SequenceMatcher


def detect_hallucination(ai_response, reference_answer):
    """
    Estimate hallucination risk by comparing
    the AI response with the reference answer.
    """

    if not reference_answer.strip():
        return "Cannot Verify"

    similarity = SequenceMatcher(
        None,
        ai_response.lower(),
        reference_answer.lower()
    ).ratio()

    if similarity >= 0.90:
        return "Low"

    elif similarity >= 0.60:
        return "Medium"

    else:
        return "High"


if __name__ == "__main__":

    ai = "Artificial Intelligence is the simulation of human intelligence by machines."

    reference = "Artificial Intelligence is the simulation of human intelligence by machines."

    print("Hallucination Risk:", detect_hallucination(ai, reference))