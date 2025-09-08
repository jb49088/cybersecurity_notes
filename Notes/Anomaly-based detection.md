
# Anomaly-based detection

Anomaly-based detection focuses on identifying deviations from a predefined baseline of normal activity. By monitoring network traffic, system behavior, or user activity, this method detects unusual patterns that might indicate potential threats, even if the specific threat has never been encountered before.

Anomalies can be categorized in several ways:

- **Network anomalies**: Unusual patterns in network traffic, such as unexpected spikes in data flow, irregular packet sizes, or strange connection attempts, could signify attacks like DDoS or data exfiltration.
- **Host anomalies**: Unexpected behavior from a system or device, such as an unusual increase in CPU usage, unexpected file modifications, or unauthorized login attempts, may point to malware infection or unauthorized access.
- **User behavior anomalies**: Significant deviations in user behavior, such as accessing sensitive files or systems at odd hours or from unusual locations, can signal insider threats or compromised accounts.

Anomaly-based detection is useful for identifying previously unknown or zero-day threats, as it doesn't rely on predefined signatures. It can detect novel attacks that signature-based methods might miss. However, it can also lead to false positives, as legitimate activities that deviate from the norm might be incorrectly flagged as threats.

---

See also:

- [[Security baselines]]
- [[Signature-based detection]]
- [[Intrusion detection system (IDS)]]
- [[Intrusion prevention system (IPS)]]
- [[Endpoint detection and response (EDR)]]
- [[Antivirus (AV)]]
- [[Firewall]]
