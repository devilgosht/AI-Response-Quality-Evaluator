def evaluate_completeness(ai_response, reference_answer):
    """
    Compare the length of the AI response with the reference answer.
    """

    if not reference_answer.strip():
        return 0

    ai_words = len(ai_response.split())
    ref_words = len(reference_answer.split())

    if ref_words == 0:
        return 0

    score = min((ai_words / ref_words) * 100, 100)

    return round(score, 2)


if __name__ == "__main__":

    ai = "Artificial Intelligence is the simulation of human intelligence by machines."

    reference = "Artificial Intelligence is the simulation of human intelligence by machines."

    print("Completeness:", evaluate_completeness(ai, reference), "%")