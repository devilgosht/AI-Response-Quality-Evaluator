def generate_verdict(accuracy, relevance, completeness, hallucination):
    """
    Generate overall score and verdict.
    """

    overall_score = round((accuracy + relevance + completeness) / 3, 2)

    if hallucination == "High":
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