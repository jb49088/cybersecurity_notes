
# Kerberos

[[🏷️Network protocol]]

Kerberos is a network authentication protocol designed to provide secure authentication for users and services within a distributed environment. It uses strong cryptography to ensure that data exchanged between clients and servers is secure, and that unauthorized users cannot access sensitive information.

- **Port number and protocol type:** Kerberos typically operates over port 88 using TCP or UDP.
- **Authentication process:** Kerberos uses a centralized authentication server known as the Key Distribution Center (KDC), which consists of two components: the Authentication Server (AS) and the Ticket Granting Server (TGS).
- **Tickets:** Instead of sending passwords over the network, Kerberos uses tickets to authenticate users. The user first obtains a Ticket Granting Ticket (TGT) from the AS, which is then used to request service tickets from the TGS to access specific services.
- **Encryption:** Kerberos relies on symmetric key cryptography, where both the client and the server share a secret key. This ensures that the communication between the client and server is encrypted and secure.
- **Time-sensitive:** Kerberos relies on synchronized clocks between the client, KDC, and server to prevent replay attacks and ensure the validity of tickets within a defined time window.

Kerberos is widely used in enterprise environments for secure network authentication, including integration with Microsoft Active Directory.

---

See also:

- [[Ticket granting ticket (TGT)]]
- [[Authentication, Authorization, and Accounting (AAA)]]
- [[Lightweight directory access protocol (LDAP)]]
- [[Remote authentication dial-in user service (RADIUS)]]
