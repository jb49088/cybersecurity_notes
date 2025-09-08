
# Diffie-Hellman Ephemeral (DHE)

[[🏷️Key exchange algorithm]]

Diffie-Hellman Ephemeral (DHE) is a key exchange protocol that provides secure, temporary session keys for encrypted communication. It is an extension of the classic Diffie-Hellman algorithm, incorporating ephemeral keys to ensure forward secrecy.

In DHE, both parties generate temporary (ephemeral) public-private key pairs for each session. These keys are used to derive a shared secret, which is then employed to encrypt the communication. Once the session ends, the ephemeral keys are discarded, preventing future compromises of private keys from exposing past communications.

DHE is widely used in secure protocols such as TLS to enhance the confidentiality of encrypted data. While it offers strong security, its performance is slower compared to some alternatives like Elliptic Curve Diffie-Hellman Ephemeral (ECDHE).

---

See also:

- [[Diffie-Hellman (DH)]]
- [[Elliptic Curve Diffie-Hellman (ECDH)]]
- [[Elliptic-curve diffie-hellman ephemeral (ECDHE)]]
- [[Perfect forward secrecy (PFS)]]