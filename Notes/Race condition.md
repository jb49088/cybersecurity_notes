
# Race condition

A race condition occurs when a program's behavior depends on the timing of events, such as the order in which certain processes or threads are executed. This can lead to unpredictable results, especially if two or more operations happen simultaneously and interfere with one another. Race conditions are particularly problematic when the program is not designed to handle such concurrency, leading to unintended consequences like data corruption, security vulnerabilities, or system crashes.

One common type of race condition is the time-of-check to time-of-use (TOCTOU) attack. In a TOCTOU scenario, an attacker exploits the window between when a system checks a condition (e.g., file permissions or system state) and when the result of that check is used. If something changes in that gap—such as a file being altered or a privilege being escalated—the program may act on outdated or incorrect information, resulting in unauthorized access or other security risks.

---

See also:

- [[Time-of-check to time-of-use (TOCTOU)]]