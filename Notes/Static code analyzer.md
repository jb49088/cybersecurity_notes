
# Static code analyzers

Static code analyzers are tools that scan source code for potential security flaws and vulnerabilities without executing the program. They are commonly used in security testing to identify weaknesses early in the development process, helping to prevent security issues before the software is deployed.

Static Application Security Testing (SAST) is a type of static code analysis designed to detect security flaws in the code. These tools are particularly effective at identifying common vulnerabilities such as buffer overflows, database injections, and other easily detectable issues.

However, not all security risks can be detected through static analysis alone. For example, issues related to authentication security or insecure cryptography may not be identified by these tools. As such, it's important not to rely solely on automated analysis. Each finding still requires manual verification to ensure its accuracy. False positives can be an issue, so careful review is necessary.

---

See also:

- [[Vulnerability scanning]]
- [[Buffer overflow]]
- [[Injection attack]]
- [[Fuzzing]]
