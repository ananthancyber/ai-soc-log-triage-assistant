import json
from ollama import chat

# Load the Wazuh alert
with open("sample_logs/wazuh_alert.json", "r") as file:
    alert = json.load(file)

# Create a prompt for the AI
prompt = f"""
You are a SOC Analyst.

Analyze the following Wazuh alert and provide:

1. Incident Summary
2. Severity
3. Possible MITRE ATT&CK Technique
4. Investigation Recommendations

Wazuh Alert:
{json.dumps(alert, indent=2)}
"""

# Send the prompt to the local AI model
response = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# Print the AI response
print(response["message"]["content"])