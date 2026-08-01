import json
import ollama

documents = [
    "knowledge_base/ssh_authentication.md",
    "knowledge_base/mitre_attack.md",
    "knowledge_base/soc_investigation.md"
]
embedding_store = []
for document in documents:

    with open(document, "r", encoding="utf-8") as file:
        content = file.read()

    response = ollama.embed(
        model="nomic-embed-text",
        input=content
    )
    if not response.get("embeddings"):
       print(f"Skipping {document}: No embedding generated.")
       continue

    embedding = response["embeddings"][0]
    embedding_store.append(
    {
        "document": document,
        "embedding": embedding
    }
)
with open("vector_store/embeddings.json", "w", encoding="utf-8") as file:
    json.dump(embedding_store, file, indent=4)

    print("\nEmbeddings saved successfully!")
    print("=" * 60)
    print("Document:", document)
    print("Embedding Length:", len(embedding))
    print("First 10 Values:")
    print(embedding[:10])