
# Terminal access controller access control system plus (TACACS+)

[[🏷️Network protocol]]

Terminal access controller access control system plus (TACACS+) is an authentication, authorization, and accounting (AAA) protocol used to manage network access. It is designed to provide centralized control over access to network devices such as routers, switches, and firewalls.

- **Port number:** TACACS+ typically operates over port 49.
- **Protocol type:** TACACS+ uses TCP (Transmission Control Protocol) to ensure reliable and secure communication between clients and servers.
- **Authentication:** TACACS+ separates the authentication, authorization, and accounting processes, allowing for flexible and granular control over network access. It supports username and password-based authentication, and can integrate with external systems such as RADIUS or LDAP.
- **Encryption:** Unlike RADIUS, TACACS+ encrypts the entire payload of the communication, providing stronger security for sensitive data.
- **Authorization:** TACACS+ allows for fine-grained control over which commands a user can execute on network devices after they are authenticated.
- **Accounting:** TACACS+ supports logging of user activity for auditing and reporting purposes. This helps track which users accessed devices and what commands they executed.

TACACS+ is commonly used in large enterprise environments to ensure secure and controlled access to network devices.

---

See also:

- [[Authentication, Authorization, and Accounting (AAA)]]
- [[Remote authentication dial-in user service (RADIUS)]]
- [[Lightweight directory access protocol (LDAP)]]