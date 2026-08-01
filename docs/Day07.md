# Day 07 – Building the Foundation for Retrieval-Augmented Generation (RAG)

## Objective

The goal of Day 7 was to begin transforming the AI SOC Log Triage Assistant from a standalone Large Language Model (LLM) application into a Retrieval-Augmented Generation (RAG) system.

Instead of relying only on information contained in Wazuh alerts, the application now retrieves additional cybersecurity knowledge from a local knowledge base before sending prompts to the AI model.

This provides the foundation for more accurate, explainable, and context-aware security analysis.

---

## Understanding Retrieval-Augmented Generation (RAG)

Traditional LLM applications generate responses using only the information supplied in the prompt and the model's internal knowledge.

Retrieval-Augmented Generation improves this process by retrieving relevant external knowledge before generating a response.

The workflow implemented during Day 7 is:

```text
Wazuh Alert
      │
      ▼
Knowledge Retrieval
      │
      ▼
Prompt + Security Knowledge
      │
      ▼
Local LLM (Ollama)
      │
      ▼
AI Security Analysis
```

Although the retrieval mechanism currently uses rule-based document selection, the overall architecture now follows the core concept of a RAG pipeline.

---

## Knowledge Base

A dedicated `knowledge_base/` directory was introduced to store trusted cybersecurity reference material.

The following knowledge documents were created:

- `ssh_authentication.md`
- `mitre_attack.md`
- `soc_investigation.md`

Each file contains curated security knowledge that can be reused across multiple investigations.

Separating cybersecurity knowledge from application logic improves maintainability and prepares the project for future vector-based retrieval.

---

## Loading External Knowledge

A reusable `load_knowledge_base()` function was implemented.

Instead of hardcoding security knowledge inside prompts, Python now loads the required Markdown documents from the local knowledge base.

This introduces the retrieval stage of the RAG pipeline while keeping the implementation simple and easy to understand.

---

## Rule-Based Knowledge Retrieval

Instead of loading every document for every alert, the application now performs simple rule-based retrieval.

For SSH-related alerts, the system loads:

- SSH Authentication knowledge
- MITRE ATT&CK reference
- SOC Investigation guidance

This approach reduces unnecessary prompt content and more closely resembles the behavior of production RAG systems.

---

## Prompt Augmentation

The prompt generation function was updated to include retrieved cybersecurity knowledge together with alert information.

The AI now receives:

- Security alert information
- Retrieved cybersecurity knowledge
- Investigation instructions

Providing additional context enables the model to generate more informed and consistent security analysis.

---

## Current RAG Architecture

The application workflow now follows this structure:

```text
Real Wazuh Alert
        │
        ▼
Python Alert Parser
        │
        ▼
Rule-Based Knowledge Retrieval
        │
        ▼
Local Cybersecurity Knowledge Base
        │
        ▼
Prompt Construction
        │
        ▼
Local LLM (Ollama)
        │
        ▼
AI SOC Investigation Report
```

---

## Skills Learned

- Retrieval-Augmented Generation (RAG) fundamentals
- Building a local cybersecurity knowledge base
- Rule-based document retrieval
- Prompt augmentation
- Separating knowledge from application logic
- Designing AI workflows for cybersecurity

---

## Conclusion

Day 7 introduced the first implementation of Retrieval-Augmented Generation within the AI SOC Log Triage Assistant.

Although the retrieval mechanism currently relies on simple rule-based document selection, the project architecture now separates cybersecurity knowledge from the application itself.

This establishes the foundation for future enhancements such as vector embeddings, semantic search, FAISS integration, and fully context-aware AI-assisted security investigations.