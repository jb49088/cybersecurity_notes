
# Rivest Cipher 4 (RC4)

[[🏷️Symmetric encryption algorithm]]

Rivest Cipher 4 (RC4) is a stream cipher designed by Ron Rivest in 1987. It gained widespread adoption due to its simplicity and speed, particularly in software implementations. RC4 encrypts data one byte at a time using a variable-length key, ranging from 40 to 256 bits.

RC4 operates using a key-scheduling algorithm (KSA) to initialize a permutation of all 256 possible byte values, followed by a pseudo-random generation algorithm (PRGA) to produce a keystream. The plaintext is XORed with this keystream to generate the ciphertext.

While RC4 was widely used in protocols like SSL/TLS and WEP, vulnerabilities in its key scheduling and bias in its keystream led to its deprecation in most secure systems.

---

See also:

- [[Stream cipher]]
- [[Symmetric encryption]]
- [[Rivest Cipher 5 (RC5)]]
- [[Rivest Cipher 6 (RC6)]]