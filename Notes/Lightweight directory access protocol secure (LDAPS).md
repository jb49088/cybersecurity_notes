
# Lightweight directory access protocol secure (LDAPS)

[[🏷️Network protocol]]

Lightweight directory access protocol secure (LDAPS) is a protocol used for accessing and managing directory services over a secure connection. It is a secure version of the standard Lightweight Directory Access Protocol (LDAP), which is used to query and modify directory services, such as those storing user information, email addresses, and other network resources.

- **Port number and protocol type:** LDAPS operates over port 636 using TCP (Transmission Control Protocol) for reliable data transfer.
- **Encryption:** LDAPS uses SSL/TLS encryption to secure communication between clients and directory servers, ensuring that sensitive data, such as passwords and user information, is transmitted securely.
- **Authentication:** LDAPS supports various authentication methods to verify the identity of users and servers, helping to prevent unauthorized access to directory information.
- **Request/response model:** LDAPS operates with a request-response model, where a client sends a query or request for directory information, and the server responds with the requested data or an error message.
- **LDAP vs. LDAPS:** While LDAP can be used without encryption, LDAPS ensures that the communication channel is encrypted, providing an extra layer of security for directory services.

LDAPS is essential for protecting sensitive directory information and maintaining the privacy and integrity of data when accessing directory services over a network.

---

See also:

- [[Lightweight directory access protocol (LDAP)]]
- [[X.500]]
- [[Active directory (AD)]]
- [[Security assertion markup language (SAML)]]
- [[Remote authentication dial-in user service (RADIUS)]]
- [[Terminal access controller access control system plus (TACACS+)]]