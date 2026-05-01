# 🤖 Multi-Agent AI System

A production-ready multi-agent AI application where multiple AI agents collaborate to perform complex tasks such as research, planning, and professional report generation.

This project demonstrates modular AI workflow orchestration using multiple specialized agents powered by LLMs.


## 📌 Project Overview

This system takes user input and processes it through a sequence of AI agents:

1. **Research Agent**
   - Collects topic insights
   - Extracts trends, facts, and relevant information

2. **Planner Agent**
   - Organizes research into a structured outline

3. **Writer Agent**
   - Generates a final professional report


## ⚙️ Workflow Architecture

```text
User Input
   ↓
Research Agent
   ↓
Planner Agent
   ↓
Writer Agent
   ↓
Final Report

## 🚀 Features

- Multi-agent AI architecture
- Research automation
- Report planning and structuring
- Final report generation
- Streamlit interactive frontend
- FastAPI backend endpoints
- Workflow visualization
- Logging system
- Environment variable security

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Python

### AI/LLM
- Groq API
- Llama 3.3 70B Versatile

### Utilities
- Graphviz
- Python Dotenv

---

## 📂 Project Structure

```bash
multi_agent_ai_system/
│
├── app.py
├── api.py
├── agents.py
├── logger.py
├── workflow.py
├── requirements.txt
├── .env
├── logs.txt
└── README.md
```

## 🔌 API Endpoints

### Base URL
```bash
http://127.0.0.1:8000
```

### Available Endpoints

#### Home
```http
GET /
```

#### Research
```http
POST /research
```

Request Body:
```json
{
  "topic": "Artificial Intelligence"
}
```

---

#### Generate Report Outline
```http
POST /plan
```

---

#### Generate Full Report
```http
POST /generate-report
```

---

## 📖 Swagger Documentation

```bash
http://127.0.0.1:8000/docs
```

---

## ▶️ Installation & Setup

### Clone repository

```bash
git clone https://github.com/Mahimachoudhari/Multi_agent_AI_System.git
cd Multi_agent_AI_System
```


### Install dependencies

```bash
pip install -r requirements.txt
```


### Configure environment variables

Create `.env`

```env
GROQ_API_KEY=your_api_key_here
```

### Run backend

```bash
uvicorn api:app --reload
```

### Run frontend

```bash
python -m streamlit run app.py
```

## 🌐 Local URLs

### Frontend
```bash
http://localhost:8501
```

### Backend
```bash
http://127.0.0.1:8000
```

## 🎯 Use Cases

- AI report generation
- Research automation
- Workflow orchestration
- Multi-agent collaboration systems
- AI internship/demo projects

## 🔐 Security

- API keys stored securely in `.env`
- `.gitignore` configured to prevent secret leakage

---

## 👩‍💻 Author

**Mahima Choudhari**

GitHub:  
https://github.com/Mahimachoudhari


## ⭐ Future Improvements

- PDF export
- Authentication system
- Chat history
- Database integration
- Deployment on cloud

---
