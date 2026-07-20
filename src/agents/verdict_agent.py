def generate_verdict(
    accuracy,
    relevance,
    completeness,
    hallucination
):

    overall_score = round(

        (
            accuracy["score"] +
            relevance["score"] +
            completeness["score"]

        ) / 3,

        2

    )

    if hallucination["risk"] == "High":

        verdict = "❌ Poor Response"

    elif overall_score >= 90:

        verdict = "⭐⭐⭐⭐⭐ Excellent Response"

    elif overall_score >= 75:

        verdict = "⭐⭐⭐⭐ Good Response"

    elif overall_score >= 60:

        verdict = "⭐⭐⭐ Average Response"

    else:

        verdict = "⭐⭐ Needs Improvement"

    return overall_score, verdict