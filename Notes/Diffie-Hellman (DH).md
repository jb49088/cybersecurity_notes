
# Diffie-Hellman (DH) 

[[🏷️Key exchange algorithm]]

Diffie-Hellman is a cryptographic protocol used to securely exchange cryptographic keys over an untrusted communication channel. Unlike traditional encryption algorithms, Diffie-Hellman allows two parties to establish a shared secret key without directly transmitting it, thus ensuring confidentiality.

The protocol relies on the difficulty of solving discrete logarithm problems in modular arithmetic. Each party generates a private key and a public key, then exchanges their public keys. Using their own private key and the other party's public key, both parties can compute the same shared secret, which can then be used for symmetric encryption.

While Diffie-Hellman itself does not provide encryption or authentication, it is widely used in establishing secure communications in protocols like SSL/TLS and VPNs.

---

See also:

- [[Diffie-Hellman Ephemeral (DHE)]]
- [[Elliptic-curve diffie-hellman ephemeral (ECDHE)]]
