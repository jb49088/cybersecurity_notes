
# Indicators of compromise (IoC)

Indicators of compromise (IoC) are artifacts or patterns found in system logs, files, or network traffic that suggest a security breach or malicious activity has occurred. These can include things like unusual login activity, resource spikes, or missing logs, and they help security teams detect, analyze, and respond to potential threats.

## Common indicators of compromise

- **Account Lockout:** When credentials are not working, it’s important to investigate. Account lockouts typically occur after exceeding the number of allowed failed login attempts. This could indicate an attacker is trying to break into the account and has locked it in the process. An attacker may even lock the account and then call support to reset the password as part of a larger attack plan.
- **Concurrent Session Usage:** It’s physically impossible to be in two places at once. Multiple logins from different locations or devices under the same user account suggest suspicious activity. This could be an attacker using stolen credentials from different geographical locations. Log analysis is necessary to identify these anomalies, especially when automated processes are involved.
- **Blocked Content:** Attackers may block access to security updates, anti-malware tools, or patches to maintain their foothold. If a system shows signs of blocked updates or tools, it’s a strong indicator of an ongoing attack. Attackers often try to stop any defensive mechanisms that might disrupt their control.
- **Impossible Travel:** A login from one location, followed shortly by a login from a geographically distant location (e.g., a login from Omaha, Nebraska followed by a login from Melbourne, Australia within minutes), is an indicator that something is wrong. This is impossible without stolen credentials. Monitoring login activity and analyzing logs can help identify this IoC.
- **Resource Consumption:** Unusual spikes in system resources, such as bandwidth usage or file transfers, can point to malicious activity like data exfiltration or denial-of-service attacks. Monitoring firewall logs and looking for unusual traffic patterns can help detect attackers attempting to send data outside the network.
- **Resource Inaccessibility:** When systems or network resources are suddenly unavailable, it could indicate an attack, such as a ransomware encryption process or other exploits. Network disruptions or server outages may be an attempt to cover up the exploit or make the attack more difficult to trace.
- **Out-of-Cycle Logging:** Logs that appear outside of normal maintenance windows—such as operating system patches or unexpected firewall activity—are suspicious. They may indicate that an attacker is actively exploiting or manipulating the system without detection.
- **Missing Logs:** When logs are deleted or tampered with, it's a clear sign that an attacker is trying to erase their traces. Missing logs, such as those from authentication, file access, or firewall activity, should be immediately flagged as suspicious. Securing logs and monitoring them regularly is vital for detecting such activity.
- **Published/Documented:** If attackers post stolen data online, it’s a significant red flag. Often, this happens in conjunction with ransomware attacks. The release of raw data or documents without context can reveal the extent of the breach and should be investigated to trace the source and mitigate further damage.
---

See also:

- [[Indicators of attack (IoA)]]
- [[Pyramid of pain]]
