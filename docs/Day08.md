# Day 08 – Generating Embeddings for Semantic Retrieval

## Objective

The objective of Day 8 was to introduce text embeddings and prepare the AI SOC Log Triage Assistant for semantic search.

Instead of relying only on keyword matching or rule-based document selection, the project now converts cybersecurity knowledge into numerical vector representations (embeddings). These vectors capture the semantic meaning of documents and form the foundation for Retrieval-Augmented Generation (RAG) using vector databases.

---

## Understanding Embeddings

Large Language Models (LLMs) generate human-readable text but are not designed for efficient similarity search.

Embedding models convert text into fixed-length numerical vectors that represent the semantic meaning of the content.

Documents discussing similar topics produce vectors that are located close to each other in vector space, allowing applications to retrieve relevant information based on meaning rather than exact keyword matches.

---

## Local Embedding Model

A dedicated embedding model was added using Ollama.

Model used:

- `nomic-embed-text`

Unlike the language model used for alert analysis, this model is responsible only for converting text into vector embeddings.

Current AI models in the project:

- **Qwen 2.5** → Generates AI SOC analysis
- **nomic-embed-text** → Generates semantic embeddings

---

## Generating Embeddings

A new Python script, `generate_embeddings.py`, was created.

The script performs the following tasks:

- Reads cybersecurity knowledge documents
- Sends each document to the embedding model
- Generates a 768-dimensional embedding vector
- Displays basic embedding information for verification

Each knowledge base document successfully produced an embedding vector.

---

## Persistent Embedding Storage

Instead of discarding embeddings after generation, the project now stores them inside:

```text
vector_store/embeddings.json
```

Each stored record contains:

- Document path
- Generated embedding vector

Persisting embeddings eliminates the need to regenerate vectors every time the application runs and prepares the project for efficient retrieval.

---

## Error Handling Improvements

Additional validation was implemented while generating embeddings.

The application now verifies that an embedding was successfully returned before accessing it, preventing runtime errors caused by empty or invalid documents.

This improves the robustness of the embedding generation process.

---

## Current Embedding Pipeline

The application now follows this workflow:

```text
Cybersecurity Knowledge Base
            │
            ▼
Embedding Model
(nomic-embed-text)
            │
            ▼
768-Dimensional Embeddings
            │
            ▼
embeddings.json
```

This stored vector data will be indexed by FAISS during the next development phase.

---

## Why Embeddings Matter

Traditional keyword matching depends on exact word matches.

Embeddings enable semantic retrieval by comparing the meaning of documents rather than individual words.

This allows the AI assistant to retrieve relevant cybersecurity knowledge even when different terminology is used.

---

## Skills Learned

- Embeddings and semantic representations
- Difference between LLMs and embedding models
- Local embedding generation using Ollama
- Persisting embeddings for future retrieval
- Basic validation and error handling during embedding generation
- Preparing data for vector databases

---

## Conclusion

Day 8 introduced semantic embeddings into the AI SOC Log Triage Assistant.

The project can now convert cybersecurity knowledge into reusable vector representations and store them locally for future retrieval.

This establishes the final prerequisite for integrating FAISS, where semantic similarity search will replace the current rule-based retrieval mechanism.