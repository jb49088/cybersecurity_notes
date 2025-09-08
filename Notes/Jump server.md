
# Jump server

[[🏷️Networking]] [[🏷️Network security]]

A jump server is a secure server that acts as a gateway or intermediary to access a restricted network or systems. It is commonly used in environments where direct access to sensitive or critical systems must be controlled or monitored.

Jump servers are often employed to access systems in a secure network (such as a private data center or cloud environment) from an external or less-secure network. The idea is to reduce the attack surface by providing a single, controlled point of entry for administrative or authorized users.

Jump servers generally provide the following features:

- **Authentication**: Strong authentication methods, such as multi-factor authentication (MFA), are often required to access the jump server.
- **Monitoring**: Activity on the jump server can be logged and monitored, allowing for auditing of administrative actions.
- **Segmentation**: The jump server can be isolated in a demilitarized zone (DMZ) or other segmented network areas, enhancing security by limiting direct access to critical systems.

Jump servers are crucial for maintaining secure access control, especially when working with systems that need to be protected from unauthorized or unmonitored access.

---

See also:

- [[Network segmentation]]
- [[Demilitarized zone (DMZ)]]
- [[Virtual private network (VPN)]]
- [[Secure shell (SSH)]]
- [[Remote desktop protocol (RDP)]]

