# Day 03 – Building a Robust Multi-Alert Parser

## Objectives

- Transition from a single sample alert to processing real Wazuh security alerts.
- Learn how Wazuh stores alerts inside a Docker-based deployment.
- Parse multiple JSON alerts instead of a single JSON object.
- Build a robust Python parser that can handle different Wazuh rule structures.

---

## Why Preprocess Security Logs?

Raw Wazuh alerts contain a large amount of structured information. Before sending alert data to an AI model, Python extracts only the fields that are relevant to security investigations.

This preprocessing step improves efficiency, keeps prompts focused, and prepares the data for later stages such as embeddings and Retrieval-Augmented Generation (RAG).

Typical fields extracted include:

- Timestamp
- Rule ID
- Rule description
- Severity
- Source IP
- Full log message

---

## Why Process Multiple Alerts?

A single Wazuh alert provides limited context. Security analysts often need to correlate multiple related alerts to identify attack patterns such as brute-force attempts, port scans, or repeated authentication failures.

Processing multiple alerts allows the AI assistant to analyze a sequence of security events instead of treating every alert independently.

---

## Tasks Completed

### 1. Accessed Real Wazuh Alerts

Connected to the Wazuh Manager Docker container and inspected the `alerts.json` file that stores real security events.

---

### 2. Generated Real SSH Authentication Events

Triggered multiple failed SSH login attempts from the Kali Linux VM against the Ubuntu system to generate real authentication alerts.

Generated alerts included:

- Rule 5710 – SSH login attempt using a non-existent user
- Rule 2502 – Multiple failed password attempts detected

---

### 3. Created a Real AI Dataset

Extracted only the SSH-related alerts from the Wazuh alert stream and added them to the project as:

```text
sample_logs/
└── ssh_failed_alerts.json
```

---

### 4. Implemented Multi-Alert Processing

Updated the parser to process multiple alerts stored in JSON Lines (JSONL) format instead of a single JSON object.

Implemented:

- Reading one alert at a time
- Parsing each line independently
- Displaying important alert information

---

### 5. Improved Parser Reliability

Different Wazuh rules contain different JSON structures.

The parser was updated to safely handle missing fields using Python's `.get()` method, preventing runtime errors when certain attributes (such as `srcip`) are unavailable.

---

## Key Concepts Learned

- Wazuh alert storage
- Docker container log access
- JSON vs JSON Lines (JSONL)
- `json.load()` vs `json.loads()`
- Parsing multiple alerts
- Defensive parsing using `.get()`
- Processing heterogeneous Wazuh events

---

## Files Updated

```text
sample_logs/
└── ssh_failed_alerts.json

scripts/
└── analyze_alert.py

docs/
└── Day03.md
```

---

## Screenshots

- Alert preprocessing
- Real SSH authentication alerts
- Multi-alert parser output
- Robust parser handling different rule structures

---

## Outcome

By the end of Day 3, the project evolved from analyzing a single synthetic alert to processing multiple real Wazuh security events generated during the Blue Team lab.

The parser now supports multiple alerts and safely handles different event structures, providing a solid foundation for integrating AI-powered SOC triage in the next phase.