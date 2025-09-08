
# Diameter

[[🏷️Network protocol]]

Diameter is an authentication, authorization, and accounting (AAA) protocol that serves as an advanced successor to RADIUS. It is designed for high-performance networks, offering improved security, scalability, and reliability for handling user access control in modern telecommunications and enterprise environments.

- **Port number and protocol type:** Diameter operates over port 3868 using TCP or SCTP (Stream Control Transmission Protocol) for reliable data transfer.
- **Authentication:** Diameter supports enhanced authentication mechanisms, including Extensible Authentication Protocol (EAP) and public key infrastructure (PKI)-based methods, providing stronger security than RADIUS.
- **Authorization:** After authentication, Diameter determines the level of access granted to a user, enforcing policies based on predefined rules.
- **Accounting:** Diameter provides detailed logging of user activities, such as session duration, bandwidth usage, and service consumption, aiding in billing and auditing.
- **Encryption and security:** Unlike RADIUS, Diameter requires TLS or IPsec for secure communications, ensuring data integrity and confidentiality.
- **Extensibility:** Diameter is highly extensible, allowing for custom applications and additional functionalities beyond traditional AAA services, making it suitable for next-generation networks (e.g., 5G and IMS architectures).

Diameter is widely used in telecommunications, mobile networks, and large enterprise environments that require robust authentication and accounting systems.

---

See also:

- [[Remote authentication dial-in user service (RADIUS)]]
- [[Authentication, Authorization, and Accounting (AAA)]]
- [[IEEE 802.1X]]
- [[Lightweight directory access protocol (LDAP)]]
- [[Terminal access controller access control system plus (TACACS+)]]