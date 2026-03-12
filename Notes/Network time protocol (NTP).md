# Network time protocol (NTP)

[[🏷️Network protocol]]

Network time protocol (NTP) is one of the oldest internet protocols still in widespread use, designed to synchronize the clocks of computers and network devices to a common time reference. Accurate timekeeping is a fundamental dependency for a surprising number of critical systems and security mechanisms, making NTP a quiet but essential part of network infrastructure.

- **How it works:** NTP operates in a hierarchical structure of time sources called strata. Stratum 0 devices are highly precise reference clocks such as atomic clocks or GPS receivers. Stratum 1 servers synchronize directly to stratum 0 devices, stratum 2 servers synchronize to stratum 1, and so on. Each level of the hierarchy introduces a small amount of additional latency and potential drift.
- **Port and protocol:** NTP operates over UDP port 123 and is designed to function efficiently over unreliable networks, accounting for variable network latency when calculating accurate time offsets.
- **Security dependency:** Many security mechanisms depend heavily on accurate time synchronization. Kerberos authentication, which is central to Active Directory environments, requires clocks to be within five minutes of each other or authentication will fail entirely. TLS certificate validation, log correlation, and multi-factor authentication token generation are similarly time dependent.
- **NTP attacks:** Because time synchronization underpins so many security controls, NTP can be an attractive attack target. NTP amplification is a well known distributed denial of service technique where attackers send small spoofed requests to NTP servers that respond with significantly larger replies, amplifying traffic toward a victim. Clock skew attacks attempt to manipulate a target's time perception to invalidate certificates or disrupt authentication.
- **NTPsec and authentication:** Traditional NTP has limited built-in authentication, making it vulnerable to man-in-the-middle attacks that feed a target false time data. NTPsec and symmetric key authentication extensions address some of these weaknesses, though deployment is inconsistent across environments.
- **Logging and forensics:** Accurate NTP synchronization is critical in forensic investigations and incident response, as log correlation across multiple systems depends on consistent timestamps. Devices with drifted clocks can produce logs that are difficult or impossible to correlate accurately, complicating timeline reconstruction.

NTP is a foundational protocol that operates largely invisibly until something goes wrong, at which point its absence or compromise can cascade into authentication failures, logging gaps, and security control bypasses that are difficult to diagnose without understanding its role in the broader infrastructure.

---

See also:

- [[User datagram protocol (UDP)]]
- [[Kerberos]]
- [[Active directory (AD)]]
- [[Amplification attack]]
- [[Incident response plan (IRP)]]
