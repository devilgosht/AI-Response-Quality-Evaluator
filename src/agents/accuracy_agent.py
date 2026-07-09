from difflib import SequenceMatcher


def evaluate_accuracy(ai_response, reference_answer):
    """
    Compare AI response with the reference answer
    and return an accuracy percentage.
    """

    if not reference_answer.strip():
        return 0

    similarity = SequenceMatcher(
        None,
        ai_response.lower(),
        reference_answer.lower()
    ).ratio()

    return round(similarity * 100, 2)


if __name__ == "__main__":

    ai = "Artificial Intelligence is the simulation of human intelligence by machines."

    reference = "Artificial Intelligence is the simulation of human intelligence by machines."

    print("Accuracy:", evaluate_accuracy(ai, reference), "%")