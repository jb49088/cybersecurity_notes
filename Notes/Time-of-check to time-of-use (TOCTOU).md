
# Time-of-check to time-of-use (TOCTOU)

Time-of-check to time-of-use (TOCTOU) is a type of race condition where an attacker exploits the time gap between checking a system condition (such as file permissions, system state, or resource availability) and actually using the results of that check. During this brief period, the system's state may change, allowing the attacker to manipulate the system to their advantage.

For example, consider a situation where a program checks whether a file exists and has appropriate permissions (time-of-check). Between the time the program checks this condition and the time it attempts to access the file (time-of-use), the attacker might alter the file or its permissions. This could lead to unintended behavior, such as unauthorized file access or privilege escalation.

TOCTOU vulnerabilities are challenging to detect because the exploit occurs in a narrow window of time and requires precise timing. Securing systems against TOCTOU attacks typically involves ensuring that conditions are checked and used in a way that prevents changes during the process, such as by using locks, atomic operations, or preventing changes to critical system states between checks and actions.

---

See also:

- [[Race condition]]
- [[Privilege escalation]]