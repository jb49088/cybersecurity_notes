# Web shell

A web shell is a malicious script uploaded to a web server that provides an attacker with remote access and control over the server through a web browser. By navigating to the uploaded file, an attacker can execute commands, browse the file system, exfiltrate data, and maintain persistent access to the compromised server, effectively turning a file upload vulnerability or misconfiguration into a full remote administration backdoor.

- **How it works:** A web shell is typically a small script written in the same language the web server executes, commonly PHP, ASP, JSP, or Python. Once uploaded and accessible via a URL, it accepts commands through HTTP requests, passes them to the server's shell or interpreter, and returns the output to the attacker's browser.
- **Common upload vectors:** Web shells are most commonly installed by exploiting unrestricted file upload vulnerabilities, remote code execution flaws, compromised content management systems, or misconfigured web server directories that allow write access to publicly accessible locations.
- **Appearance and simplicity:** Some of the most effective web shells are extremely small. A minimal PHP web shell can be as short as a single line, such as a script that passes a URL parameter directly to a PHP execution function, demonstrating that file size and complexity are not reliable indicators of a web shell's presence.
- **Obfuscation:** Attackers frequently obfuscate web shell code using base64 encoding, XOR encoding, or string manipulation to evade file scanning, signature-based detection, and web application firewalls that look for known malicious patterns.
- **Persistence:** Web shells provide persistent access that survives password changes, session expiry, and many remediation attempts, as they exist as files on the server rather than relying on an active session. This makes them a common tool for maintaining long-term access after initial compromise.
- **Detection:** Web shells can be detected through file integrity monitoring, web server log analysis looking for unusual POST requests to static files, and scanning tools that identify suspicious scripts in web-accessible directories. Behavioral anomalies such as a web server process spawning unexpected child processes are also strong indicators.
- **Bug bounty context:** Demonstrating a web shell upload in a bug bounty program is typically considered a critical finding, as it provides clear and unambiguous proof of RCE on the target server. Most programs require responsible disclosure and prohibit actually executing commands beyond what is necessary to demonstrate impact.

Web shells sit at the intersection of file upload vulnerabilities and remote code execution, representing one of the most impactful and tangible demonstrations of server compromise available to an attacker or security researcher.

---

See also:

- [[Remote code execution (RCE)]]
- [[Command injection]]
- [[Base64]]
- [[Exclusive or (XOR)]]
- [[Misconfiguration]]
