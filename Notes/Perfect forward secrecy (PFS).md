
# Perfect forward secrecy (PFS)

Perfect forward secrecy (PFS) is a cryptographic feature that ensures the security of encrypted communications by generating unique session keys for each exchange. Even if the server’s private key is compromised, past communications remain secure because the session keys cannot be retroactively decrypted.

Key aspects of PFS include:

- **Unique session keys:** Each session uses a distinct key generated through ephemeral key exchanges, typically using the Diffie-Hellman or Elliptic Curve Diffie-Hellman (ECDH) algorithms.
- **Protection from key compromise:** If the server's private key is exposed, attackers cannot decrypt previous sessions because the session keys are not derived from the server's private key.
- **Enhanced confidentiality:** PFS ensures long-term privacy by preventing attackers from accessing past communication data, even if they have recorded encrypted traffic and later obtain the server's private key.

Perfect forward secrecy is an essential feature for securing sensitive communications, and it is widely implemented in modern protocols like TLS (Transport Layer Security).

---

See also:

- [[Diffie-Hellman Ephemeral (DHE)]]
- [[Elliptic-curve diffie-hellman ephemeral (ECDHE)]]
- [[Transport Layer Security (TLS)]]
