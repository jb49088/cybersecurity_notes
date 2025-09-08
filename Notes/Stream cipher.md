
# Stream cipher

A stream cipher is a symmetric encryption method that encrypts data one bit or byte at a time. Instead of processing fixed-size blocks like block ciphers, stream ciphers generate a continuous keystream that is XORed with the plaintext to produce ciphertext.

Stream ciphers are designed for simplicity and speed, making them suitable for real-time applications like video streaming and secure communications. Examples of stream ciphers include RC4 and ChaCha20.

While stream ciphers can be efficient, they are highly sensitive to key reuse and require strong randomness in their keystream generation to maintain security.

---

See also:

- [[Block cipher]]
- [[Symmetric encryption]]
- [[Rivest Cipher 4 (RC4)]]