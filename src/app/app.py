import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.accuracy_agent import evaluate_accuracy
from agents.relevance_agent import evaluate_relevance
from agents.completeness_agent import evaluate_completeness
from agents.hallucination_agent import detect_hallucination
from agents.verdict_agent import generate_verdict

st.set_page_config(page_title="AI Response Quality Evaluator", page_icon="🤖")

st.title("🤖 AI Response Quality Evaluator")

question = st.text_area("Question")

ai_response = st.text_area("AI Response")

reference = st.text_area("Reference Answer (Optional)")

st.divider()

if st.button("🚀 Evaluate Response"):

    accuracy = evaluate_accuracy(ai_response, reference)
    relevance = evaluate_relevance(question, ai_response)
    completeness = evaluate_completeness(ai_response, reference)
    hallucination = detect_hallucination(ai_response, reference)

    overall_score, verdict = generate_verdict(
        accuracy,
        relevance,
        completeness,
        hallucination
    )

    st.success("Evaluation Completed!")

    st.subheader("📊 Accuracy")
    st.metric("Score", f'{accuracy["score"]}%')
    st.write("Reason:", accuracy["reason"])
    st.write("Evidence:", accuracy["evidence"])

    st.divider()

    st.subheader("📊 Relevance")
    st.metric("Score", f'{relevance["score"]}%')
    st.write("Reason:", relevance["reason"])

    st.divider()

    st.subheader("📊 Completeness")
    st.metric("Score", f"{completeness}%")

    st.divider()

    st.subheader("📊 Hallucination")
    st.metric("Risk", hallucination["risk"])
    st.write("Reason:", hallucination["reason"])

    if hallucination["unsupported_claims"]:
        st.write("Unsupported Claims:")
        for claim in hallucination["unsupported_claims"]:
            st.write("-", claim)

    st.divider()

    st.subheader("🏁 Final Verdict")
    st.metric("Overall Score", f"{overall_score}%")
    st.success(verdict)