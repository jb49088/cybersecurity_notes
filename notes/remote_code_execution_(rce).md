# Remote code execution (RCE)

Remote code execution (RCE) is a critical vulnerability class that allows an attacker to run arbitrary code on a target system from a remote location without requiring prior physical or local access. RCE is consistently ranked among the most severe vulnerability types, as successful exploitation can result in complete system compromise, data exfiltration, and lateral movement through a network.

- **Arbitrary code execution:** RCE gives an attacker the ability to execute any code they choose on the target system, limited only by the privileges of the process being exploited. This can include spawning shells, installing malware, exfiltrating data, or using the compromised system as a pivot point for further attacks.
- **Common vulnerability classes leading to RCE:** RCE can be achieved through a wide variety of underlying vulnerabilities including command injection, insecure deserialization, server-side template injection, file upload vulnerabilities, memory corruption, and exploitation of unpatched software vulnerabilities.
- **Command injection:** One of the most direct paths to RCE in web applications, command injection occurs when user-supplied input is passed unsanitized to a system shell, allowing an attacker to append or inject arbitrary operating system commands that the server executes.
- **Deserialization vulnerabilities:** Applications that deserialize untrusted data without proper validation can be exploited to achieve RCE by supplying a crafted serialized object that triggers malicious code execution during the deserialization process.
- **File upload vulnerabilities:** Web applications that allow file uploads without properly validating file type or content can be exploited by uploading a malicious executable or web shell, which can then be triggered to achieve RCE on the server.
- **Impact and severity:** RCE is almost universally rated as critical severity in bug bounty programs, as it typically results in full compromise of the affected system. A successful RCE finding on an in-scope target is among the highest value submissions a bug bounty hunter can make.
- **Chaining to RCE:** In practice, RCE is frequently achieved not through a single vulnerability but by chaining multiple lower-severity findings together. For example, a file inclusion vulnerability combined with a file upload may be chained to achieve code execution that neither vulnerability would enable independently.

Remote code execution represents the highest tier of impact in most vulnerability taxonomies, and the ability to identify and demonstrate RCE in a controlled and responsible manner is one of the most valued skills in both bug bounty hunting and professional penetration testing.

---

See also:

- [[command_injection]]
- [[code_injection]]
- [[buffer_overflow]]
- [[privilege_escalation]]
- [[input_sanitization]]
- [[binary_exploitation]]
