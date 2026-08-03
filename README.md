# 🛡️ AI SOC Log Triage Assistant

> An AI-powered Security Operations Center (SOC) assistant that combines **Wazuh SIEM**, **Retrieval-Augmented Generation (RAG)**, **FAISS Vector Search**, and **Local Large Language Models (LLMs)** to analyze security alerts and generate structured investigation reports.

---

## 📖 Overview

The AI SOC Log Triage Assistant is a cybersecurity project designed to assist SOC analysts in investigating Wazuh security alerts using Artificial Intelligence.

Instead of relying solely on prompt engineering, the project implements a **Retrieval-Augmented Generation (RAG)** pipeline. Relevant cybersecurity knowledge is retrieved from a local knowledge base using **semantic vector search (FAISS)** before being provided to a locally hosted Large Language Model (Qwen via Ollama).

All processing occurs locally, ensuring that sensitive security data never leaves the analyst's machine.

---

# 🚀 Current Features

## ✅ AI-Powered Alert Analysis

- Analyze real Wazuh security alerts
- Generate structured SOC investigation reports
- Produce concise security summaries
- Suggest possible threats
- Recommend MITRE ATT&CK techniques (when supported)
- Provide investigation recommendations

---

## ✅ Retrieval-Augmented Generation (RAG)

- Local cybersecurity knowledge base
- Embedding generation using `nomic-embed-text`
- FAISS vector database
- Semantic similarity search
- Automatic knowledge retrieval
- Structured retrieval context for the LLM

---

## ✅ Local AI

- Ollama integration
- Local Qwen LLM
- Offline inference
- Privacy-preserving AI workflow

---

## ✅ Security Data Processing

- JSON Lines (JSONL) support
- Multi-alert processing
- Robust Wazuh alert parsing
- Source IP extraction
- AI-generated Markdown investigation reports

---

## ✅ Modular Architecture

The project follows a modular design to improve maintainability and scalability.

```
analyze_alert.py
        │
        ├── retriever.py
        ├── prompt_builder.py
        └── report_generator.py
```

---

# 🏗️ Current Architecture

```text
                Wazuh SIEM
                     │
                     ▼
            Real Security Alerts
                     │
                     ▼
            Python Alert Parser
                     │
                     ▼
           Extract Alert Details
                     │
                     ▼
      Generate Alert Embedding
      (nomic-embed-text)
                     │
                     ▼
          FAISS Vector Database
                     │
                     ▼
 Retrieve Most Relevant Knowledge
                     │
                     ▼
        Prompt Construction
                     │
                     ▼
      Local LLM (Qwen + Ollama)
                     │
                     ▼
      AI Security Investigation
                     │
                     ▼
      Markdown Investigation Report
```

---

# 📂 Project Structure

```text
AI-SOC-LOG-TRIAGE-ASSISTANT/
│
├── app/
│   ├── __init__.py
│   ├── retriever.py
│   ├── prompt_builder.py
│   └── report_generator.py
│
├── docs/
│   ├── Day01.md
│   ├── ...
│   └── Day11.md
│
├── knowledge_base/
│   ├── ssh_authentication.md
│   ├── mitre_attack.md
│   └── soc_investigation.md
│
├── reports/
│   └── ai_soc_report.md
│
├── sample_logs/
│
├── screenshots/
│
├── scripts/
│   ├── analyze_alert.py
│   ├── build_faiss_index.py
│   ├── generate_embeddings.py
│   ├── search_faiss.py
│   └── test_retriever.py
│
├── vector_store/
│   ├── embeddings.json
│   └── faiss_index.bin
│
├── config.py
├── requirements.txt
└── README.md
```

---

# 🔍 Retrieval-Augmented Generation Workflow

```text
Wazuh Alert
      │
      ▼
Extract Alert Description
      │
      ▼
Generate Embedding
      │
      ▼
FAISS Semantic Search
      │
      ▼
Retrieve Relevant Knowledge
      │
      ▼
Build AI Prompt
      │
      ▼
Local LLM (Qwen)
      │
      ▼
AI SOC Investigation Report
```

---

# 🛠️ Technologies Used

### Security

- Wazuh SIEM

### Artificial Intelligence

- Ollama
- Qwen 2.5
- nomic-embed-text

### RAG

- FAISS
- Vector Embeddings
- Semantic Search

### Programming

- Python
- JSON
- JSONL

### Development

- Git
- GitHub

---

# 📸 Project Development

This repository documents the complete engineering journey.

Development progress includes:

- ✅ Environment setup
- ✅ Local LLM integration
- ✅ Wazuh alert parsing
- ✅ AI report generation
- ✅ Knowledge base creation
- ✅ Embedding generation
- ✅ FAISS vector database
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Modular architecture
- ✅ Retrieval transparency
- ✅ Similarity score visualization
- ✅ Independent retriever testing

Every implementation step is documented inside the `docs/` directory.

---

# 📈 Current Status

**Project Phase:** Active Development

### Completed

- AI alert analysis
- Knowledge base
- Semantic search
- Vector database
- Retrieval-Augmented Generation
- Modular backend architecture

### Currently Improving

- Retrieval quality
- Context engineering
- AI reasoning accuracy

### Planned

- Advanced RAG optimization
- Web dashboard
- Interactive alert upload
- Report export
- Docker deployment
- Multi-source knowledge base
- Advanced prompt optimization

---

# 🎯 Learning Outcomes

This project demonstrates hands-on experience with:

- Security Operations Center (SOC) workflows
- Wazuh SIEM
- Python automation
- Artificial Intelligence
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Local LLM deployment
- Semantic search
- FAISS vector databases
- Software architecture
- Modular Python development
- Technical documentation

---

# 🚀 Future Improvements

- Web-based SOC dashboard
- Support for additional Wazuh rule categories
- Larger cybersecurity knowledge base
- Hybrid retrieval strategies
- Advanced RAG pipelines
- Conversation memory
- Report export (PDF/HTML)
- Docker Compose deployment

---

# 👨‍💻 Development Philosophy

Rather than presenting only the final application, this repository documents the complete engineering process.

Each development phase includes:

- Objectives
- Implementation details
- Challenges encountered
- Solutions applied
- Concepts learned
- Screenshots
- Daily documentation

This approach demonstrates not only the final result but also the reasoning and problem-solving process behind the project.

---

# 📜 License

This project is developed for educational and portfolio purposes.