
# Session key

A session key is a temporary encryption key used to secure a single communication session between two parties. This symmetric key encrypts and decrypts all messages exchanged during the session, ensuring confidentiality and integrity. Once the session ends, the session key is discarded, minimizing the risk of long-term key compromise.

Session keys are typically generated randomly to ensure unpredictability and are exchanged securely using mechanisms such as public-key cryptography or key exchange protocols like Diffie-Hellman or Elliptic Curve Diffie-Hellman (ECDH). These methods prevent unauthorized interception of the key during transmission. The temporary nature of session keys ensures that even if a key is compromised, it only affects a single session, while their use in symmetric encryption improves computational efficiency for encrypting large amounts of data.

---

See also:

- [[Symmetric encryption]]
- [[Asymmetric encryption]]
- [[Rivest shamir adleman (RSA)]]
- [[Key exchange]]
- [[Transport Layer Security (TLS)]]
- [[Diffie-Hellman (DH)]]
- [[Elliptic Curve Diffie-Hellman (ECDH)]]