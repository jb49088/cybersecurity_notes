# Reverse engineering

Reverse engineering in cybersecurity is the process of analyzing a compiled program, binary, or system to understand its internal logic, functionality, and behavior without access to the original source code. It is a foundational skill in malware analysis, vulnerability research, exploit development, and CTF competitions.

- **Static analysis:** Involves examining a binary without executing it, using tools like disassemblers and decompilers to convert machine code back into human-readable assembly or pseudo-code. This approach is safe for analyzing potentially malicious software as it does not require running the program.
- **Dynamic analysis:** Involves executing the binary in a controlled environment and observing its behavior in real time, including system calls made, files accessed, network connections initiated, and memory contents. Debuggers are the primary tool for dynamic analysis, allowing analysts to step through execution and inspect state at any point.
- **Disassemblers and decompilers:** Tools like Ghidra, IDA Pro, and Binary Ninja are the primary platforms for reverse engineering, converting raw binary machine code into assembly language or higher-level pseudo-code that is significantly easier to reason about than raw bytes.
- **Common targets:** Reverse engineering is applied to malware samples to understand their capabilities and indicators of compromise, to proprietary software to identify vulnerabilities, to firmware of embedded devices and IoT hardware, and to CTF challenges where binaries must be analyzed to extract hidden flags.
- **Anti-reversing techniques:** Malware authors and software vendors frequently employ techniques to hinder reverse engineering, including code obfuscation, packing, encryption of strings and payloads, anti-debugging checks, and virtual machine detection. Overcoming these protections is a significant part of advanced reverse engineering work.
- **Relevance to bug bounty:** While reverse engineering is less central to web-focused bug bounty hunting, it becomes relevant when targets include mobile applications, thick client software, or compiled binaries where understanding the application's logic requires analyzing the binary directly.

Reverse engineering is one of the most technically demanding disciplines in cybersecurity, requiring a strong understanding of computer architecture, assembly language, and operating system internals, but it is also among the most powerful skills for deeply understanding how software behaves at the lowest level.

---

See also:

- [[capture_the_flag_(ctf)]]
- [[malware]]
- [[malware_analysis]]
- [[binary_exploitation]]
