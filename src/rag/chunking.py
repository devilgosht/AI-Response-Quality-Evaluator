def chunk_documents(data):
    chunks = []

    for item in data:
        chunk = f"Question: {item['question']}\nAnswer: {item['answer']}"
        chunks.append(chunk)

    print(f"Created {len(chunks)} chunks.")

    return chunks


if __name__ == "__main__":
    from .dataset_loader import load_knowledge_base

    kb = load_knowledge_base()
    chunks = chunk_documents(kb)

    print("\nFirst Chunk:\n")
    print(chunks[0])