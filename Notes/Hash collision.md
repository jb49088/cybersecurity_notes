
# Hash collision

[[🏷️Cryptography]]

A hash collision occurs when two different inputs produce the same hash output. In other words, it is when two distinct sets of data (e.g., files, passwords, or messages) yield the same hash value after being processed by a hash function. Hash collisions are a significant concern in cryptography and data integrity because they undermine the uniqueness and reliability of a hash function.

## Impact of hash collisions

- **Data Integrity**: Hash functions are used to verify the integrity of data. A collision could mean that different pieces of data have the same hash value, leading to misidentification or failure to detect unauthorized changes.
- **Cryptographic Security**: Many security protocols (such as digital signatures, file verification, and password hashing) rely on hash functions for authenticity and integrity. A collision could allow an attacker to substitute malicious data with legitimate-looking data, undermining trust in the system.
- **Vulnerabilities in Algorithms**: Older or weaker hash algorithms (like MD5 and SHA-1) are more prone to collisions and are considered insecure for many applications today. Cryptographers aim to use stronger, collision-resistant hash functions such as SHA-256 to reduce these risks.

A hash collision demonstrates the limits of hash functions and the importance of using secure, modern algorithms to ensure the integrity and authenticity of data in cryptographic systems.

---

See also:

- [[Hashing]]
- [[Secure Hash Algorithm 1 (SHA-1)]]
- [[Message Digest 5 (MD5)]]
