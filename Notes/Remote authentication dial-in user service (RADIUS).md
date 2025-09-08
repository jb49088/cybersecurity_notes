
# Remote authentication dial-in user service (RADIUS)

[[🏷️Network protocol]]

Remote authentication dial-in user service (RADIUS) is a network protocol used for centralized authentication, authorization, and accounting (AAA) of users accessing a network. It is commonly used by internet service providers (ISPs), enterprises, and wireless networks to manage user authentication and access control.

- **Port number and protocol type:** RADIUS operates over UDP, using port 1812 for authentication and authorization and port 1813 for accounting. Some legacy implementations use ports 1645 and 1646 instead.
- **Authentication:** RADIUS verifies user credentials (such as usernames and passwords) against a centralized database before granting access to network resources.
- **Authorization:** After authentication, RADIUS enforces access policies, determining what resources a user can access and any session restrictions.
- **Accounting:** RADIUS tracks user activity, such as login times, session durations, and bandwidth usage, providing detailed logs for auditing and billing purposes.
- **Encryption:** RADIUS encrypts only the user’s password during transmission but leaves other information, such as usernames and accounting data, in plaintext. For enhanced security, it is often used with additional encryption protocols like IPsec or TLS.

RADIUS is widely used in enterprise environments for managing remote access, wireless authentication, and network security enforcement.



See also:

- [[AAA server]]
- [[Authentication, Authorization, and Accounting (AAA)]]
- [[IEEE 802.1X]]
- [[Lightweight directory access protocol (LDAP)]]
- [[Terminal access controller access control system plus (TACACS+)]]
