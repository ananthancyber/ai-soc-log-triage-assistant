import json
import faiss
import ollama
import numpy as np
index = faiss.read_index("vector_store/faiss_index.bin")

with open("vector_store/embeddings.json", "r", encoding="utf-8") as file:
    EMBEDDING_DATA = json.load(file)

def retrieve_knowledge(query):
    response = ollama.embed(
    model="nomic-embed-text",
    input=query
)

    query_embedding = np.array(
        response["embeddings"][0]
    ).astype("float32")

    query_embedding = np.expand_dims(query_embedding, axis=0)

    distances, indices = index.search(query_embedding, 3)

    knowledge = ""

    for idx in indices[0]:
        document = EMBEDDING_DATA[idx]["document"]

        with open(document, "r", encoding="utf-8") as file:
            knowledge += file.read()
            knowledge += "\n\n"

    return knowledge       