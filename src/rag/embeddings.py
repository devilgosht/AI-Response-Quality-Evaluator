from sentence_transformers import SentenceTransformer

from .chunking import chunk_documents
from .dataset_loader import load_knowledge_base

def generate_embeddings():
    print("Loading embedding model...")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    kb = load_knowledge_base()

    chunks = chunk_documents(kb)

    embeddings = model.encode(chunks)

    print(f"\nGenerated {len(embeddings)} embeddings.")

    return embeddings, chunks


if __name__ == "__main__":
    embeddings, chunks = generate_embeddings()

    print("\nFirst Chunk:")
    print(chunks[0])

    print("\nEmbedding Dimension:")
    print(len(embeddings[0]))