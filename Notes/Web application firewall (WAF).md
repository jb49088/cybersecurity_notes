
# Web application firewall (WAF)

[[🏷️Web application security]]

A web application firewall (WAF) is a specialized security solution designed to protect web applications by filtering and monitoring HTTP/HTTPS traffic. Unlike traditional firewalls, which operate at the network layer, WAFs operate at the application layer to specifically address threats targeting web applications.

Key Features:

- **Rule-Based Filtering**: WAFs apply pre-configured rules to HTTP/HTTPS conversations to determine whether to allow or deny traffic based on expected input. This allows them to block attacks that exploit vulnerabilities in web applications.
- **Protection Against Exploits**: Web applications are often vulnerable to attacks due to unexpected or malicious input. A WAF protects against these types of attacks by identifying and blocking malicious input, such as SQL injection, cross-site scripting (XSS), and other injection attacks.
- **SQL Injection Prevention**: One of the most common attacks blocked by WAFs is SQL injection, where an attacker adds unauthorized SQL commands into an application’s query, potentially exposing or manipulating the database.
- **Compliance with PCI DSS**: WAFs play a crucial role in meeting security standards, particularly in the context of the Payment Card Industry Data Security Standard (PCI DSS). PCI DSS mandates the protection of sensitive cardholder data, and WAFs are a critical tool in ensuring that web applications handling such data are secure.

A web application firewall adds an essential layer of security by focusing on the protection of applications from attacks that target vulnerabilities in their code, making it especially important for organizations handling sensitive or customer-facing data.

---

See also:

- [[Firewall]]
- [[Hypertext transfer protocol (HTTP)]]
- [[Hypertext transfer protocol secure (HTTPS)]]
- [[Injection attack]]
- [[SQL injection (SQLi)]]
- [[Cross-site scripting (XSS)]]
- [[Payment Card Industry Data Security Standard (PCI DSS)]]