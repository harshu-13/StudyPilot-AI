import chromadb

# Create Chroma client
client = chromadb.PersistentClient(path="../chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="study_notes"
)


def store_chunks(chunks, embeddings):
    """
    Store document chunks and embeddings.
    """

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )


def search_chunks(query_embedding, n_results=3):
    """
    Search the vector database.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]

def get_all_chunks():
    """
    Returns all stored text chunks from ChromaDB.
    """

    results = collection.get()

    if results is None:
        return []

    return results["documents"]