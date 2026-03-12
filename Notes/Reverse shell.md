# Reverse shell

A reverse shell is a type of remote access technique where the target machine initiates an outbound connection back to the attacker's machine, rather than the attacker connecting directly to the target. This inverts the traditional client-server model and is one of the most commonly used techniques for establishing interactive shell access after exploiting a vulnerability.

- **Why reverse over bind:** The alternative to a reverse shell is a bind shell, where a listener is opened on the target and the attacker connects inward. Bind shells are frequently blocked by firewalls that restrict unsolicited inbound connections. Because reverse shells originate as outbound connections from the target, they commonly bypass these restrictions since most firewalls are more permissive with outbound traffic.
- **How it works:** After exploiting a vulnerability that provides code execution, an attacker delivers a reverse shell payload to the target. The payload causes the target machine to open a connection back to an IP address and port the attacker controls, where a listener is waiting to catch the connection and interact with the resulting shell.
- **Listeners:** The attacker must have a listener running before the reverse shell payload is executed. Netcat is the most basic and commonly used listener, while Metasploit's multi/handler provides a more feature-rich alternative capable of handling staged payloads and providing a Meterpreter session.
- **Common payload languages:** Reverse shell payloads can be written in virtually any language available on the target system. Bash, Python, PHP, Perl, PowerShell, and Ruby one-liners are among the most commonly used, with the choice depending on what interpreter is available on the target.
- **Staged vs stageless payloads:** Stageless payloads contain the entire reverse shell code in a single self-contained package. Staged payloads send a small initial stager that connects back to the attacker and downloads the full payload in a second stage, reducing the initial payload size and evading some detection mechanisms.
- **Upgrading shells:** Raw reverse shells are often limited and unstable, lacking features like tab completion, job control, and the ability to run interactive programs. Upgrading a raw shell to a fully interactive TTY using Python's pty module or tools like rlwrap is a standard step after catching a reverse shell.
- **Detection and evasion:** Reverse shells are a well known indicator of compromise and are detected by network monitoring tools watching for unexpected outbound connections, particularly on common listener ports. Attackers frequently use ports 80 or 443 to blend reverse shell traffic with legitimate web traffic and evade detection.

Reverse shells are a fundamental technique in offensive security that bridge the gap between initial code execution and interactive control of a target system, and understanding how to generate, catch, and stabilize them is an essential practical skill for penetration testing and CTF challenges alike.

---

See also:

- [[Remote code execution (RCE)]]
- [[Web shell]]
- [[Bind shell]]
- [[Netcat]]
- [[Metasploit]]
- [[Firewall]]
- [[Capture the flag (CTF)]]
