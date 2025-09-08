
# Remote code execution (RCE)

Remote code execution (RCE) is a critical security vulnerability that allows an attacker to execute arbitrary code on a target system from a remote location. Exploiting RCE vulnerabilities enables attackers to take control of a system, steal sensitive data, deploy malware, or disrupt operations.

Common causes of RCE include:

- **Input Validation Failures:** Applications improperly handle user-supplied input, allowing malicious code injection.
- **Outdated Software:** Vulnerabilities in unpatched software can be exploited to execute code remotely.
- **Insecure Deserialization:** Unsafe handling of serialized data can allow attackers to inject and execute code.

RCE attacks pose significant risks, such as full system compromise, data breaches, and ransomware deployment. Mitigation involves patching vulnerabilities promptly, validating and sanitizing inputs, and adhering to secure coding practices.

---

See also:

- [[Code injection]]
- [[Buffer overflow]]
- [[Privilege escalation]]
- [[Input sanitization]]
