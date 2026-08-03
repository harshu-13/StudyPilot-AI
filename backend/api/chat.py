from fastapi import APIRouter
from pydantic import BaseModel

from rag.embedding import create_query_embedding
from rag.vector_store import search_chunks
from rag.generator import generate_answer

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: QuestionRequest):

    # Create embedding for the user's question
    query_embedding = create_query_embedding(request.question)

    # Search the vector database
    retrieved_chunks = search_chunks(query_embedding)

    # Combine retrieved chunks into one context
    context = "\n\n".join(retrieved_chunks)

    # Generate answer using Groq
    answer = generate_answer(context, request.question)

    return {
        "question": request.question,
        "answer": answer,
        "context_used": len(retrieved_chunks)
    }