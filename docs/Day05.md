# Day 05 – Improving AI Prompt Engineering and Refactoring the Code

## Objective

The objective of Day 5 was to improve both the quality of AI-generated security analysis and the maintainability of the Python code.

The focus was on:

- Reducing AI hallucinations
- Standardizing AI responses
- Improving severity classification
- Refactoring the code into reusable functions

---

# Tasks Completed

## 1. Improved Prompt Engineering

The prompt provided to the local LLM (Qwen 2.5 via Ollama) was redesigned to encourage evidence-based analysis.

The updated prompt now instructs the model to:

- Analyze only the information provided
- Avoid making unsupported assumptions
- Return **"Insufficient evidence"** when the available data is not enough
- Keep responses concise and professional

This reduces hallucinations and makes the generated analysis more reliable.

---

## 2. Standardized AI Response Format

The AI response was constrained to always return the following sections:

- Alert Summary
- Severity
- Possible Threat
- MITRE ATT&CK
- Recommended Actions

Using a fixed template improves consistency and makes the reports easier to read and automate.

---

## 3. Added Severity Guidelines

Explicit severity definitions were included in the prompt.

Severity levels:

- Low
- Medium
- High
- Critical

Providing these guidelines helps the model classify alerts more consistently instead of assigning severity arbitrarily.

---

## 4. Refactored Source IP Extraction

The source IP extraction logic was moved into its own function.

```python
extract_source_ip(alert)
```

This function is responsible for retrieving the source IP from the alert while safely handling missing fields.

Benefits:

- Cleaner code
- Reusable logic
- Easier maintenance

---

## 5. Refactored Prompt Generation

The prompt creation logic was moved into a dedicated function.

```python
build_prompt(alert, source_ip)
```

Separating prompt construction from the main workflow improves readability and makes future prompt modifications easier.

---

## 6. Refactored AI Communication

The Ollama API call was extracted into its own function.

```python
analyze_with_ai(prompt)
```

This isolates all AI communication in one place.

Future improvements such as switching to another LLM or adding retries can now be implemented without modifying the main workflow.

---

# Challenges Faced

During refactoring, the script produced the following error:

```
NameError: name 'response' is not defined
```

Cause:

The original code accessed:

```python
response["message"]["content"]
```

After introducing the `analyze_with_ai()` function, the function returned the analysis string directly.

The remaining references to the old `response` variable were updated to use:

```python
analysis
```

After replacing the outdated references, the script executed successfully.

---

# Concepts Learned

## Prompt Engineering

Designed prompts that encourage evidence-based AI responses instead of unsupported assumptions.

---

## Hallucination Reduction

Configured the model to explicitly return **"Insufficient evidence"** whenever the provided alert lacks enough information.

---

## Standardized AI Output

Used a structured response template to produce consistent reports suitable for SOC workflows.

---

## Single Responsibility Principle (SRP)

Each function now has one clear responsibility.

Examples:

- `extract_source_ip()` → Extract source IP
- `build_prompt()` → Create the AI prompt
- `analyze_with_ai()` → Send requests to the LLM

---

## Code Refactoring

Improved maintainability by separating logic into reusable functions.

The code is now easier to understand, test, and extend.

---

# Final Project Structure

```
scripts/
└── analyze_alert.py

Functions:

extract_source_ip()
build_prompt()
analyze_with_ai()

Main Workflow

Read Alert
↓

Extract Source IP
↓

Build Prompt
↓

Send Prompt to Ollama
↓

Receive AI Analysis
↓

Generate Markdown Report
```

---

# Result

Successfully improved both the AI analysis quality and the internal code structure.

The application now:

- Produces more reliable AI-generated SOC analysis
- Uses consistent report formatting
- Reduces hallucinations
- Follows a modular Python design
- Is easier to extend for future features such as Retrieval-Augmented Generation (RAG), configurable AI models, and additional alert sources.

---

# Screenshots

- `day05-02-standardized-output.png`
- `day05-03-severity-guidelines.png`
- `day05-04-first-function.png`
- `day05-05-build-prompt-function.png`
- `day05-06-analyze-function.png`
- `day05-final-working-script.png`
