
# Lightweight directory access protocol (LDAP)

[[🏷️Network protocol]]

Lightweight directory access protocol (LDAP) is an open protocol used to access and manage directory services over a network. It is commonly used for authentication, user management, and centralized access control in enterprise environments.

- **Port number and protocol type:** LDAP typically operates on port 389 for both TCP and UDP, while port 636 is used for TCP to provide secure communications via LDAPS.
- **Based on X.500:** LDAP is a simplified version of the X.500 directory services standard, which was originally designed for large-scale enterprise directory management. Unlike X.500, LDAP does not require OSI networking and operates over TCP/IP.
- **Directory structure:** LDAP organizes data hierarchically in a tree structure, known as the Directory Information Tree (DIT), which stores objects like users, groups, and devices.
- **Authentication and access control:** LDAP enables centralized authentication by allowing applications and services to validate user credentials against a directory service, such as Active Directory (AD) or OpenLDAP.
- **Search and query:** Clients can query directory services using Distinguished Names (DNs) and filters to retrieve user information, permissions, or other stored attributes.
- **Replication and scalability:** LDAP supports distributed directory services, enabling replication across multiple servers for improved performance and redundancy.

LDAP is widely used for managing user access in enterprise networks, supporting authentication mechanisms like Single Sign-On (SSO) and Multi-Factor Authentication (MFA).

---

See also:

- [[Lightweight directory access protocol secure (LDAPS)]]
- [[X.500]]
- [[Active directory (AD)]]
- [[Security assertion markup language (SAML)]]
- [[Remote authentication dial-in user service (RADIUS)]]
- [[Terminal access controller access control system plus (TACACS+)]]