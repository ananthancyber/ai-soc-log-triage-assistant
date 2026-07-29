# Day 02 – AI Environment Setup

## Objectives

- Install Ollama on the Windows host.
- Download and configure a local Large Language Model (LLM).
- Connect Python to Ollama.
- Verify AI responses using Python.
- Analyze a structured Wazuh alert using the local LLM.

---

## Why Ollama?

Ollama allows Large Language Models (LLMs) to run locally on a computer. Instead of sending sensitive Wazuh security logs to a cloud AI service, the project uses Ollama to execute a local LLM.

This approach improves privacy, enables offline analysis after the model is downloaded, and allows the AI SOC Log Triage Assistant to generate incident summaries using local resources.

---

## AI Model Selection

For this project, the **Qwen 2.5:3B** model was selected because it provides a good balance between reasoning capability, performance, and memory usage for a laptop with 16 GB RAM.

The model runs locally through Ollama and serves as the AI engine for generating SOC-style incident summaries.

---

## Python and Ollama Integration

The `ollama` Python package was installed inside the project's virtual environment.

A test script (`scripts/test_ollama.py`) was created to verify communication between Python and the local LLM.

The successful execution confirmed that Python can send prompts to Ollama and receive AI-generated responses.

---

## From Hardcoded Prompts to Real Security Logs

The initial Python script used a hardcoded prompt to verify communication between Python, Ollama, and the local LLM.

In the completed AI SOC Log Triage Assistant, hardcoded prompts will be replaced with real Wazuh security alerts. Python reads the alert data, sends it to the local LLM, and receives structured incident summaries that assist SOC analysts during investigations.

This transition marks the move from an AI demonstration to a practical cybersecurity application.

---

## First Wazuh Alert Analysis

A sample Wazuh alert stored in `sample_logs/wazuh_alert.json` was analyzed using the local Qwen model.

A second Python script (`scripts/analyze_alert.py`) was developed to:

- Read the JSON alert.
- Construct an AI prompt dynamically.
- Send the alert to Ollama.
- Generate a SOC-style incident summary.

The AI successfully produced:

- Incident Summary
- Severity Assessment
- Possible MITRE ATT&CK Technique
- Investigation Recommendations

---

## Key Learning Outcomes

- Installed and configured Ollama.
- Downloaded and verified the Qwen 2.5:3B model.
- Connected Python to a local LLM.
- Executed AI prompts directly from Python.
- Read structured Wazuh JSON alerts.
- Generated AI-assisted SOC incident summaries from security log data.

---

## Files Created

- `scripts/test_ollama.py`
- `scripts/analyze_alert.py`
- `sample_logs/wazuh_alert.json`

---

## Next Steps

The next phase of the project will focus on processing multiple Wazuh alerts, preparing the data for embeddings, and building the Retrieval-Augmented Generation (RAG) pipeline.