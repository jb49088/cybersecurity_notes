
# Cipher block chaining (CBC)

Cipher block chaining (CBC) is a mode of operation for block ciphers that provides enhanced security by chaining together encrypted blocks of data. CBC is widely used in symmetric key encryption algorithms, such as advanced encryption standard (AES), to ensure that identical plaintext blocks are encrypted into different ciphertext blocks, even if they appear multiple times in the data stream.

In CBC mode, the encryption process works as follows:

1. Initialization Vector (IV): A random IV is generated and used to modify the first block of plaintext before encryption. The IV is typically transmitted along with the ciphertext but does not need to be kept secret.
2. XOR Operation: The plaintext is divided into fixed-size blocks. Each plaintext block is XORed (exclusive OR) with the previous ciphertext block (or IV for the first block) before being encrypted.
3. Chaining: The resulting ciphertext block is used as input for the next block of plaintext. This chaining process ensures that identical blocks of plaintext produce different ciphertexts, enhancing security by preventing patterns from emerging in the encrypted data.

While CBC is a secure encryption method, it does have some limitations, including the need for proper IV management and vulnerability to certain types of attacks, such as padding oracle attacks, if not implemented correctly.

---

See also:

- [[Block cipher]]
- [[Advanced encryption standard (AES)]]



