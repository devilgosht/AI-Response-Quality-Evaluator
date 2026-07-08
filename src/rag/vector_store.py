import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from .embeddings import generate_embeddings

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_store():
    embeddings, chunks = generate_embeddings()

    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, chunks


def search_knowledge(query):
    index, chunks = create_vector_store()

    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k=1)

    return chunks[indices[0][0]]