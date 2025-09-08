
# Challenge handshake authentication protocol (CHAP)

[[🏷️Network protocol]]

Challenge handshake authentication protocol (CHAP) is an authentication protocol used to verify the identity of a user or device in a secure manner during a network connection. It is commonly used in point-to-point protocol (PPP) connections, such as those used in dial-up or VPNs.

- **Three-way handshake:** CHAP uses a challenge-response mechanism to authenticate the user:
    - The server sends a randomly generated challenge to the client.
    - The client combines the challenge with a shared secret (like a password) and applies a cryptographic hash function to produce a response.
    - The server performs the same hash calculation using its stored shared secret and compares the result with the client’s response. Authentication is granted if the results match.
- **Periodic verification:** CHAP periodically reauthenticates the client during the session, ensuring that the connection remains secure and preventing session hijacking.
- **Encrypted credentials:** Only the hashed values are exchanged over the network, ensuring that the shared secret (password) is not transmitted in plain text.
- **Resistance to replay attacks:** The use of unique challenges for each handshake ensures that attackers cannot reuse intercepted responses to gain unauthorized access.

CHAP is more secure than simpler protocols like PAP (Password Authentication Protocol) because it does not send passwords in clear text. However, it has been largely replaced by stronger protocols like EAP (Extensible Authentication Protocol) in modern networks.

---

See also:

- [[Point-to-Point Protocol (PPP)]]
- [[Password authentication protocol (PAP)]]
- [[Extensible authentication protocol (EAP)]]