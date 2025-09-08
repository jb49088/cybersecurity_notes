
# Initialization vector (IV)

An Initialization Vector (IV) is a random or pseudorandom value used in cryptographic algorithms to ensure that identical plaintexts produce different ciphertexts when encrypted. The IV adds an element of unpredictability to encryption processes, enhancing security by preventing attackers from recognizing patterns in encrypted data.

- **Encryption security:** The IV is combined with the encryption key to ensure that the same data encrypted multiple times will result in different ciphertexts, preventing attacks like ciphertext pattern analysis.
- **Usage in modes of operation:** The IV is essential in certain encryption modes, such as Cipher Block Chaining (CBC), where each block of plaintext is XORed with the previous ciphertext block before encryption. The first block uses the IV as its "previous block" value.
- **Randomness requirement:** IVs must be unique and random for each encryption session. Reusing an IV with the same key can lead to serious vulnerabilities, as it may allow attackers to deduce information about the plaintext.
- **Length and specification:** The length of the IV usually matches the block size of the encryption algorithm (e.g., 128 bits for AES). It is typically transmitted alongside the ciphertext for use during decryption.
- **Not a secret:** While the IV is used to enhance encryption security, it does not need to be kept secret. However, it must be protected from reuse with the same key to avoid compromising encryption strength.

The use of an IV is crucial for maintaining the confidentiality and integrity of encrypted data, especially in scenarios where data patterns are predictable or repeated.

---

See also:

- [[Cipher block chaining (CBC)]]
- [[Exclusive or (XOR)]]
- [[Advanced encryption standard (AES)]]