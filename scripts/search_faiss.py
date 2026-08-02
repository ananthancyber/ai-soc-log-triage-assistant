import json
import faiss
import ollama
import numpy as np
index = faiss.read_index("vector_store/faiss_index.bin")
with open("vector_store/embeddings.json", "r", encoding="utf-8") as file:
    data = json.load(file)

query = "SSH brute force attack"

response = ollama.embed(
    model="nomic-embed-text",
    input=query
)

query_embedding = np.array(
    response["embeddings"][0]
).astype("float32")

query_embedding = np.expand_dims(query_embedding, axis=0)
distances, indices = index.search(query_embedding, 3)
print("=" * 60)
print("Search Query:", query)

print("\nTop Matches:\n")

for rank, (idx, distance) in enumerate(zip(indices[0], distances[0]), start=1):
    print(f"{rank}. {data[idx]['document']}")
    print(f"   Distance: {distance:.4f}")
