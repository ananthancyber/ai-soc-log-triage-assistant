import streamlit as st
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from scripts.analyze_alert import main
import config

st.set_page_config(
    page_title="AI SOC Log Triage Assistant",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI SOC Log Triage Assistant")

st.caption("AI-Powered Wazuh Security Alert Analysis using RAG + Ollama")

st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📂 Upload Alert")

    st.info("Upload a Wazuh JSONL alert file for analysis.")

    uploaded_file = st.file_uploader(
    "Choose a JSONL file",
    type=["jsonl"]
)

if uploaded_file is not None:

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

        with st.spinner("Analyzing alerts..."):
            main()

        st.success("Analysis completed successfully!")
with col2:
    st.subheader("📊 Analysis Results")

    st.write("Analysis results will appear here after processing the uploaded alert file.")

st.divider()

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