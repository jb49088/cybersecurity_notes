
# DLL sideloading

[[🏷️Injection attack]]

DLL sideloading is a technique where an attacker places a malicious DLL file in a location where a legitimate application is likely to search for it. When the application tries to load a required DLL, it inadvertently loads the malicious one instead. This can allow the attacker to execute arbitrary code, steal data, or compromise the system.

DLL sideloading exploits the way Windows searches for DLL files when an application runs. If a program is configured to load a DLL from a specific directory and the attacker places a malicious version in that directory, the program will load the compromised DLL without suspecting anything is wrong. This technique is commonly used in targeted attacks and is especially effective when security software fails to properly validate the integrity of the loaded DLLs.

To defend against DLL sideloading, developers should use secure coding practices, such as specifying full paths to trusted DLLs, and ensure applications verify the integrity of loaded DLLs. Additionally, security software should monitor and alert on unusual DLL loading behavior.

---

See also:

- [[Dynamic-link library (DLL)]]
- [[DLL injection]]