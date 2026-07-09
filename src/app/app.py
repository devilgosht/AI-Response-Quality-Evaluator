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

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Accuracy", f"{accuracy}%")
        st.metric("Relevance", f"{relevance}%")

    with col2:
        st.metric("Completeness", f"{completeness}%")
        st.metric("Hallucination", hallucination)

    st.metric("Overall Score", f"{overall_score}%")

    st.subheader("Verdict")

    st.success(verdict)