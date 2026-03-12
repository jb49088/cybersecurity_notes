# GTFOBins

GTFOBins is a curated public reference list of Unix binaries that can be abused by attackers to bypass local security restrictions, escalate privileges, or execute unintended actions when misconfigured or available in restricted environments. The name is a play on "Get The F*** Out," reflecting its purpose of helping attackers break out of constrained situations using trusted system binaries.

- **Living off the land:** GTFOBins is centered around the concept of living off the land, where attackers use legitimate, pre-installed system tools rather than introducing external malware or exploits. This makes detection significantly harder as the activity blends in with normal system behavior.
- **Coverage of abuse techniques:** Each binary listed on GTFOBins includes documented techniques for how it can be abused across several categories including SUID exploitation, sudo misconfigurations, file read and write, reverse shells, and escaping restricted shells.
- **SUID abuse:** GTFOBins documents how binaries with the SUID bit set can be used to spawn privileged shells or execute commands as root, making it an essential companion to SUID file enumeration.
- **Sudo misconfigurations:** When a user is granted the ability to run specific binaries as root via sudo, GTFOBins provides techniques for abusing those binaries to break out into a full root shell, even when the permission appears innocuous at first glance.
- **Restricted shell escaping:** In environments where users are placed in restricted shells, GTFOBins documents how commonly available binaries can be leveraged to escape those restrictions and gain access to a full shell environment.
- **Usage in assessments:** During penetration testing and CTF challenges, GTFOBins is routinely consulted immediately after identifying interesting sudo permissions with `sudo -l` or unexpected SUID binaries discovered through filesystem enumeration.

GTFOBins is an indispensable reference for anyone working in offensive security, transforming the discovery of a misconfigured binary from an uncertain finding into a clearly documented and actionable privilege escalation path.

---

See also:

- [[set_user_id_(suid)]]
- [[privilege_escalation]]
- [[linux]]
- [[sudo]]
- [[living_off_the_land_(lol)]]
