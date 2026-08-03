from fastapi import APIRouter

from rag.vector_store import get_all_chunks
from rag.generator import generate_summary

router = APIRouter()


@router.post("/summary")
async def summary():

    # Get all chunks from ChromaDB
    chunks = get_all_chunks()

    if len(chunks) == 0:
        return {
            "summary": "No PDF has been uploaded."
        }

    context = "\n\n".join(chunks)

    summary = generate_summary(context)

    return {
        "summary": summary
    }