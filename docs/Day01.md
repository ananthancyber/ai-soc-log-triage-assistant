# Day 01 – Understanding the AI SOC Architecture

## Problem Statement

Modern Security Operations Centers (SOCs) generate thousands of security alerts every day. Manually reviewing every log entry is time-consuming and leads to alert fatigue.

The goal of this project is to build an AI-powered assistant that helps SOC analysts retrieve relevant Wazuh alerts, understand incidents quickly, and receive structured investigation recommendations using a local Large Language Model (LLM).

## Why Not Send All Logs to the LLM?

Sending every Wazuh log directly to a Large Language Model is inefficient because the dataset can become extremely large, leading to slower responses and unnecessary processing.

Instead, the project first retrieves only the security events relevant to the user's question. These selected log entries are then provided to the LLM, allowing it to generate accurate and context-aware incident summaries while keeping the system efficient and privacy-focused.

This approach is known as Retrieval-Augmented Generation (RAG).

## High-Level System Workflow

The AI SOC Log Triage Assistant processes a user's question through a Retrieval-Augmented Generation (RAG) pipeline.

1. The SOC analyst submits a natural language question.
2. Python receives the request.
3. The question is converted into an embedding.
4. FAISS retrieves the most relevant Wazuh log entries.
5. The retrieved logs and the user's question are sent to a local LLM through Ollama.
6. The LLM generates a structured incident summary and investigation recommendations.
7. The result is displayed to the analyst.

## Core Technologies

The project combines several technologies, each with a specific responsibility.

- **Python** – Controls the complete workflow and integrates all components.
- **Wazuh** – Provides security alerts and log data.
- **Ollama** – Runs the local Large Language Model (LLM).
- **Embedding Model** – Converts text into vector representations for semantic comparison.
- **FAISS** – Performs fast similarity searches over stored embeddings.
- **Retrieval-Augmented Generation (RAG)** – Retrieves only the most relevant log entries before sending them to the LLM.
- **Streamlit** – Provides a simple user interface for SOC analysts.

## What Are Embeddings?

Embeddings are numerical vector representations of text. Instead of comparing exact words, embeddings allow the system to compare the meaning of different pieces of text.

In this project, both Wazuh log entries and the user's question are converted into embeddings. FAISS then compares these vectors to retrieve the most semantically relevant log entries, even if the wording is different.

This enables semantic search, which is a key component of the Retrieval-Augmented Generation (RAG) pipeline.

## What is FAISS?

FAISS (Facebook AI Similarity Search) is a vector search library used to perform fast similarity searches over large collections of embeddings.

In this project, embeddings generated from Wazuh log entries are stored in a FAISS index. When a SOC analyst submits a question, the question is also converted into an embedding. FAISS compares the question embedding with the stored log embeddings and retrieves the most semantically relevant log entries.

This retrieval step makes the RAG pipeline efficient by avoiding the need to search every log entry manually.

## What is Ollama?

Ollama is a tool that allows Large Language Models (LLMs) to run locally on a computer.

In this project, Ollama is used to execute a local LLM that receives the user's question together with the relevant Wazuh log entries retrieved through the RAG pipeline. The model then generates a structured incident summary and investigation recommendations.

Running the model locally helps keep security logs private, reduces dependence on cloud services, and enables offline AI-assisted log analysis.

## Complete System Architecture

The AI SOC Log Triage Assistant follows a Retrieval-Augmented Generation (RAG) architecture.

1. The SOC analyst submits a question through the web interface.
2. Python receives the request.
3. The question is converted into an embedding.
4. Wazuh security logs are stored as embeddings inside a FAISS vector database.
5. FAISS retrieves the log entries most relevant to the user's question.
6. Python sends both the user's question and the retrieved log entries to a local LLM running through Ollama.
7. The LLM generates an incident summary and investigation recommendations.
8. The final response is displayed to the SOC analyst.