
# Process Hollowing

Process hollowing is a technique used by attackers to inject malicious code into the memory space of a legitimate, running process. The attacker first creates a new process in a suspended state, then removes (or "hollows out") the legitimate code in memory and replaces it with malicious code. After this, the process is resumed, executing the attacker's code while appearing as a legitimate process to the operating system and security software.

This technique is commonly used in malware attacks to evade detection, as the malicious code runs within the context of a trusted process, making it difficult for traditional security tools to differentiate between normal and malicious behavior. Process hollowing is often used to bypass security measures, maintain persistence, or carry out tasks like data theft, keylogging, or launching further attacks.

Defending against process hollowing requires monitoring for abnormal process behaviors, such as unusual memory activity or unexpected code injection, and employing advanced detection techniques like behavior-based analysis.

---

See also:

- [[Malware]]
- [[Code injection]]
- [[DLL injection]]