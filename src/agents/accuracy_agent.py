from difflib import SequenceMatcher

def evaluate_accuracy(ai_response, reference_answer):
    if not reference_answer.strip():
        return {
            "score": 0,
            "reason": "No reference answer provided.",
            "evidence": "Reference answer unavailable."
        }

    similarity = SequenceMatcher(
        None,
        ai_response.lower(),
        reference_answer.lower()
    ).ratio()

    score = round(similarity * 100, 2)

    if score >= 90:
        reason = "The AI response is highly consistent with the reference answer."
    elif score >= 70:
        reason = "The AI response is mostly correct with minor differences."
    elif score >= 50:
        reason = "The AI response is partially correct."
    else:
        reason = "The AI response differs significantly from the reference."

    return {
        "score": score,
        "reason": reason,
        "evidence": reference_answer
    }