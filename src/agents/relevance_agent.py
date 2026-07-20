import string

def evaluate_relevance(question, ai_response):

    translator = str.maketrans('', '', string.punctuation)

    question = question.lower().translate(translator)
    ai_response = ai_response.lower().translate(translator)

    question_words = set(question.split())
    response_words = set(ai_response.split())

    common = question_words.intersection(response_words)

    if len(question_words) == 0:
        return {
            "score": 0,
            "reason": "Question is empty."
        }

    score = round(
        (len(common) / len(question_words)) * 100,
        2
    )

    if score >= 80:
        reason = "The response covers most important concepts."

    elif score >= 50:
        reason = "The response partially answers the question."

    else:
        reason = "The response is weakly related to the question."

    return {
        "score": score,
        "reason": reason
    }