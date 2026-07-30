import json
import ollama

report = open("reports/ai_soc_report.md", "w", encoding="utf-8")

report.write("# AI SOC Security Analysis Report\n\n")
report.write("---\n\n")

with open("sample_logs/ssh_failed_alerts.json", "r") as file:

    for line in file:

        line = line.strip()

        if not line:
            continue

        alert = json.loads(line)

        print("=" * 60)
        print("Rule ID:", alert["rule"]["id"])
        print("Description:", alert["rule"]["description"])

        source_ip = (
            alert.get("data", {}).get("srcip")
            or alert.get("srcip")
            or "N/A"
        )

        print("Source IP:", source_ip)
        print("Timestamp:", alert["timestamp"])

        prompt = f"""
You are an experienced Tier 1 SOC Analyst.

Analyze the following Wazuh security alert.

Rule ID: {alert["rule"]["id"]}
Description: {alert["rule"]["description"]}
Source IP: {source_ip}
Timestamp: {alert["timestamp"]}

Respond using exactly the following format:

Alert Summary:
Severity:
Possible Threat:
MITRE ATT&CK Technique (if applicable):
Recommended Actions:

Keep the response concise and professional.
"""

        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print("\nAI Analysis")
        print("-" * 40)
        print(response["message"]["content"])
        report.write(f"## Rule ID: {alert['rule']['id']}\n")
        report.write(f"**Description:** {alert['rule']['description']}\n\n")
        report.write(f"**Source IP:** {source_ip}\n\n")
        report.write(f"**Timestamp:** {alert['timestamp']}\n\n")

        report.write("## AI Analysis\n\n")
        report.write(response["message"]["content"])
        report.write("\n\n---\n\n")
report.close()

print("\nReport saved successfully!")        