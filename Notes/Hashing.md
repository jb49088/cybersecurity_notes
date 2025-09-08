
# Hashing

[[🏷️Cryptography]] [[🏷️Password security]]

Hashing is a process that transforms input data (such as a file, password, or message) into a fixed-length string of characters, known as a hash value or hash code. The output is typically a sequence that appears random but is consistently derived from the input data. Hashing is deterministic, meaning the same input will always produce the same output. It also generates a fixed-length result regardless of the input size, and it is a one-way process, making it computationally infeasible to reverse the hash and retrieve the original data.

## Common uses of hashing

- **Data Integrity**: Hash functions are commonly used to verify the integrity of data. When files or data are transmitted over a network, a hash is computed at the source and sent with the data. The recipient computes the hash of the received data and compares it with the sent hash to ensure no changes were made during transmission.
- **Password Storage**: Hashing is widely used to store passwords securely. Instead of storing the actual password, a system stores the hash value. When a user logs in, the system hashes the entered password and compares it with the stored hash.
- **Digital Signatures**: Hashing is essential for creating digital signatures. A hash of a message is signed using a private key, providing both integrity and authenticity to the message.
- **Cryptographic Applications**: Hashing forms the basis of various cryptographic protocols, like HMAC (Hash-based Message Authentication Code) and blockchain technology.

Hash functions like SHA-256, SHA-3, and BLAKE2 are considered secure and widely used, while older algorithms like MD5 and SHA-1 are now deemed insecure due to vulnerabilities, such as hash collisions.

---

See also:

- [[Integrity]]
- [[Digital signature]]
- [[Checksum]]
- [[Salting]]

