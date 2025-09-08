
# DLL injection

[[🏷️Injection attack]]

DLL injection is a technique used by attackers to insert a malicious dynamic-link library (DLL) into the address space of a running process. This allows the injected code to be executed within the context of that process, enabling attackers to manipulate the process’s behavior, bypass security checks, or gain control over the system.

In DLL injection, the attacker typically exploits vulnerabilities in the targeted application to force it to load a malicious DLL. Once injected, the attacker can execute arbitrary code, alter the flow of execution, monitor or modify data, or even escalate privileges.

![[Image 2.75.png|center|500]]

DLL injection is commonly used in malware attacks, such as those targeting web browsers, system processes, or security software, to perform malicious actions without detection. Defending against DLL injection involves securing applications, using anti-malware tools, and applying techniques like code integrity checks to ensure only trusted DLLs are loaded.

---

See also:

- [[Dynamic-link library (DLL)]]
- [[DLL sideloading]]