# Day 04 – Integrating AI for SOC Alert Analysis

## Objectives

- Connect the Python alert parser to a local Large Language Model (LLM).
- Send real Wazuh security alerts to the AI for analysis.
- Improve AI responses using prompt engineering.
- Generate a persistent Markdown report containing AI-generated SOC investigations.

---

## Why Integrate an LLM?

Security Operations Center (SOC) analysts manually review thousands of alerts every day. Many alerts are repetitive and require similar investigation steps.

A Large Language Model can assist analysts by:

- Explaining security alerts in plain language
- Estimating alert severity
- Identifying possible attack techniques
- Recommending investigation actions

Instead of replacing analysts, the AI acts as a triage assistant that helps prioritize and understand security events more efficiently.

---

## Tasks Completed

### 1. Connected Python to Ollama

Integrated the Ollama Python library into the project, allowing Python to communicate directly with the locally hosted Qwen 2.5 model.

This enabled the application to send prompts and receive AI-generated responses without relying on external cloud services.

---

### 2. Built the AI Prompt

Created a structured prompt that instructs the model to behave as a Tier 1 SOC Analyst.

The prompt includes:

- Rule ID
- Alert description
- Source IP
- Timestamp

The model is instructed to generate a structured security analysis instead of free-form text.

---

### 3. Generated AI-Based Alert Analysis

Each real Wazuh alert is sent individually to the local LLM.

For every alert, the AI generates:

- Alert Summary
- Severity Assessment
- Possible Threat
- MITRE ATT&CK Technique (when applicable)
- Recommended Investigation Actions

---

### 4. Automated Report Generation

Instead of displaying results only in the terminal, the project now creates a Markdown report containing all AI-generated analyses.

Generated report:

```text
reports/
└── ai_soc_report.md
```

The report provides a persistent record of the AI investigation and can be viewed directly on GitHub.

---

## Current Workflow

```text
Kali Linux
      │
      ▼
Ubuntu + Wazuh SIEM
      │
      ▼
alerts.json
      │
      ▼
Python Alert Parser
      │
      ▼
Prompt Builder
      │
      ▼
Ollama (Qwen 2.5)
      │
      ├────────────► Terminal Output
      │
      └────────────► Markdown Report
```

---

## Key Concepts Learned

- Local LLM integration using Ollama
- Prompt engineering
- AI-assisted security triage
- Python API communication
- Markdown report generation
- Automating security documentation

---

## Files Updated

```text
scripts/
└── analyze_alert.py

reports/
└── ai_soc_report.md

docs/
└── Day04.md
```

---

## Screenshots

- Ollama model running
- Ollama Python package verification
- First AI-generated alert analysis
- Structured AI response
- Generated Markdown report

---

## Outcome

By the end of Day 4, the project successfully analyzes real Wazuh security alerts using a locally hosted Large Language Model and automatically generates structured SOC investigation reports.

This milestone transforms the project from a log-processing utility into an AI-assisted SOC log triage application, providing security analysts with concise explanations, threat assessments, and investigation recommendations while keeping all analysis local.