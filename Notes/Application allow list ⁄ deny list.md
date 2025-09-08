
# Application allow list ⁄ deny list

An application allow list and deny list control which applications can run on a system, helping protect against malicious software and vulnerabilities. Applications can be exploited through vulnerabilities, trojan horses, or malware, making it essential to limit which programs are permitted.

Security policy typically uses allow lists (whitelisting) or deny lists (blacklisting) to manage application execution.

- **Allow List:** Only approved applications can run, offering a highly restrictive security measure.
- **Deny List:** Known harmful applications are blocked, allowing any other programs to run. Anti-virus software often uses this method to prevent malware.

Decisions about which applications are allowed or denied are typically made within the operating system, often as part of its built-in management features. These decisions can be based on various factors, such as application hash, certificate, path, or network zone. An application hash ensures that only applications with a unique identifier are allowed to run, while certificates allow only digitally signed applications from trusted publishers. Path restrictions can limit the execution of applications to those within specified folders, and network zones can restrict applications to only run from particular network zones.

Application allow lists and deny lists are key tools for securing systems by controlling which applications can execute, minimizing the risk of malware and unauthorized software.

---

See also:

- 