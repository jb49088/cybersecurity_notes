
# Signature-based detection

Signatures are specific patterns or characteristics used to detect known threats in cybersecurity. These patterns could be based on known malware, attacks, or vulnerabilities, and they play a key role in identifying threats by matching incoming data or activity to a database of known attack signatures.

- **File signatures**: Unique identifiers like hashes (MD5, SHA) that represent specific files, which are used to detect known malicious files.
- **Network signatures**: Patterns of network traffic or specific behaviors that indicate potential attacks, such as DDoS, port scans, or other malicious network activity.
- **Protocol signatures**: Recognizing unusual or malformed protocol usage, such as invalid packets or suspicious handshakes, which are indicative of attacks like buffer overflows or exploitation attempts.
- **Behavioral signatures**: These are based on known attack actions like file encryption by ransomware, or unusual system behavior, allowing the detection of attacks even if they don't match exactly a previous signature.

Signature-based detection is widely used in Intrusion Detection Systems (IDS), Intrusion Prevention Systems (IPS), antivirus software, and firewalls. It works by comparing the observed traffic or system activity against known attack patterns. When a match is found, an alert is triggered or the malicious activity is blocked.

Signature-based detection offers fast and efficient identification of known threats, with minimal resource usage. However, it is limited to recognizing only known threats and cannot detect new or unknown attacks until signatures are created. Additionally, it may miss sophisticated or polymorphic malware that alters its code to evade detection.

---

See also:

- [[Anomaly-based detection]]
- [[Intrusion detection system (IDS)]]
- [[Intrusion prevention system (IPS)]]
- [[Endpoint detection and response (EDR)]]
- [[Antivirus (AV)]]
- [[Firewall]]