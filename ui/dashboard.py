import streamlit as st
import sys
import os
import subprocess

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

import config

st.set_page_config(
    page_title="AI SOC Log Triage Assistant",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI SOC Log Triage Assistant")
st.caption("AI-Powered Wazuh Security Alert Analysis using RAG + Ollama")

st.divider()

# ==========================================
# Dashboard Metrics
# ==========================================

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric("Alerts", "JSONL")

with metric2:
    st.metric("AI Model", config.MODEL_NAME)

with metric3:
    st.metric("Embedding", config.EMBEDDING_MODEL)

with metric4:
    st.metric("Top-K", str(config.TOP_K_RESULTS))

st.divider()

# ==========================================
# Main Layout
# ==========================================

col1, col2 = st.columns([1, 2])

uploaded_file = None
analyze_button = False
result = None

# ==========================================
# Upload Section
# ==========================================

with col1:

    st.subheader("📂 Upload Alert")

    st.info("Upload a Wazuh JSONL alert file for analysis.")

    uploaded_file = st.file_uploader(
        "Choose a JSONL file",
        type=["jsonl"]
    )

    if uploaded_file is not None:

        if uploaded_file.size == 0:
            st.error("❌ The uploaded file is empty.")
            st.stop()

        save_path = os.path.join(
            "sample_logs",
            "uploaded_alerts.jsonl"
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Alert file uploaded successfully!")

        st.write("Filename:", uploaded_file.name)
        st.write("Saved to:", save_path)

        analyze_button = st.button(
            "🚀 Analyze Alerts",
            use_container_width=True
        )

        if analyze_button:

            config.INPUT_FILE = save_path

            status = st.status(
                     "Starting AI analysis...",
                      expanded=True
                        )

            status.write("📂 Uploaded alert file verified.")
            status.write("🔍 Launching backend analysis...")

            result = subprocess.run(
    [
        sys.executable,
        "scripts/analyze_alert.py"
    ],
    capture_output=True,
    text=True
)

            if result.returncode == 0:
             status.write("🤖 AI analysis completed.")
             status.write("📝 Report generated successfully.")
             status.update(
        label="✅ Analysis Complete",
        state="complete"
           )
            else:
             status.update(
             label="❌ Analysis Failed",
             state="error"
             )

# ==========================================
# Analysis Results
# ==========================================

with col2:

    st.subheader("📊 Analysis Results")

    if uploaded_file is None:

        st.write(
            "Analysis results will appear here after processing the uploaded alert file."
        )

    elif analyze_button and result is not None:

        if result.returncode == 0:

            st.toast("✅ AI analysis completed successfully!", icon="🎉")

            metric1, metric2, metric3 = st.columns(3)

            with metric1:
                st.metric(
                    "Alerts",
                    "Processed"
                )

            with metric2:
                st.metric(
                    "Report",
                    "Generated"
                )

            with metric3:
                st.metric(
                    "Knowledge Sources",
                    config.TOP_K_RESULTS
                )

            report_path = config.REPORT_FILE

            if os.path.exists(report_path):

                with open(
                    report_path,
                    "r",
                    encoding="utf-8"
                ) as report_file:

                    report_content = report_file.read()

                report_content = report_content.replace(
                    "# AI SOC Security Analysis Report",
                    ""
                )

                with st.expander(
                    "📋 View AI Security Analysis Report",
                    expanded=True
                ):

                    st.markdown(report_content)

                    st.download_button(
                        label="📥 Download Report",
                        data=report_content,
                        file_name="ai_soc_report.md",
                        mime="text/markdown",
                        use_container_width=True
                    )

            else:

                st.error(
                    "❌ Analysis completed, but the report file was not found."
                )

                st.info(
                    "Please verify that report generation completed successfully."
                )

        else:

            st.error("❌ AI analysis failed.")

            if "ollama" in result.stderr.lower():
                st.warning(
                    "⚠️ Ollama appears to be unavailable. Please start the Ollama service."
                )

            with st.expander("View Error Details"):
                st.code(result.stderr)

st.divider()

# ==========================================
# Project Features
# ==========================================

st.subheader("ℹ️ Project Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    st.markdown("""
- 🤖 Local AI (Ollama + Qwen)
- 🔍 FAISS Semantic Search
- 📚 Retrieval-Augmented Generation
""")

with feature_col2:
    st.markdown("""
- 🛡️ Wazuh SIEM Integration
- 📝 AI Investigation Reports
- 📄 Markdown Report Export
""")