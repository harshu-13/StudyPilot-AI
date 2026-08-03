from fastapi import APIRouter

from rag.vector_store import get_all_chunks
from rag.generator import generate_quiz

router = APIRouter()


@router.post("/quiz")
async def quiz():

    chunks = get_all_chunks()

    if len(chunks) == 0:
        return {
            "quiz": "No PDF has been uploaded."
        }

    context = "\n\n".join(chunks)

    quiz = generate_quiz(context)

    return {
        "quiz": quiz
    }