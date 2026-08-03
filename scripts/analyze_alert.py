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

def main():
    print("=" * 70)
    print("AI SOC Log Triage Assistant")
    print("=" * 70)
    print()
    with open(config.REPORT_FILE, "w", encoding="utf-8") as report:

        report.write("# AI SOC Security Analysis Report\n\n")
        report.write("---\n\n")

        alert_count = 0

        try:
            with open(config.INPUT_FILE, "r", encoding="utf-8") as file:

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    try:
                        alert = json.loads(line)
                    except json.JSONDecodeError:
                        print("Warning: Skipping invalid JSON line.")
                        continue

                    alert_count += 1

                    try:
                        print("=" * 60)
                        print("Rule ID:", alert["rule"]["id"])
                        print("Description:", alert["rule"]["description"])

                        source_ip = extract_source_ip(alert)

                        knowledge, retrieved_documents = retrieve_knowledge(
                            alert["rule"]["description"]
                        )

                        print("\nRetrieved Knowledge Sources:")

                        for item in retrieved_documents:
                            print(
                                f"- {item['document']} "
                                f"(Distance: {item['distance']:.4f})"
                            )

                        print("Source IP:", source_ip)
                        print("Timestamp:", alert["timestamp"])

                        prompt = build_prompt(
                            alert,
                            source_ip,
                            knowledge
                        )

                        analysis = analyze_with_ai(prompt)

                        print("\nAI Analysis")
                        print("-" * 40)
                        print(analysis)

                        write_report(
                            report,
                            alert,
                            source_ip,
                            analysis,
                            retrieved_documents
                        )

                    except Exception as e:
                        print(f"Error processing alert: {e}")
                        continue

        except FileNotFoundError:
            print(f"Error: Input file '{config.INPUT_FILE}' not found.")
            sys.exit(1)

        report.write("# Report Summary\n\n")
        report.write(f"**Total Alerts Processed:** {alert_count}\n\n")
        report.write(f"**AI Model:** {config.MODEL_NAME}\n\n")

        print("\nReport saved successfully!")
        print(f"Processed {alert_count} alerts successfully.")
        print("Analysis completed.")
        print("=" * 70)

if __name__ == "__main__":
    main()