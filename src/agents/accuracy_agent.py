from difflib import SequenceMatcher

def evaluate_accuracy(ai_response, reference_answer):
    """
    Compare AI response with the reference answer.
    Returns an accuracy score (0-100).
    """

    if not reference_answer.strip():
        return 0

    similarity = SequenceMatcher(
        None,
        ai_response.lower(),
        reference_answer.lower()
    ).ratio()

    score = round(similarity * 100, 2)

    return score


if __name__ == "__main__":

    ai = "Artificial Intelligence is the simulation of human intelligence by machines."

    ref = "Artificial Intelligence is the simulation of human intelligence by machines."

    print("Accuracy Score:", evaluate_accuracy(ai, ref))