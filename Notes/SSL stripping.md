
# SSL stripping

[[🏷️Cryptographic attack]]

SSL stripping is an attack that downgrades a secure HTTPS connection to an unencrypted HTTP connection, allowing the attacker to intercept and manipulate sensitive data. The attacker accomplishes this by intercepting the initial connection between the user and the server, presenting an unencrypted version of the site while relaying the data to the legitimate server over HTTPS. As a result, the user unknowingly sends and receives data in plaintext, making it vulnerable to eavesdropping and tampering.

This attack typically happens when a user attempts to visit a site via HTTPS, but the attacker strips away the SSL/TLS encryption, leaving the connection unsecured. SSL stripping is effective in environments where the client does not properly check for SSL/TLS encryption or where weak or outdated security protocols are in use.

![[Image 3.47.png]]

To mitigate SSL stripping, websites should implement HTTP Strict Transport Security (HSTS), which forces browsers to connect using HTTPS and prevents fallback to HTTP. Additionally, using strong SSL/TLS configurations and educating users to always verify HTTPS connections can help reduce the risk.

---

See also:

- [[Hypertext transfer protocol secure (HTTPS)]]
- [[Hypertext transfer protocol (HTTP)]]
- [[Secure sockets layer (SSL)]]
- [[Transport Layer Security (TLS)]]
- [[On-path attack]]