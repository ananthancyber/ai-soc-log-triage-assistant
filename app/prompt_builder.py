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