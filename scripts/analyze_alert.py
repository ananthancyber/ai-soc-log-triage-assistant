import json

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