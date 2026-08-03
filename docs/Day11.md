# Day 11 – Improving Retrieval Transparency and Context Quality

## Objective

The objective of Day 11 was to improve the Retrieval-Augmented Generation (RAG) pipeline by making the retrieval process more transparent, improving the structure of the retrieved context, and independently testing the semantic retriever.

While the previous implementation successfully retrieved relevant cybersecurity knowledge using FAISS, it did not expose which documents were selected or how similar they were to the query. This made debugging and evaluating the retrieval process difficult.

To address this, the retriever was enhanced to provide retrieval metadata and better organize the context supplied to the Large Language Model (LLM).

---

## Tasks Completed

### Improved Retriever Output

The `retrieve_knowledge()` function was enhanced to return both:

- The combined cybersecurity knowledge
- Metadata about the retrieved documents

Instead of returning only:

```python
return knowledge
```

The function now returns:

```python
return knowledge, retrieved_documents
```

This allows the application to display which knowledge sources were retrieved during each investigation.

---

### Displayed Retrieved Knowledge Sources

The alert analysis workflow was updated to print the retrieved knowledge sources before generating the AI analysis.

Example:

```text
Retrieved Knowledge Sources:

- knowledge_base/ssh_authentication.md
- knowledge_base/mitre_attack.md
- knowledge_base/soc_investigation.md
```

This significantly improves the transparency of the RAG pipeline.

---

### Added Similarity Distance Scores

The retriever was updated to include the FAISS similarity distance for each retrieved document.

Example output:

```text
Retrieved Knowledge Sources:

- knowledge_base/ssh_authentication.md (Distance: 0.6323)
- knowledge_base/mitre_attack.md (Distance: 0.7437)
- knowledge_base/soc_investigation.md (Distance: 0.9631)
```

The similarity score provides insight into how closely each document matches the alert description.

---

### Improved Context Structure

Previously, retrieved documents were combined into one continuous block of text.

The retriever now inserts a heading before each document:

```text
### Source: knowledge_base/ssh_authentication.md
```

and separates documents using a visual divider.

This provides a cleaner and more structured context for the LLM, making the retrieved knowledge easier to interpret.

---

### Created Independent Retriever Tests

A dedicated testing script was created:

```
scripts/test_retriever.py
```

The script allows the semantic retriever to be tested independently from the AI analysis pipeline.

Multiple cybersecurity queries were evaluated, including:

- SSH authentication failed
- SSH brute force attack
- Failed password for invalid user

The retrieved documents and similarity scores were verified for each query.

---

## Project Improvements

### Before Day 11

```text
Alert
      │
      ▼
Embedding
      │
      ▼
FAISS Search
      │
      ▼
Merged Documents
      │
      ▼
LLM
```

---

### After Day 11

```text
Alert
      │
      ▼
Embedding
      │
      ▼
FAISS Search
      │
      ▼
Retrieved Documents
      │
      ▼
Similarity Scores
      │
      ▼
Structured Context
      │
      ▼
LLM
```

---

## Skills Learned

- Retrieval debugging
- FAISS similarity evaluation
- Retrieval transparency
- Semantic search validation
- Context engineering for LLMs
- Independent component testing
- Retrieval-Augmented Generation (RAG) evaluation

---

## Challenges Faced

### Improving Retrieval Visibility

Initially, the retriever returned only the combined knowledge, making it difficult to determine which documents had been selected.

**Solution**

The retriever was updated to return both:

- Combined knowledge
- Retrieved document metadata

---

### Understanding Similarity Scores

Understanding the FAISS distance values required additional experimentation.

Through testing, it was verified that:

- Smaller distance values indicate greater semantic similarity.
- Documents with lower distances are generally more relevant to the alert.

---

### Organizing Retrieved Context

The original context consisted of multiple documents concatenated together without clear boundaries.

Adding document headings and separators created a much more readable context for the AI model.

---

## Screenshots

### 1. Retrieved Knowledge Sources

`day11-01-retrieved-knowledge-sources.png`

---

### 2. FAISS Similarity Scores

`day11-02-faiss-distance-scores.png`

---

### 3. Structured Retrieval Context

`day11-03-structured-retrieval-context.png`

---

### 4. Retriever Testing

`day11-04-retriever-testing.png`

---

### 5. Retriever Cleanup

`day11-05-retriever-cleanup.png`

---

## Conclusion

Day 11 focused on improving the quality and transparency of the Retrieval-Augmented Generation (RAG) pipeline.

The retriever now exposes the retrieved knowledge sources, displays similarity scores, organizes retrieved context more effectively, and supports independent testing.

These improvements make the retrieval process easier to evaluate, debug, and explain while providing the Large Language Model with better-structured cybersecurity knowledge.

The AI SOC Log Triage Assistant now has a more robust and maintainable semantic retrieval pipeline, providing a strong foundation for future enhancements.