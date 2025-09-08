
# Password authentication protocol (PAP)

[[🏷️Network protocol]]

Password authentication protocol (PAP) is a simple authentication method used to verify users by transmitting usernames and passwords over a network. It is commonly used in older network protocols and remote access services but is considered insecure due to its lack of encryption.

- **Plaintext transmission:** PAP sends credentials in cleartext, making it vulnerable to interception by attackers using packet sniffing techniques.
- **Two-way handshake:** The authentication process consists of a simple exchange where the client sends the username and password, and the server verifies the credentials before granting access.
- **Weak security:** Because PAP does not offer encryption or challenge-response mechanisms, it is susceptible to **man-in-the-middle (MITM) attacks** and credential theft.
- **Replacement by stronger protocols:** More secure authentication protocols, such as **Challenge Handshake Authentication Protocol (CHAP)** and **Extensible Authentication Protocol (EAP),** have largely replaced PAP in modern systems.
- **Legacy use:** PAP may still be found in older systems, simple network setups, or applications where encryption is handled at another layer.

Due to its security weaknesses, PAP is generally discouraged for use unless combined with additional encryption mechanisms like **Transport Layer Security (TLS).**

---

See also:

- [[Challenge Handshake Authentication Protocol (CHAP)]]
- [[Extensible authentication protocol (EAP)]]