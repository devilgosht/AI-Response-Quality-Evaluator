def evaluate_relevance(question, ai_response):
    """
    Check how many keywords from the question
    appear in the AI response.
    """

    question_words = set(question.lower().split())
    response_words = set(ai_response.lower().split())

    common_words = question_words.intersection(response_words)

    if len(question_words) == 0:
        return 0

    score = (len(common_words) / len(question_words)) * 100

    return round(score, 2)


if __name__ == "__main__":

    question = "What is Artificial Intelligence?"

    ai_response = "Artificial Intelligence is the simulation of human intelligence by machines."

    print("Relevance:", evaluate_relevance(question, ai_response), "%")