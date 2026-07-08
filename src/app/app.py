import streamlit as st
import os
import sys

# Add src folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

st.set_page_config(
    page_title="AI Response Quality Evaluator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Response Quality Evaluator")
st.write(
    "Evaluate AI-generated responses using Accuracy, Relevance, Completeness and Hallucination Detection."
)

st.divider()

st.subheader("📝 Evaluation Input")

question = st.text_area(
    "Question",
    placeholder="Enter your question..."
)

ai_response = st.text_area(
    "AI Response",
    placeholder="Paste the AI response..."
)

reference = st.text_area(
    "Reference Answer (Optional)"
)

uploaded_file = st.file_uploader(
    "Upload Source Document",
    type=["pdf", "txt", "docx"]
)

st.divider()

st.subheader("📊 Evaluation")

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy", "Pending")
    st.metric("Relevance", "Pending")

with col2:
    st.metric("Completeness", "Pending")
    st.metric("Hallucination", "Pending")

st.metric("Overall Score", "Pending")

st.divider()

if st.button("🚀 Evaluate Response"):

    st.success("Evaluation Started!")

    st.write("### Submitted Data")

    st.write("**Question:**")
    st.write(question)

    st.write("**AI Response:**")
    st.write(ai_response)

    if reference:
        st.write("**Reference Answer:**")
        st.write(reference)

    if uploaded_file:
        st.write(f"Uploaded File: {uploaded_file.name}")

    st.info("Knowledge Base : Ready")
    st.info("Chunking : Ready")
    st.info("Embeddings : Ready")
    st.info("Vector Store : Ready")

    st.success("Prototype Working Successfully!")