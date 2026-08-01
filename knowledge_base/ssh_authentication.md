# SSH Authentication

## Overview

SSH (Secure Shell) is a network protocol used to securely access and manage remote systems over an encrypted connection.

Authentication is the process of verifying a user's identity before granting access to the remote host.

---

## Failed Authentication Attempts

Failed SSH authentication may occur because of:

- Incorrect username
- Incorrect password
- Invalid user account
- Disabled account
- Expired credentials

Occasional failed logins are normal.

Repeated failed login attempts from the same source may indicate malicious activity.

---

## Common Attack Techniques

Attackers frequently target SSH services using:

- Credential Guessing
- Password Spraying
- Brute Force Attacks
- Valid Account Abuse

---

## Indicators of Suspicious Activity

Examples include:

- Multiple failed logins from the same IP address
- Repeated attempts against different usernames
- Authentication attempts occurring within a short period
- Authentication attempts outside normal business hours

---

## Initial SOC Investigation

A SOC analyst should consider:

- Reviewing authentication logs
- Identifying repeated source IP addresses
- Checking whether any login eventually succeeded
- Determining whether the source IP is internal or external
- Reviewing previous alerts involving the same host

---

## Notes

A single failed SSH login does not necessarily indicate an attack.

Additional context is required before concluding that malicious activity is occurring.