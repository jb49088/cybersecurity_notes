
# Ticket granting ticket (TGT)

A ticket granting ticket (TGT) is a key component of the Kerberos authentication protocol, used to authenticate users securely without repeatedly requesting their credentials. When a user logs in, the authentication server (AS) issues a TGT, which serves as proof of authentication and allows the user to request access to various network services without needing to re-enter credentials.

TGTs are encrypted and time-limited, ensuring that authentication remains secure while reducing the risk of credential exposure.

- **Issued by the authentication server (AS):** Generated after the user successfully authenticates with Kerberos.
- **Used to request service tickets:** Allows users to obtain tickets for accessing specific network resources from the ticket granting server (TGS).
- **Time-limited validity:** Expires after a set period to enhance security and prevent misuse.
- **Encrypted for security:** Protects against tampering and unauthorized access.
- **Part of single sign-on (SSO):** Enables seamless authentication across multiple services without requiring repeated logins.

TGTs play a crucial role in Kerberos-based authentication, improving both security and user convenience in enterprise environments.

---

See also:

- [[Kerberos]]
- [[Single sign-on (SSO)]]


