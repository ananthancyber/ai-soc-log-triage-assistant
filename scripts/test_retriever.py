import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from app.retriever import retrieve_knowledge

queries = [
    "SSH authentication failed",
    "SSH brute force attack",
    "Failed password for invalid user"
]

for query in queries:
    print("=" * 60)
    print("Query:", query)

    _, retrieved_documents = retrieve_knowledge(query)

    print("\nRetrieved Documents:")

    for item in retrieved_documents:
        print(
            f"- {item['document']} "
            f"(Distance: {item['distance']:.4f})"
        )

    print()