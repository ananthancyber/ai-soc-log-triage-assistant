import json
import faiss
import ollama
import numpy as np
import config
SEPARATOR = "\n\n" + "=" * 60 + "\n\n"
index = faiss.read_index("vector_store/faiss_index.bin")

with open("vector_store/embeddings.json", "r", encoding="utf-8") as file:
    EMBEDDING_DATA = json.load(file)

def retrieve_knowledge(
    query,
    top_k=config.TOP_K_RESULTS
):
    response = ollama.embed(
    model=config.EMBEDDING_MODEL,
    input=query
)

    query_embedding = np.array(
        response["embeddings"][0]
    ).astype("float32")

    query_embedding = np.expand_dims(query_embedding, axis=0)

    distances, indices = index.search(query_embedding, top_k)
    retrieved_documents = [] 
    knowledge = ""

    for idx, distance in zip(indices[0], distances[0]):
        document = EMBEDDING_DATA[idx]["document"]
        retrieved_documents.append(
    {
        "document": document,
        "distance": float(distance)
    }
   ) 
        with open(document, "r", encoding="utf-8") as file:

          knowledge += f"### Source: {document}\n\n"

          knowledge += file.read()

          knowledge += SEPARATOR
    print(f"\nRetrieved {len(retrieved_documents)} documents.")
    
    return knowledge, retrieved_documents       