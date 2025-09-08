
# Electronic codebook (ECB)

Electronic codebook (ECB) is a mode of operation for block ciphers in cryptography. It is the simplest and most widely used mode for encrypting data in fixed-size blocks. In ECB mode, the plaintext is divided into blocks of equal size, and each block is encrypted independently using the same encryption key.

- **Block-based encryption:** ECB works by breaking the plaintext into fixed-length blocks, typically 128 bits (16 bytes), and encrypting each block separately.
- **Simplicity and speed:** Due to its straightforward approach, ECB is fast and easy to implement, making it a popular choice in basic cryptographic applications.
- **Security weaknesses:** The primary drawback of ECB is that identical plaintext blocks will always produce identical ciphertext blocks. This makes it vulnerable to pattern recognition and attacks, as the structure of the plaintext can remain visible in the ciphertext.
- **Lack of diffusion:** Because each block is encrypted independently, ECB does not offer as much diffusion (spreading out plaintext information across the ciphertext) as other modes, making it less secure in certain applications.
- **Use cases:** While ECB is typically avoided for securing sensitive data due to its vulnerabilities, it may still be used in situations where security is not a primary concern, such as encrypting small amounts of data or in non-sensitive applications.

For stronger security, other encryption modes, like Cipher Block Chaining (CBC) or Galois/Counter Mode (GCM), are generally preferred over ECB.

---

See also:

- [[Block cipher]]
- [[Cipher block chaining (CBC)]]
- [[Galois counter mode (GCM)]]