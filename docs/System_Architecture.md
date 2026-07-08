# System Architecture

## Workflow

User

↓

Evaluation Input Module

↓

Reference Knowledge Base (RAG)

↓

Evaluation Agents

- Accuracy Agent
- Relevance Agent
- Completeness Agent
- Hallucination Detection Agent

↓

Verdict Agent

↓

Evaluation Report

---

## Module Description

### Evaluation Input Module

Accepts:
- Question
- AI Response
- Optional Reference Answer
- Optional Source Document

### Reference Knowledge Base

Stores trusted reference information using embeddings and vector search.

### Evaluation Agents

Each agent evaluates one quality dimension.

### Verdict Agent

Combines all scores into a final evaluation report.