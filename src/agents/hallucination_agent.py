from difflib import SequenceMatcher

def detect_hallucination(ai_response, reference_answer):

    if not reference_answer.strip():
        return {
            "risk": "Cannot Verify",
            "reason": "Reference answer unavailable.",
            "unsupported_claims": []
        }

    similarity = SequenceMatcher(
        None,
        ai_response.lower(),
        reference_answer.lower()
    ).ratio()

    if similarity >= 0.90:
        return {
            "risk": "Low",
            "reason": "No unsupported claims detected.",
            "unsupported_claims": []
        }

    elif similarity >= 0.60:
        return {
            "risk": "Medium",
            "reason": "Some statements require verification.",
            "unsupported_claims": [
                "Possible unsupported statement detected."
            ]
        }

    else:
        return {
            "risk": "High",
            "reason": "Multiple unsupported statements detected.",
            "unsupported_claims": [
                ai_response
            ]
        }


if __name__ == "__main__":

    ai_response = "Artificial Intelligence is the simulation of human intelligence by machines."

    reference = "Artificial Intelligence is the simulation of human intelligence by machines."

    result = detect_hallucination(ai_response, reference)

    print(result)