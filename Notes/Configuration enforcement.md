
# Configuration enforcement

Configuration enforcement ensures that devices comply with security policies before gaining full access to a network. This process is critical for maintaining a secure environment and preventing non-compliant devices from introducing vulnerabilities.

A posture assessment is performed each time a device connects to the network. This assessment includes an extensive check of the device’s operating system patch level, endpoint detection and response (EDR) version, the status of its firewall and EDR, and the validity of its security certificates. These checks ensure that the device adheres to the organization’s required configuration standards.

Devices found to be out of compliance are quarantined. Quarantined devices are placed in a private VLAN with restricted access, limiting their ability to interact with sensitive network resources. Once corrections are made, the device undergoes a recheck before being granted full access to the network.

Configuration enforcement is an essential security practice, helping to identify and remediate potential weaknesses while maintaining the integrity of the overall system.

---

See also:

- [[Endpoint detection and response (EDR)]]