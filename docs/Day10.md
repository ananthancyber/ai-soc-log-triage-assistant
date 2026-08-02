# Day 10 – Refactoring into a Modular Architecture

## Objective

The objective of Day 10 was to improve the architecture of the AI SOC Log Triage Assistant by refactoring the project into reusable modules.

As the project grew with additional features such as Retrieval-Augmented Generation (RAG), maintaining all functionality inside a single Python file became difficult. To improve maintainability, readability, and scalability, the project was reorganized into a modular architecture where each component has a single responsibility.

---

## Why Refactor?

Initially, `analyze_alert.py` handled every stage of the workflow:

- Reading Wazuh alerts
- Retrieving cybersecurity knowledge
- Building AI prompts
- Sending prompts to the LLM
- Writing Markdown reports

Although functional, this design made the application harder to maintain as new features were introduced.

To address this, the project was reorganized into dedicated modules following software engineering best practices.

---

## Project Structure Before Refactoring

```text
scripts/
└── analyze_alert.py

Responsibilities:
- Read alerts
- Retrieve knowledge
- Build prompts
- AI analysis
- Generate reports
```

---

## Project Structure After Refactoring

```text
AI-SOC-LOG-TRIAGE-ASSISTANT/
│
├── app/
│   ├── __init__.py
│   ├── retriever.py
│   ├── prompt_builder.py
│   └── report_generator.py
│
├── scripts/
│   ├── analyze_alert.py
│   ├── generate_embeddings.py
│   ├── build_faiss_index.py
│   └── search_faiss.py
│
├── knowledge_base/
├── vector_store/
├── reports/
└── docs/
```

---

## Module Responsibilities

### retriever.py

Responsible for semantic retrieval.

Functions include:

- Loading the FAISS index
- Loading stored embeddings
- Generating query embeddings using Ollama
- Performing semantic search
- Returning the most relevant cybersecurity knowledge

---

### prompt_builder.py

Responsible for prompt engineering.

Functions include:

- Combining Wazuh alert information
- Combining retrieved cybersecurity knowledge
- Building the structured prompt sent to the LLM

---

### report_generator.py

Responsible for report generation.

Functions include:

- Formatting Markdown reports
- Writing AI analysis
- Creating structured investigation reports

---

### analyze_alert.py

Acts as the application controller.

Responsibilities:

- Read Wazuh alerts
- Extract source IP
- Retrieve relevant knowledge
- Build AI prompts
- Send prompts to Ollama
- Save investigation reports

The file now coordinates the workflow instead of implementing every feature directly.

---

## Final Processing Workflow

```text
Read Wazuh Alert
        │
        ▼
Extract Source IP
        │
        ▼
Retrieve Knowledge
        │
        ▼
Build AI Prompt
        │
        ▼
Generate AI Analysis
        │
        ▼
Write Markdown Report
```

---

## Challenges Faced

### Python Package Import Issue

After moving functionality into the `app` package, Python could not locate the package when executing:

```bash
python scripts/analyze_alert.py
```

This resulted in:

```
ModuleNotFoundError: No module named 'app'
```

### Solution

The project root directory was added to Python's module search path using:

```python
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
```

This allowed the application to successfully import modules from the `app` package while continuing development.

---

## Skills Learned

- Modular software architecture
- Python package organization
- Separation of concerns
- Single Responsibility Principle (SRP)
- Code refactoring techniques
- Organizing reusable Python modules
- Building maintainable AI applications

---

## Screenshots

### 1. Application Module Structure

`day10-01-app-module-structure.png`

### 2. Retriever Module

`day10-02-retriever-module.png`

### 3. Prompt Builder Module

`day10-03-prompt-builder-module.png`

### 4. Report Generator Module

`day10-04-report-generator-module.png`

### 5. Final Main Workflow

`day10-05-final-main-workflow.png`

---

## Conclusion

Day 10 transformed the AI SOC Log Triage Assistant from a monolithic script into a modular Python application.

Each major responsibility was separated into dedicated modules, improving readability, maintainability, and scalability. This architecture provides a solid foundation for future enhancements, including advanced Retrieval-Augmented Generation (RAG), improved semantic retrieval, and a web-based user interface.

The project is now structured more like a production-ready Python application, making future development significantly easier.