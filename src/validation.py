from agents.accuracy_agent import evaluate_accuracy
from agents.relevance_agent import evaluate_relevance
from agents.completeness_agent import evaluate_completeness
from agents.hallucination_agent import detect_hallucination
from agents.verdict_agent import generate_verdict

samples = [

    {
        "question":"What is Artificial Intelligence?",

        "response":"Artificial Intelligence is the simulation of human intelligence by machines.",

        "reference":"Artificial Intelligence is the simulation of human intelligence by machines."
    },

    {
        "question":"What is Machine Learning?",

        "response":"Machine Learning is a subset of Artificial Intelligence.",

        "reference":"Machine Learning is a subset of Artificial Intelligence that enables systems to learn from data."
    },

    {
        "question":"How many states are there in India?",

        "response":"India has 45 states.",

        "reference":"India has 28 states and 8 Union Territories."
    }

]

print("="*70)

print("AI RESPONSE QUALITY EVALUATOR VALIDATION")

print("="*70)

for i,sample in enumerate(samples,start=1):

    print()

    print(f"Test Case {i}")

    print("-"*60)

    accuracy=evaluate_accuracy(

        sample["response"],

        sample["reference"]

    )

    relevance=evaluate_relevance(

        sample["question"],

        sample["response"]

    )

    completeness=evaluate_completeness(

        sample["response"],

        sample["reference"]

    )

    hallucination=detect_hallucination(

        sample["response"],

        sample["reference"]

    )

    overall,verdict=generate_verdict(

        accuracy,

        relevance,

        completeness,

        hallucination

    )

    print("Accuracy :",accuracy)

    print()

    print("Relevance :",relevance)

    print()

    print("Completeness :",completeness)

    print()

    print("Hallucination :",hallucination)

    print()

    print("Overall Score :",overall)

    print("Verdict :",verdict)

    print("="*70)