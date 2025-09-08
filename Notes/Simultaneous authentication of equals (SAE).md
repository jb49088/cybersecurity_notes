
# Simultaneous authentication of equals (SAE)

[[🏷️Key exchange protocol]]

Simultaneous authentication of equals (SAE) is a password-based authentication and key exchange protocol designed to provide secure communication in wireless networks. It is used to protect against offline brute force attacks and enables secure password-based authentication. SAE is commonly utilized in modern Wi-Fi networks as part of the WPA3 security standard.

SAE uses a Diffie-Hellman derived key exchange with an added authentication component, which ensures that both parties authenticate each other while establishing a shared session key. This process prevents attackers from gaining access to the session key even if they intercept the communication.

Key characteristics of SAE:

- **Diffie-Hellman key exchange**: SAE relies on the Diffie-Hellman method to securely exchange keys over an insecure channel.
- **Unique session keys**: Each party in the communication generates a unique session key, even if they share the same pre-shared key (PSK). This makes it more secure than older methods like WPA2, where the same PSK could lead to identical session keys.
- **Dragonfly handshake**: The SAE protocol uses a handshake known as the "Dragonfly" handshake. This handshake facilitates mutual authentication while creating a shared session key in a manner resistant to offline brute force attacks.

By ensuring unique session keys and utilizing a robust authentication process, SAE improves the security of wireless networks and mitigates the risks posed by common attacks.

---

See also:

- [[Wi-Fi Protected Access III (WPA3)]]
- [[Brute force attack]]
- [[Diffie-Hellman (DH)]]
- [[Pre-shared key (PSK)]]