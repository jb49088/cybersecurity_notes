
# Dynamic-link library (DLL)

A dynamic-link library (DLL) is a file format used by Microsoft Windows that contains code and data which can be shared by multiple programs simultaneously. This allows different applications to access common functions or resources without duplicating the code, improving memory efficiency and simplifying updates.

However, DLLs can be exploited in cyberattacks, particularly through techniques like DLL injection and DLL sideloading. DLL injection occurs when a malicious DLL is injected into the memory space of a running process, enabling attackers to execute arbitrary code within that process. DLL sideloading involves tricking a program into loading a malicious DLL in place of a legitimate one, often exploiting search order vulnerabilities to load a compromised version.

Both techniques are commonly used in malware attacks, as they allow attackers to bypass security controls and execute malicious code in the context of trusted applications.

---

See also:

- [[DLL injection]]
- [[DLL sideloading]]
