# Misconfiguration

Misconfiguration is a vulnerability class that arises when systems, services, or applications are not set up securely, leaving them unnecessarily exposed due to oversight, poor practices, or a failure to apply security hardening. Unlike vulnerabilities that require complex exploitation, misconfigurations are often simple oversights that can be discovered and abused with minimal effort.

- **Default credentials:** Many devices, services, and applications ship with default usernames and passwords that administrators fail to change before deployment. Attackers commonly attempt these known defaults as an early step in gaining unauthorized access.
- **Unnecessary services and features:** Leaving unused services, ports, or application features enabled increases the attack surface. Features not required for normal operations should be disabled to limit exposure.
- **Improper access controls:** Overly permissive file system permissions, database access rights, or cloud storage policies can expose sensitive data or allow unauthorized users to perform privileged actions.
- **Verbose error handling:** Applications that return detailed error messages or stack traces in production environments leak information that aids attackers in understanding the system's internals and identifying further attack vectors.
- **Missing security headers:** Web applications that omit headers such as Content-Security-Policy, X-Frame-Options, or Strict-Transport-Security leave users exposed to attacks like clickjacking and cross-site scripting.
- **Unpatched software:** Running outdated software with known vulnerabilities is itself a form of misconfiguration, as failing to apply patches represents a deviation from secure operational practices.
- **Cloud misconfigurations:** Publicly accessible storage buckets, overly permissive IAM roles, and exposed management interfaces are among the most common and damaging misconfigurations in cloud environments.

Misconfiguration is consistently ranked among the most common vulnerability classes and is a reliable area of focus in bug bounty hunting, as it often yields findings across a wide range of targets with relatively straightforward discovery techniques.

---

See also:

- [[Default credentials]]
- [[Disclosure]]
- [[Attack surface]]
- [[Hardening]]
- [[Debug mode]]
