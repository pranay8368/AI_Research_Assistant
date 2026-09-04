# Agentic AI Research Assistant

## Overview

Agentic AI Research Assistant is an end-to-end AI application designed to help users research and understand documents using natural language.

The application will allow users to upload documents, ask questions, search across multiple documents, and receive context-aware answers with relevant source references.

The project is being developed step-by-step, with each phase adding functionality to the final system.

---

## Current Progress

### Phase 1 — Python Fundamentals ✅

- Python fundamentals
- Project structure
- Configuration management
- File management utilities
- File reading, writing, deletion, and listing
- Logging system
- Error handling

### Phase 2 — Git & GitHub ✅

- Git repository initialization
- Git add, commit, and push
- GitHub repository setup
- `.gitignore`
- Version control

### Phase 3 — SQL & SQLite ✅

- SQL fundamentals
- SQLite fundamentals
- Python `sqlite3`
- SQLite database connection
- Database table creation
- Document metadata storage
- CRUD operations
- Document repository

Current database table:

```text
documents
├── id
├── filename
├── filepath
├── upload_time
└── size
```

---

## Planned Features

- PDF Upload and Management
- Document Metadata Management
- Multi-PDF Search
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Citation-Based Answers
- Conversation Memory
- Agentic AI Workflow
- Tool-Based AI Agents
- FastAPI Backend
- React Frontend
- Cloud Deployment

---

## Tech Stack

### Programming Language

- Python

### Version Control

- Git
- GitHub

### Database

- SQL
- SQLite
- Python `sqlite3`

### Backend

- FastAPI

### AI

- Google Gemini API

### RAG

- LangChain
- ChromaDB

### Agent Framework

- LangGraph

### Frontend

- React
- JavaScript
- HTML
- CSS

### Deployment

- Render
- Vercel

---

## Project Structure

```text
agentic-ai-research-assistant/
│
├── backend/
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── document_repository.py
│   │   └── test_database.py
│   │
│   └── utils/
│       ├── config.py
│       ├── error_handler.py
│       ├── file_manager.py
│       └── logger.py
│
├── data/
│   ├── logs/
│   └── documents.db
│
├── docs/
├── frontend/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Development Roadmap

| Phase | Topic | Status |
|---|---|---|
| 1 | Python Fundamentals | ✅ Completed |
| 2 | Git & GitHub | ✅ Completed |
| 3 | SQL & SQLite | ✅ Completed |
| 4 | APIs & JSON | 🔜 Upcoming |
| 5 | FastAPI | 🔜 Upcoming |
| 6 | LLM Fundamentals | 🔜 Upcoming |
| 7 | Embeddings & RAG | 🔜 Upcoming |
| 8 | Agentic AI & LangGraph | 🔜 Upcoming |
| 9 | Frontend | 🔜 Upcoming |
| 10 | Deployment | 🔜 Upcoming |

---

## Project Status

🚧 **Currently under development**

This project is being developed phase-by-phase, with each phase contributing reusable components to the final Agentic AI Research Assistant.

---

## Planned Final Features

- 📄 PDF Upload
- 📚 Multi-PDF Document Search
- 🔎 Semantic Search
- 🧠 Retrieval-Augmented Generation
- 🤖 Agentic AI Workflow
- 💬 Natural Language Question Answering
- 📝 Citation-Based Answers
- 🧠 Conversation Memory
- ⚡ FastAPI Backend
- 💻 React Frontend
- ☁️ Cloud Deployment