
# Birthday attack

[[🏷️Cryptographic attack]]

A birthday attack is a type of cryptographic attack that exploits the mathematics of the birthday paradox to find collisions in hash functions. In cryptographic terms, a collision occurs when two different inputs produce the same hash value.

The birthday paradox reveals that the probability of two randomly chosen items sharing a common attribute (e.g., the same birthday) is higher than intuitively expected. Similarly, in hash functions, finding two distinct inputs that hash to the same output can require significantly fewer attempts than one might expect.

For a hash function that produces an output of a certain length (for example, a 128-bit hash), a birthday attack could find a collision with only around half the number of possible outputs. This principle shows why shorter hash lengths are more vulnerable to such attacks, emphasizing the need to use hash functions with larger output sizes (e.g., 256 bits or more) to ensure security.

---

See also:

- [[Hash collision]]
- [[Collision attack]]
