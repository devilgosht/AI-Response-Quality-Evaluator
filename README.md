# 🤖 AI Response Quality Evaluator

## 📌 Project Overview

AI Response Quality Evaluator is a Python-based application that evaluates AI-generated responses using multiple quality dimensions. It helps determine whether an AI response is relevant, accurate, complete, and free from hallucinations.

This project was developed as part of the Infosys Springboard Internship.

---

## 🚀 Features

- ✅ Relevance Judge Agent
- ✅ Accuracy Judge Agent
- ✅ Completeness Judge Agent
- ✅ Hallucination Detection Agent
- ✅ Overall Verdict Generation
- ✅ Validation Module
- ✅ Streamlit User Interface
- ✅ Knowledge Base using JSON
- ✅ RAG Pipeline Foundation
- ✅ Vector Store using FAISS

---

## 🛠 Tech Stack

- Python
- Streamlit
- FAISS
- Sentence Transformers
- NumPy
- Git
- GitHub

---

## 📂 Project Structure

```
AI-Response-Quality-Evaluator
│
├── datasets/
│   └── knowledge_base.json
│
├── docs/
│   ├── Milestone1_Report.md
│   ├── Milestone2_Report.md
│   ├── Research.md
│   ├── System_Architecture.md
│   └── Tech_Stack.md
│
├── src/
│   ├── agents/
│   ├── app/
│   ├── rag/
│   └── validation.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Modules

### Evaluation Input Module
Accepts:
- Question
- AI Response
- Optional Reference Answer

### Relevance Judge Agent
Evaluates whether the AI response answers the question.

### Accuracy Judge Agent
Compares the AI response with the reference answer and generates:
- Accuracy Score
- Reason
- Supporting Evidence

### Completeness Judge Agent
Measures how complete the response is compared to the reference answer.

### Hallucination Detection Agent
Detects unsupported or hallucinated information in the response.

### Verdict Agent
Generates an overall quality score and verdict.

---

## 📊 Sample Output

```
Accuracy : 100%

Relevance : 75%

Completeness : 100%

Hallucination : Low

Overall Score : 91.67%

Verdict : ⭐⭐⭐⭐⭐ Excellent Response
```

---

## ▶️ Run the Project

Install dependencies

```
pip install -r requirements.txt
```

Run the Streamlit application

```
python -m streamlit run src/app/app.py
```

Run validation

```
python src/validation.py
```

---

## 👨‍💻 Developed By

Lakshmi Mandal

Infosys Springboard Internship Project
