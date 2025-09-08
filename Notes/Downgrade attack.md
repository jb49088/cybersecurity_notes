
# Downgrade attack

[[🏷️Cryptographic attack]]

A downgrade attack occurs when an attacker forces a communication protocol to revert to an older, less secure version in order to exploit known vulnerabilities. This typically happens when the attacker intercepts and manipulates the negotiation process between two systems, convincing them to use weaker encryption or authentication methods than originally intended.

For example, an attacker might force a secure connection (such as HTTPS) to fall back to an older, insecure protocol like HTTP, which can be easily intercepted or tampered with. Downgrade attacks are common in protocols like SSL/TLS, where vulnerabilities in older versions can be leveraged for malicious purposes.

To mitigate downgrade attacks, it's important to disable outdated protocol versions and enforce the use of strong, secure protocols. Regularly updating software and security configurations also helps protect against these types of attacks.

---

See also:

- [[SSL stripping]]
- [[Insecure Protocols]]