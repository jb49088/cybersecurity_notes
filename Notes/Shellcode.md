
# Shellcode

Shellcode is a small piece of code used as the payload in a cyberattack, typically written in machine code or assembly language. It is designed to exploit vulnerabilities in a system, allowing an attacker to execute arbitrary commands, often by taking control of a running process. Shellcode gets its name because it often spawns a command shell, providing the attacker with access to the compromised system.

Shellcode is commonly used in exploits like buffer overflows, where the attacker manipulates the program's memory to inject and execute their own code. Once executed, shellcode can perform various malicious actions, such as escalating privileges, downloading additional malware, exfiltrating data, or even taking full control of the system.

Given its small and efficient nature, shellcode is particularly useful in scenarios where stealth and minimal footprint are necessary. Defending against shellcode typically involves techniques such as input validation, memory protection (e.g., Data Execution Prevention), and using up-to-date security patches to close vulnerabilities.

---

See also:

- [[Malware]]