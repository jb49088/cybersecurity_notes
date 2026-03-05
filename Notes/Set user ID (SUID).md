# Set user ID (SUID)

Set user ID (SUID) is a special file permission on Linux and Unix systems that allows an executable to run with the privileges of the file's owner rather than the user executing it. When applied to files owned by root, this means any user on the system can execute that binary with full root privileges, making SUID files a critical area of focus during privilege escalation.

- **How SUID works:** When the SUID bit is set on an executable, the operating system temporarily elevates the executing user's privileges to match those of the file owner for the duration of the process. This is used legitimately by programs like passwd, which need root access to modify the shadow file on behalf of regular users.
- **Identifying SUID files:** The command `find / -perm -4000 2>/dev/null` is the standard way to enumerate all SUID binaries on a system, recursively searching the filesystem for files with the SUID bit set while suppressing permission denied errors.
- **GTFOBins:** GTFOBins is an essential reference for SUID exploitation, cataloguing Unix binaries that can be abused when misconfigured with the SUID bit set. If a non-standard binary appears in SUID enumeration results, GTFOBins is the first place to check for a known exploitation technique.
- **Legitimate vs. non-standard binaries:** Common system binaries like passwd and su expectedly carry the SUID bit. The real area of interest is non-standard or unexpected binaries with the SUID bit set, such as text editors, scripting interpreters, or custom application binaries, which can often be abused to escalate privileges.
- **Custom SUID binaries:** Developers occasionally create custom SUID binaries for administrative convenience without fully understanding the security implications. These are particularly valuable targets as they may contain exploitable logic flaws or call other programs using relative paths, making them vulnerable to path hijacking.
- **Writable SUID binaries:** If a SUID binary is also writable by a low-privileged user, an attacker can replace or modify its contents entirely, trivially achieving privilege escalation.

SUID files are a foundational concept in Linux privilege escalation and are among the first things checked after gaining an initial foothold on a system, both in penetration testing engagements and CTF challenges.

---

See also:

- [[Linux]]
- [[Privilege escalation]]
- [[GTFOBins]]
