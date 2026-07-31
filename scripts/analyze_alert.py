import json
import ollama
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
def build_prompt(alert, source_ip):
    """
    Build the prompt sent to the LLM.
    """

    return f"""
You are an experienced Tier 1 SOC Analyst.

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
    """
    Send the prompt to the LLM and return its response.
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

    return response["message"]["content"]

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

        source_ip = extract_source_ip(alert)

        print("Source IP:", source_ip)
        print("Timestamp:", alert["timestamp"])

        prompt = build_prompt(alert, source_ip)

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
report.close()

print("\nReport saved successfully!")        