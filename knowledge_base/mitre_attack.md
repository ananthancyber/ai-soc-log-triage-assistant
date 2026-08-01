# MITRE ATT&CK Reference

## Overview

The MITRE ATT&CK framework is a knowledge base of adversary tactics and techniques based on real-world observations.

It helps security analysts classify attacker behavior and standardize investigations.

---

## T1110 – Brute Force

### Description

Brute Force is a technique in which an attacker repeatedly attempts different credentials to gain unauthorized access to a system.

### Indicators

- Multiple failed login attempts
- Repeated authentication failures
- Attempts against multiple user accounts
- High volume of authentication requests

### SOC Response

- Review authentication logs
- Identify repeated source IP addresses
- Determine whether any login attempts succeeded
- Consider blocking malicious IP addresses if appropriate

---

## Valid Accounts

Successful authentication after repeated failed attempts may indicate abuse of valid credentials.

Analysts should verify whether the login activity matches normal user behavior.

---

## Important Note

A single failed authentication event is not sufficient evidence to conclude a brute-force attack.

Analysts should correlate multiple alerts before mapping activity to MITRE ATT&CK techniques.