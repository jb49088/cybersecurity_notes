# Deep packet inspection (DPI)

[[🏷️Network security]]

Deep packet inspection (DPI) is a network traffic analysis technique that examines the contents of packets beyond just their headers. Unlike traditional packet filtering, which only evaluates source/destination IP addresses and port numbers, DPI inspects the actual payload of packets to identify protocols, applications, and threats in real time.

- **Application identification:** DPI can identify the true application or protocol being used regardless of port number, meaning SSH disguised as HTTP traffic on port 80 can still be detected and blocked.
- **Threat detection:** DPI is used by intrusion detection and prevention systems (IDS/IPS) to identify malicious payloads, exploits, and command-and-control traffic embedded within otherwise legitimate-looking packets.
- **Protocol fingerprinting:** Even without reading plaintext content, DPI can identify protocols by analyzing handshake patterns, packet size distributions, and timing — making it effective against traffic that attempts to blend in.
- **TLS/encrypted traffic:** DPI has limited visibility into encrypted payloads, however metadata such as SNI headers, certificate information, and TLS handshake fingerprints (JA3/JA3S) still reveal significant information about the traffic without decryption.
- **TLS inspection:** Enterprise DPI solutions can perform man-in-the-middle decryption by acting as a TLS proxy, fully decrypting, inspecting, and re-encrypting traffic. This requires a trusted root certificate installed on client devices.
- **Evasion techniques:** From an offensive perspective, DPI can be evaded through traffic obfuscation, protocol mimicry, encrypting C2 communications over common protocols like HTTPS or DNS, and fragmenting packets to prevent signature matching.

DPI is a powerful tool for both defenders and a well-understood obstacle for attackers, making knowledge of its capabilities and limitations essential for offensive security work.

---

See also:

- [[Firewall]]
- [[Next-generation firewall (NGFW)]]
- [[Intrusion detection system (IDS)]]
- [[Intrusion prevention system (IPS)]]
- [[Transport layer security (TLS)]]
