
# Salting

[[🏷️Cryptography]] [[🏷️Password security]]

Salting is a cryptographic technique used to enhance the security of password storage. It involves adding a random string of characters, known as a "salt," to a password before hashing it. The salt ensures that even if two users have the same password, their stored password hashes will be different due to unique salts.

Salting prevents attackers from using precomputed hash databases, like rainbow tables, to quickly crack passwords. Since each password is combined with a different salt before hashing, the hash output becomes unique, significantly increasing the difficulty of reversing the hash.

For added security, salts should be generated using a strong random number generator and stored securely alongside the hashed passwords. Salting is widely used in secure systems, including web applications and databases, to protect user credentials.

---

See also:

- [[Hashing]]
- [[Key Derivation Function (KDF)]]
- [[Rainbow table]]