# Default credentials

Default credentials are the pre-configured usernames and passwords that manufacturers and developers ship with hardware devices, software applications, and services out of the box. They are intended as a convenience for initial setup but become a serious security risk when administrators fail to change them before deployment in a production environment.

- **Widespread prevalence:** Default credentials exist across a broad range of systems including routers, switches, firewalls, IP cameras, printers, database servers, content management systems, and web application admin panels, making them a consistent target during reconnaissance.
- **Publicly known values:** Default credentials are typically documented in product manuals, vendor websites, and aggregated databases such as DefaultCreds-cheat-sheet, meaning any attacker can look them up with minimal effort.
- **Discovery during enumeration:** In bug bounty hunting and penetration testing, identified services and login panels are routinely tested against known default credentials as an early and low-effort step before attempting more complex attacks.
- **Admin interface exposure:** Default credentials become significantly more dangerous when combined with publicly exposed admin interfaces or management panels, as successful authentication immediately grants elevated access to the underlying system.
- **IoT and embedded devices:** Internet of things devices are particularly notorious for default credential issues, as they are often deployed at scale with no credential change process and may lack the ability to enforce password changes on first login.
- **Credential databases:** Resources like DefaultCreds-cheat-sheet and Seclists maintain curated lists of known default credentials organized by vendor and product, which are commonly used alongside tools like Hydra or Burp Suite during testing.

Default credentials represent one of the most straightforward findings in security testing, requiring little technical sophistication to exploit while potentially granting significant access, making them an essential early check in any assessment or bug bounty engagement.

---

See also:

- [[Misconfiguration]]
- [[Credential stuffing]]
- [[Reconnaissance]]
- [[Brute force attack]]
- [[Wordlist]]
