import os
import sys
import json

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

import ollama
import config

from app.retriever import retrieve_knowledge
from app.prompt_builder import build_prompt
from app.report_generator import write_report

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
from app.prompt_builder import build_prompt

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

                    write_report(
                           report,
                           alert,
                           source_ip,
                           analysis 
                         )

        except FileNotFoundError:
            print(f"Error: Input file '{config.INPUT_FILE}' not found.")
            sys.exit(1)

        print("\nReport saved successfully!")


if __name__ == "__main__":
    main()