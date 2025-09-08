
# Hash-based Message Authentication Code (HMAC)

Hash-based Message Authentication Code (HMAC) is a cryptographic method that ensures data integrity and authenticity. HMAC combines a cryptographic hash function (such as SHA-256 or SHA-3) with a secret key to produce a fixed-length output, called the MAC (Message Authentication Code).

HMAC is widely used in secure communication protocols, including TLS, IPSec, and HTTPS. Its key features include resistance to tampering and the ability to verify that data has not been altered during transmission.

The HMAC process involves hashing the input data and key in a specific sequence to achieve a high level of security. It is particularly resistant to length extension attacks, making it more secure than traditional hashing for authentication purposes.

---

See also:

- [[Message Authentication Code (MAC)]]
- [[Cipher-based Message Authentication Code (CMAC)]]
- [[Secure Hash Algorithm 2 (SHA-2)]]
- [[Secure Hash Algorithm 3 (SHA-3)]]
- [[Hypertext transfer protocol secure (HTTPS)]]