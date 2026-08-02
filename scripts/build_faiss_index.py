import json
import faiss
import numpy as np

with open("vector_store/embeddings.json", "r", encoding="utf-8") as file:
    data = json.load(file)

embeddings = [item["embedding"] for item in data]
embeddings = np.array(embeddings).astype("float32")

print("Number of documents:", len(embeddings))
print("Embedding dimension:", embeddings.shape[1])

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("Vectors stored:", index.ntotal)

faiss.write_index(index, "vector_store/faiss_index.bin")

print("FAISS index saved successfully!")