
# Elliptic Curve Diffie-Hellman (ECDH)

[[🏷️Key exchange algorithm]]

Elliptic Curve Diffie-Hellman (ECDH) is a cryptographic key exchange protocol that combines the Diffie-Hellman algorithm with elliptic curve cryptography (ECC). It allows two parties to securely establish a shared secret over an insecure channel, which can then be used for encryption or authentication.

ECDH uses the mathematical properties of elliptic curves to provide equivalent security with shorter key lengths compared to traditional Diffie-Hellman. For instance, a 256-bit ECDH key provides security comparable to a 3,072-bit traditional Diffie-Hellman key.

The efficiency and strength of ECDH make it widely used in modern secure communication protocols like TLS, especially in scenarios where performance and low resource usage are critical.

---

See also:

- [[Diffie-Hellman (DH)]]
- [[Elliptic-curve cryptography (ECC)]]