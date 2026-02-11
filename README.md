# 🧠 Requirement Intelligence AI System

An AI-powered requirement analysis system that converts unstructured text or PDFs into **structured software requirements, risk analysis, and actionable task plans** using **Generative AI**.

This project simulates how real-world **product, engineering, and consulting teams** analyze client requirement documents before development.

---

## 🚀 What This Project Does

The system accepts:

- 📄 Plain text  
- 📑 PDF requirement documents  

And automatically generates:

- ✅ Structured Requirements  
- ⚠️ Risk & Assumption Analysis  
- 🧩 Task Breakdown (Epics → Stories → Tasks)  

All outputs are generated using **Large Language Models (LLMs)** and served through a **FastAPI backend** with a simple UI dashboard.

---

## 🧩 Core Features

### 🔹 Requirement Extraction
- Identifies **functional requirements**
- Identifies **non-functional requirements**
- Extracts **open questions & assumptions**

### 🔹 Risk Analysis
- Detects **technical risks**
- Detects **business & operational risks**
- Flags **dependencies & unclear areas**
- Suggests **mitigation actions**

### 🔹 Task Planning
Converts requirements into:
- **Epics**
- **User Stories**
- **Engineering Tasks**
- Includes **priority levels & effort estimates**

### 🔹 Input Methods
- Text input
- PDF upload (no OCR dependency required)

### 🔹 Output Formats
- Structured **JSON responses** (API)
- **Human-readable UI output** (dashboard)

---

## 🏗️ Architecture Overview

```text
User Input (Text / PDF)
        ↓
   FastAPI Backend
        ↓
┌───────────────────────────────┐
│ Requirement Extractor (LLM)   │
│ Risk Analyzer (LLM)           │
│ Task Planner (LLM)            │
└───────────────────────────────┘
        ↓
 Structured JSON Output
 ```
---
## 🔁 End-to-End AI Workflow

This system follows a **multi-stage Generative AI pipeline** that mirrors how real-world product and engineering teams analyze requirement documents before development.

### 1️⃣ Input Ingestion
- Users submit **plain text** or upload **PDF requirement documents**
- PDFs are parsed using **PyMuPDF** (no OCR dependency required)
- All inputs are normalized into clean text for downstream processing

### 2️⃣ Requirement Understanding (LLM)
- Extracts **functional requirements**
- Extracts **non-functional requirements**
- Identifies **assumptions, ambiguities, and open questions**
- Produces a structured requirement schema for further analysis

### 3️⃣ Risk Intelligence (LLM)
- Analyzes extracted requirements to identify:
  - Technical risks
  - Business risks
  - Operational risks
- Flags unclear dependencies and missing constraints
- Suggests mitigation strategies for each identified risk

### 4️⃣ Task Decomposition & Planning (LLM)
- Converts validated requirements into:
  - Epics
  - User Stories
  - Engineering Tasks
- Assigns:
  - Priority levels
  - Effort estimates
- Generates an execution-ready task plan

### 5️⃣ Output & Delivery
- Final outputs are delivered as:
  - **Structured JSON** via REST APIs
  - **Human-readable UI output** through a web dashboard
- Enables easy integration with project management and planning tools

---

## 🌍 Why This Project Matters

In real-world software development, unclear or incomplete requirements are a major cause of project delays, scope creep, and cost overruns.

This project demonstrates how **Generative AI can augment business analysts, product managers, and engineering teams** by:
- Automating requirement understanding from unstructured documents
- Identifying risks early in the development lifecycle
- Translating vague ideas into structured, actionable task plans

The system closely resembles **enterprise-grade pre-development workflows**, making it highly relevant for industry use.

---

## 🧠 Key Design Decisions

- Uses a **multi-stage LLM pipeline** instead of a single prompt for better reliability
- Separates concern between extraction, risk analysis, and task planning
- Produces **structured JSON outputs** for downstream system integration
- Implements a **stateless FastAPI backend** for scalability
- Avoids OCR dependency to reduce complexity and improve performance

---

## ✍️ Prompt Engineering Strategy

Each LLM component uses carefully crafted prompts that:
- Enforce structured outputs using predefined schemas
- Reduce hallucinations by constraining response formats
- Preserve context between pipeline stages
- Isolate reasoning tasks to improve clarity and accuracy

This approach reflects **best practices used in production GenAI systems**.

---

## ⚠️ Limitations & Assumptions

- Output quality depends on the clarity of input requirements
- Domain-specific terminology may require prompt tuning
- LLM responses are probabilistic and may vary across runs
- Currently processes one document at a time

---

## 📌 Future Improvements

- Streaming responses for better UX
- Retrieval-Augmented Generation (RAG) using vector databases
- Multi-document comparison and conflict detection
- Authentication and role-based access control
- Cloud deployment and scalability enhancements

## 🧰 Tech Stack

- **Backend Framework:** FastAPI  
- **Template Engine:** Jinja2  
- **AI Processing:** Large Language Models (LLMs)  
- **PDF Parsing:** PyMuPDF  
- **Server:** Uvicorn  
- **Language:** Python 3.11+


The project follows a clean separation between routing, business logic, and presentation layers.

