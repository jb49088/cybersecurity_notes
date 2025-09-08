
# Rainbow table

[[🏷️Password attack]]

A rainbow table is a precomputed table used to reverse cryptographic hash functions, primarily for the purpose of cracking password hashes. Instead of computing the hash of each possible password during the attack, a rainbow table contains a list of hashed values for common passwords, making the process of cracking faster.

Rainbow tables use a reduction function that maps a hash back to a possible password, which is then hashed again. This process is repeated to create a chain of hashed values and corresponding plaintext values. The table can be used to quickly look up a hash and find its corresponding password without having to compute every possible combination.

To defend against rainbow table attacks, it's essential to use **salt** — random data added to the password before hashing, which makes each hash unique even for identical passwords. Additionally, using strong hashing algorithms like bcrypt or Argon2, which are computationally intensive, makes the use of rainbow tables impractical.

---

See also:

- [[Hashing]]
- [[Brute force attack]]
- [[Dictionary attack]]

