from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all API routers
from api.upload import router as upload_router
from api.chat import router as chat_router
from api.summary import router as summary_router
from api.quiz import router as quiz_router

app = FastAPI(
    title="StudyPilot AI",
    description="AI-powered Study Assistant using Retrieval-Augmented Generation (RAG)",
    version="1.0.0"
)

# Enable CORS (Allows React frontend to communicate with FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Change this to your frontend URL when deploying
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(summary_router)
app.include_router(quiz_router)


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Welcome to StudyPilot AI 🚀",
        "version": "1.0.0",
        "features": [
            "📄 Upload PDF",
            "💬 AI Chat",
            "📝 AI Summary",
            "🎯 AI Quiz Generator"
        ],
        "endpoints": {
            "upload": "/upload",
            "chat": "/chat",
            "summary": "/summary",
            "quiz": "/quiz"
        }
    }