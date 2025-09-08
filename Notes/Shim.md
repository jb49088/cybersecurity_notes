
# Shim

A shim refers to a small piece of code used to alter the behavior of a software application or system, typically by modifying how the software interacts with other components or libraries. Shims are often used to fix compatibility issues, implement new features, or redirect function calls without altering the underlying codebase.

While shims can be used for legitimate purposes, such as software patching or compatibility adjustments, they can also be exploited for malicious purposes. Attackers might use shims to intercept system or application calls, bypass security measures, or inject malicious code. For instance, a shim can be placed to redirect the loading of a legitimate Dynamic-Link Library (DLL) to a malicious version, essentially performing a DLL hijacking attack.

In a typical attack scenario, a shim may be used to manipulate the execution flow of a process or to bypass security measures like code signing or antivirus detection. Since shims are often small and focused on specific tasks, they can be very difficult to detect without in-depth analysis.

---

See also:

- [[Malware]]
- [[Code injection]]