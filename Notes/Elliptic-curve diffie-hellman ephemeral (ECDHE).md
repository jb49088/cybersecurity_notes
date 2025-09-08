
# Elliptic-curve diffie-hellman ephemeral (ECDHE)

[[🏷️Key exchange algorithm]]

Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) is a key exchange protocol that combines Elliptic Curve Diffie-Hellman (ECDH) with ephemeral key pairs to ensure secure, temporary session keys. This approach provides the benefits of elliptic curve cryptography (ECC), such as stronger security with smaller key sizes, alongside forward secrecy.

In ECDHE, both parties generate ephemeral public-private key pairs for each session. These keys are used to compute a shared secret that secures communication during that session. Once the session ends, the ephemeral keys are discarded, preventing the compromise of future or past sessions if private keys are exposed.

ECDHE is widely adopted in protocols like TLS for its performance efficiency and enhanced security, making it a popular choice for modern secure communications.

---

See also:

- [[Elliptic-curve cryptography (ECC)]]
- [[Diffie-Hellman (DH)]]
- [[Elliptic Curve Diffie-Hellman (ECDH)]]
- [[Perfect forward secrecy (PFS)]]
