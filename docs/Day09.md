# Day 09 – Implementing Semantic Search with FAISS

## Objective

The objective of Day 9 was to replace the rule-based knowledge retrieval system with semantic retrieval using a FAISS vector database.

Previously, the application selected knowledge files using keyword matching (for example, checking whether the alert description contained "ssh"). While functional, this approach was difficult to scale and required manual updates whenever new knowledge documents were added.

To overcome this limitation, FAISS was integrated to perform similarity search over document embeddings, enabling Retrieval-Augmented Generation (RAG).

---

## Tasks Completed

### Installed FAISS

- Installed the `faiss-cpu` library.
- Verified successful installation.
- Confirmed compatibility with Python.

---

### Built the Vector Index

Created a new script:

```
scripts/build_faiss_index.py
```

The script:

- Loaded embeddings from `embeddings.json`
- Converted them into NumPy arrays
- Created a FAISS `IndexFlatL2`
- Stored all document embeddings
- Saved the index as:

```
vector_store/faiss_index.bin
```

---

### Tested Semantic Search

Created:

```
scripts/search_faiss.py
```

The script:

- Loaded the FAISS index
- Embedded a search query using `nomic-embed-text`
- Retrieved the three most relevant documents
- Displayed similarity distances

Example query:

```
SSH brute force attack
```

Retrieved documents:

1. ssh_authentication.md
2. mitre_attack.md
3. soc_investigation.md

---

### Integrated FAISS into the AI Pipeline

Replaced the previous keyword-based retrieval system.

Old workflow:

```
Alert
   ↓
Keyword Matching
   ↓
Load Markdown Files
   ↓
LLM
```

New workflow:

```
Alert
   ↓
Embedding Generation
   ↓
FAISS Semantic Search
   ↓
Relevant Knowledge
   ↓
LLM
```

A new function named `retrieve_knowledge()` was implemented.

The function:

- Generates an embedding from the alert description
- Searches the FAISS index
- Retrieves the three most relevant knowledge documents
- Builds contextual information for the LLM

---

## Project Structure

New files created:

```
scripts/
├── build_faiss_index.py
├── search_faiss.py
```

New generated file:

```
vector_store/
├── embeddings.json
└── faiss_index.bin
```

---

## Skills Learned

- Vector databases
- FAISS indexing
- Semantic similarity search
- Embedding-based document retrieval
- Retrieval-Augmented Generation (RAG)
- NumPy vector processing
- AI context retrieval pipelines

---

## Challenges Faced

### Missing JSON Import

Issue:

```
NameError: json is not defined
```

Solution:

Added:

```python
import json
```

---

### Empty Knowledge Files

Embedding generation initially failed because one knowledge document contained no content.

Solution:

Added meaningful SOC investigation notes before generating embeddings.

---

### Printing Similarity Distances

Improved the semantic search output by displaying similarity distances alongside retrieved documents for easier verification.

---

## Outcome

The AI SOC Log Triage Assistant now performs semantic retrieval instead of relying on hard-coded keyword matching.

This significantly improves scalability because new cybersecurity knowledge documents can be added without modifying the retrieval logic.

The project now implements the core architecture of a Retrieval-Augmented Generation (RAG) system.

---

## Conclusion

Day 9 represents one of the most significant milestones of the project.

The application evolved from a rule-based knowledge loader into an AI-assisted semantic retrieval system capable of selecting relevant cybersecurity documentation based on meaning rather than exact keyword matches.

This architecture provides a strong foundation for future enhancements such as conversational investigations, larger knowledge bases, and advanced retrieval strategies.