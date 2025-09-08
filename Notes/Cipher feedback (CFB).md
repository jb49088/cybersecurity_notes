
# Cipher feedback (CFB)

[[🏷️Cryptography]]

Cipher feedback (CFB) is a block cipher mode of operation that transforms a block cipher into a self-synchronizing stream cipher. It enables encryption and decryption of data in smaller segments, making it suitable for applications requiring real-time or incremental data processing.

- **Mode of operation:** CFB works by feeding the ciphertext from the previous encryption step back into the encryption process as input for the next block. This creates a chain-like dependency between blocks.
- **Self-synchronization:** CFB automatically resynchronizes if data is lost or out of order, as long as the receiver receives enough subsequent ciphertext to recover the stream.
- **Initialization vector (IV):** An IV is used to initialize the encryption process, ensuring that identical plaintext blocks result in different ciphertexts, preventing patterns.
- **No padding required:** Unlike other block cipher modes, CFB does not require padding because it can process plaintext in arbitrary segment sizes smaller than the block size.
- **Applications:** CFB is commonly used in scenarios such as secure communication protocols and streaming data encryption where data arrives in smaller chunks.

While Cipher Feedback mode provides flexibility and incremental encryption, it may have slower performance compared to other modes, such as counter mode (CTM), due to its feedback-based structure.

---

See also:

- [[Block cipher]]
- [[Stream cipher]]
- [[Initialization vector (IV)]]
- [[Counter mode (CTM)]]
- [[Cipher block chaining (CBC)]]