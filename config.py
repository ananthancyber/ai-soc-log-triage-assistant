"""
Application configuration.
"""

MODEL_NAME = "qwen2.5:3b"

INPUT_FILE = "sample_logs/ssh_failed_alerts.json"

REPORT_FILE = "reports/ai_soc_report.md"

# RAG Configuration

TOP_K_RESULTS = 3
EMBEDDING_MODEL = "nomic-embed-text"