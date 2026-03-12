# PATH hijacking

Path hijacking is an attack technique where a malicious actor manipulates how an operating system searches for and executes programs or scripts by exploiting the order in which directories are searched in the system's PATH environment variable. By placing a malicious executable in a directory that is searched before the legitimate one, an attacker can cause the system to run their code instead of the intended program.

- **PATH environment variable abuse:** Operating systems use the PATH variable to locate executables when a command is run without a full file path. If an attacker can influence the order of directories in PATH, they can redirect execution to a malicious binary.
- **Relative path exploitation:** Scripts or programs that call other executables using relative paths rather than absolute paths are particularly vulnerable, as the attacker only needs to place a malicious file in the current working directory or another early-searched location.
- **Privilege escalation:** Path hijacking is frequently used as a privilege escalation technique, particularly on Linux systems. If a script running as root calls an executable using a relative path, a low-privileged attacker can hijack that call to execute arbitrary code with elevated permissions.
- **Writable directories in PATH:** If a directory listed in the PATH variable is writable by a non-privileged user, an attacker can plant a malicious binary there, waiting for a higher-privileged process to invoke it.
- **Prevention:** Mitigation involves using absolute paths in scripts and programs, restricting write permissions on directories listed in PATH, and auditing scheduled tasks and startup scripts for unsafe path references.

Path hijacking is a subtle but impactful technique, often discovered during privilege escalation phases of a penetration test, and highlights the importance of secure coding practices and strict file system permissions.

---

See also:

- [[privilege_escalation]]
- [[environment_variable]]
