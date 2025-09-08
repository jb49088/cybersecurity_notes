| Flag       | Description                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------- |
| `-sS`      | Performs a **stealth SYN scan** (default for privileged users).                                 |
| `-sT`      | Conducts a **TCP connect scan** (used when SYN scan is not possible).                           |
| `-sU`      | Performs a **UDP scan** to detect open UDP ports.                                               |
| `-p`       | Specifies **which ports** to scan (e.g., `-p 80,443` or `-p 1-65535`).                          | 
| `-O`       | Enables **OS detection** to determine the target’s operating system.                            |
| `-sV`      | Enables **service version detection** on open ports.                                            |
| `-A`       | Runs **aggressive scan** (includes OS detection, service detection, and traceroute).            |
| `-T[0-5]`  | Adjusts **scan timing** (e.g., `-T4` for faster scans, `-T2` for stealthy scans).               |
| `-Pn`      | Disables **ping discovery**, treating all hosts as online.                                      |
| `--script` | Runs **Nmap Scripting Engine (NSE) scripts** for vulnerability testing (e.g., `--script=vuln`). |