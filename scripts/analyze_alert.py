import os
import sys
import json
import faiss
import numpy as np


index = faiss.read_index("vector_store/faiss_index.bin")

with open("vector_store/embeddings.json", "r", encoding="utf-8") as file:
    EMBEDDING_DATA = json.load(file)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ollama
import config

def extract_source_ip(alert):
    """
    Extract the source IP address from a Wazuh alert.
    Returns 'N/A' if no source IP is available.
    """
    return (
        alert.get("data", {}).get("srcip")
        or alert.get("srcip")
        or "N/A"
    )
def build_prompt(alert, source_ip, knowledge):
    """
    Build the prompt sent to the LLM.
    """

    return f"""
You are an experienced Tier 1 SOC Analyst.

Use the following cybersecurity knowledge when analyzing the alert.

Relevant Security Knowledge:

{knowledge}

Analyze the following Wazuh security alert using only the information provided.

Alert Information:
- Rule ID: {alert["rule"]["id"]}
- Description: {alert["rule"]["description"]}
- Source IP: {source_ip}
- Timestamp: {alert["timestamp"]}

Instructions:

1. Do not assume facts that are not present.
2. If there is insufficient evidence, explicitly state "Insufficient evidence".
3. Only suggest a MITRE ATT&CK technique if it is clearly supported by the alert. Otherwise, write "Insufficient evidence".
4. Keep the analysis concise and professional.
5. Use these severity guidelines:

- Low: Informational events with minimal security impact.
- Medium: Suspicious activity that should be investigated.
- High: Strong evidence of malicious activity requiring immediate attention.
- Critical: Confirmed compromise or severe security incident.

Respond using exactly the following template.

Alert Summary:
- <One or two sentences>

Severity:
- Low / Medium / High / Critical

Possible Threat:
- <Threat or "Insufficient evidence">

MITRE ATT&CK:
- <Technique ID and Name or "Insufficient evidence">

Recommended Actions:
- Action 1
- Action 2
- Action 3

Do not add any extra sections.
Do not include explanations outside this template.
"""
def analyze_with_ai(prompt):
    try:
        response = ollama.chat(
            model=config.MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI Error: {e}"
    
def load_knowledge_base(alert):
    """
    Load only relevant cybersecurity knowledge based on the alert.
    """

    knowledge = ""

    files = []

    description = alert["rule"]["description"].lower()

    if "ssh" in description:
        files.append("knowledge_base/ssh_authentication.md")
        files.append("knowledge_base/mitre_attack.md")

    files.append("knowledge_base/soc_investigation.md")

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                knowledge += file.read()
                knowledge += "\n\n"
        except FileNotFoundError:
            print(f"Warning: {file_path} not found.")

    return knowledge
def retrieve_knowledge(query):
    response = ollama.embed(
    model="nomic-embed-text",
    input=query
)

    query_embedding = np.array(
        response["embeddings"][0]
    ).astype("float32")

    query_embedding = np.expand_dims(query_embedding, axis=0)

    distances, indices = index.search(query_embedding, 3)

    knowledge = ""

    for idx in indices[0]:
        document = EMBEDDING_DATA[idx]["document"]

        with open(document, "r", encoding="utf-8") as file:
            knowledge += file.read()
            knowledge += "\n\n"

    return knowledge   
def main():
    with open(config.REPORT_FILE, "w", encoding="utf-8") as report:

        report.write("# AI SOC Security Analysis Report\n\n")
        report.write("---\n\n")

        try:
            with open(config.INPUT_FILE, "r") as file:



                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    try:
                        alert = json.loads(line)
                    except json.JSONDecodeError:
                        print("Warning: Skipping invalid JSON line.")
                        continue

                    print("=" * 60)
                    print("Rule ID:", alert["rule"]["id"])
                    print("Description:", alert["rule"]["description"])

                    source_ip = extract_source_ip(alert)
                    knowledge = retrieve_knowledge(alert["rule"]["description"])

                    print("Source IP:", source_ip)
                    print("Timestamp:", alert["timestamp"])

                    prompt = build_prompt(alert, source_ip, knowledge)

                    analysis = analyze_with_ai(prompt)

                    print("\nAI Analysis")
                    print("-" * 40)
                    print(analysis)

                    report.write(f"## Rule ID: {alert['rule']['id']}\n")
                    report.write(f"**Description:** {alert['rule']['description']}\n\n")
                    report.write(f"**Source IP:** {source_ip}\n\n")
                    report.write(f"**Timestamp:** {alert['timestamp']}\n\n")

                    report.write("## AI Analysis\n\n")
                    report.write(analysis)
                    report.write("\n\n---\n\n")

        except FileNotFoundError:
            print(f"Error: Input file '{config.INPUT_FILE}' not found.")
            sys.exit(1)

        print("\nReport saved successfully!")


if __name__ == "__main__":
    main()