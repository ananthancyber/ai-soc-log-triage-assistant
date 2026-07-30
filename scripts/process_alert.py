import json

# Load the Wazuh alert
with open("sample_logs/wazuh_alert.json", "r") as file:
    alert = json.load(file)

# Extract important fields
processed_alert = {
    "timestamp": alert.get("timestamp"),
    "severity": alert.get("rule", {}).get("level"),
    "rule": alert.get("rule", {}).get("description"),
    "source_ip": alert.get("srcip"),
    "full_log": alert.get("full_log")
}

# Display the processed alert
print("Processed Wazuh Alert")
print("-" * 40)

for key, value in processed_alert.items():
    print(f"{key}: {value}")