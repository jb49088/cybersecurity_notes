
# DNS tunneling

[[🏷️Network attack]]

DNS tunneling is a technique that uses DNS queries and responses to tunnel data, often bypassing firewalls and security filters. It encodes data into DNS requests, which are sent to a DNS server controlled by an attacker. The server then decodes and responds with additional DNS packets, allowing data to be exfiltrated or enabling command-and-control communication.

This method is hard to detect because DNS is a commonly used and trusted protocol. While often exploited for malicious purposes like data theft or system control, DNS tunneling can also be used by security researchers to test network defenses.

---

See also:

- [[Domain name system (DNS)]]
- [[Command and control (C2)]]
