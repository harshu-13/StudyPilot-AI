from fastapi import APIRouter, UploadFile, File
import os
import shutil

from rag.pdf_reader import extract_text
from rag.chunk import chunk_text
from rag.embedding import create_embeddings
from rag.vector_store import store_chunks

router = APIRouter()

UPLOAD_FOLDER = "../uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Save uploaded PDF
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    text = extract_text(file_path)

    # Split text into chunks
    chunks = chunk_text(text)

    # Generate embeddings
    embeddings = create_embeddings(chunks)

    # Store chunks and embeddings in ChromaDB
    store_chunks(chunks, embeddings)

    return {
        "message": "PDF uploaded and indexed successfully!",
        "filename": file.filename,
        "characters": len(text),
        "total_chunks": len(chunks),
        "embeddings_created": len(embeddings)
    }