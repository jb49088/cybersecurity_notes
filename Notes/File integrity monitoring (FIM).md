# File integrity monitoring (FIM)

File integrity monitoring (FIM) is a security process that involves tracking and monitoring changes to critical files on a system. The goal is to detect unauthorized modifications to files that are crucial for system integrity and security. By ensuring that important files remain unchanged unless authorized, FIM helps prevent potential attacks, malware infections, or system misconfigurations.

- **Some files change all the time:** Certain system files and application files are frequently updated or modified as part of regular operations, such as log files or user-generated data.
- **Some files should NEVER change:** Key system files, operating system files, and application binaries should remain unchanged to preserve system security and integrity. Unauthorized changes to these files can be a sign of a security breach.
- **Monitor important operating system and application files:** FIM focuses on monitoring sensitive files, such as critical OS files, configurations, and application files, to ensure they remain secure.
- **Identify when changes occur:** FIM systems detect any unauthorized or unexpected changes to monitored files, alerting administrators to potential issues.
- **Windows - SFC (System File Checker):** Windows operating systems use the built-in SFC tool to scan and repair corrupted or altered system files.
- **Linux - Tripwire:** Tripwire is a well-known tool for Linux systems that can monitor and verify file integrity, providing alerts for unauthorized changes.
- **Many host-based IPS options:** Many host-based intrusion prevention systems (IPS) also include FIM capabilities, adding an extra layer of protection by monitoring file integrity alongside other security measures.
    
File integrity monitoring is an essential security measure that helps ensure the integrity and trustworthiness of systems by identifying unauthorized changes before they can have significant consequences.

---

See also:

- [[Intrusion prevention system (IPS)]]
- [[Data loss prevention (DLP)]]