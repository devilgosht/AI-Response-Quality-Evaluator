def evaluate_completeness(ai_response, reference_answer):

    if not reference_answer.strip():
        return {
            "score": 0,
            "reason": "Reference answer unavailable."
        }

    ai_words = len(ai_response.split())
    ref_words = len(reference_answer.split())

    if ref_words == 0:
        return {
            "score": 0,
            "reason": "Reference answer unavailable."
        }

    score = min(
        round((ai_words / ref_words) * 100, 2),
        100
    )

    if score >= 90:
        reason = "The response covers almost all information."

    elif score >= 70:
        reason = "The response covers most information."

    else:
        reason = "The response is incomplete."

    return {
        "score": score,
        "reason": reason
    }