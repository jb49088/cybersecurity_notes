
# Command injection

[[🏷️Injection attack]]

Command injection is a type of attack where an attacker is able to execute arbitrary commands on a host operating system through a vulnerable application. This occurs when an application improperly processes user input and allows it to be interpreted as part of a system command. Successful command injection can lead to unauthorized access, data leakage, system compromise, and further exploitation of the affected system.

- **Vulnerable input fields**: Attackers often exploit input fields, such as search bars, forms, or URL parameters, that are not properly sanitized or validated.
- **Execution of arbitrary commands**: By injecting malicious commands, attackers can execute operating system commands, manipulate files, install malware, or escalate privileges.
- **Risk to web applications**: Command injection vulnerabilities are common in web applications, especially in those that interact with system processes or rely on external utilities (e.g., pinging a host, executing a script).
- **Mitigation techniques**: Proper input validation and sanitization, use of parameterized queries, least privilege access controls, and secure coding practices can help prevent command injection.
- **Examples**: An attacker may inject commands like `; rm -rf /` to delete all files or `| ls` to list system files when input is incorrectly processed by the application.
    

Command injection is a significant security concern, as it allows attackers to manipulate the underlying system, bypass application security mechanisms, and potentially gain control over the server or network.

---

See also:

