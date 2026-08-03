# 📘 StudyPilot AI

StudyPilot AI is an AI-powered study assistant that helps students interact with their study materials using Retrieval-Augmented Generation (RAG).

## ✨ Features

- 📄 Upload PDF notes
- 💬 Ask questions from uploaded notes
- 📝 Generate concise summaries
- 🧠 Automatically generate quizzes
- ⚡ Fast semantic search using ChromaDB
- 🤖 Powered by Groq LLM

---

## 🛠 Tech Stack

### Frontend
- React
- Vite
- Axios
- React Markdown

### Backend
- FastAPI
- Python
- LangChain
- ChromaDB
- Sentence Transformers
- Groq API

---

## Project Structure

```
StudyPilot-AI
│
├── backend
│   ├── api
│   ├── rag
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   └── package.json
│
└── uploads
```

---

## Installation

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Future Improvements

- User authentication
- Multiple PDF support
- Flashcards
- Voice-based Q&A
- Chat history
- Deployment on Render + Vercel

---

## Author

**Harsha Vardhini**