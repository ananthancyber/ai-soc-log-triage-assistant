# Day 14 – Streamlit Dashboard & Backend Integration

## 📅 Date
03 August 2026

---

# 🎯 Objective

Transform the AI SOC Log Triage Assistant from a command-line application into an interactive web application using Streamlit.

---

# ✅ Tasks Completed

## 1. Installed and Configured Streamlit

- Installed the Streamlit framework.
- Created the `ui/` directory.
- Built the initial Streamlit application.
- Configured the page title, icon, and layout.

---

## 2. Designed the Dashboard

Created a professional dashboard consisting of:

- Project title
- Project description
- Upload section
- Analysis results section
- Project features section

Used Streamlit columns to create a clean two-panel layout.

---

## 3. Implemented File Upload

Added support for uploading Wazuh alert files.

Features:

- JSONL file upload
- Upload validation
- Save uploaded file to:

```
sample_logs/uploaded_alerts.jsonl
```

---

## 4. Connected the Frontend to the Backend

Instead of directly importing the analysis script, the Streamlit application executes:

```
scripts/analyze_alert.py
```

using Python's `subprocess` module.

This approach:

- avoids circular imports
- keeps the CLI application unchanged
- allows the web UI to reuse the existing backend

---

## 5. Displayed AI Analysis Report

After the backend completes:

- Reads

```
reports/ai_soc_report.md
```

- Displays the generated Markdown report directly inside the Streamlit dashboard.

This provides immediate feedback to the user without opening the report manually.

---

## 6. Added Report Download

Implemented a download button allowing users to save the generated report directly from the web interface.

Supported format:

- Markdown (.md)

---

# 📸 Screenshots

- day14-01-streamlit-dashboard.png
- day14-02-dashboard-layout.png
- day14-03-file-upload.png
- day14-04-upload-save-file.png
- day14-05-backend-connected.png
- day14-06-download-report-button.png

---

# 🧠 Concepts Learned

## Streamlit

- Page configuration
- Layouts
- Columns
- Buttons
- File uploader
- Markdown rendering
- Download button
- Status messages

---

## Python

- subprocess module
- Reading generated reports
- File handling
- Upload processing

---

## Application Design

- Connecting frontend and backend
- Reusing CLI functionality
- Web-based AI workflows
- Interactive report presentation

---

# 📂 Files Created / Updated

## New

```
ui/dashboard.py
```

---

## Updated

```
scripts/analyze_alert.py
config.py
README.md
```

---

# ✅ Outcome

Successfully transformed the AI SOC Log Triage Assistant into a web application capable of:

- Uploading Wazuh alerts
- Running AI analysis
- Performing RAG retrieval
- Displaying investigation reports
- Downloading generated reports

This marks the first complete end-to-end web interface for the project.

---

# 🚀 Next Goals

- Improve dashboard UI
- Add alert statistics
- Enhance report styling
- Improve error handling
- Final testing
- Prepare Version 1.0 release