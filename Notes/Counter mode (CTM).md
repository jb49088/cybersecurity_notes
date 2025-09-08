
# Counter mode (CTM)

Counter mode (CTM) is a mode of operation used in symmetric-key encryption algorithms, such as AES, to convert a block cipher into a stream cipher. In CTM, encryption is performed by generating a sequence of "counter" values, which are then encrypted and XORed with the plaintext to produce the ciphertext. This approach allows for parallelization and high performance, making it ideal for use in high-speed networks or systems requiring low latency.

In CTM, the "counter" is typically a nonce (a number used once) that is combined with a unique value for each block of data being encrypted. This ensures that the same key produces different ciphertexts each time it is used, providing strong security against replay attacks. Since the counter is incremented for each block of data, there is no need for feedback, which makes CTM highly efficient and parallelizable.

CTM is often used in protocols like TLS (Transport Layer Security) and IPsec to secure data during transmission. It is also employed in disk encryption and other data protection applications due to its speed and efficiency.

---

See also:

- [[Block cipher]]
- [[Stream cipher]]
- [[Nonce]]
- [[Galois counter mode (GCM)]]
- [[Symmetric encryption]]
- [[Advanced encryption standard (AES)]]