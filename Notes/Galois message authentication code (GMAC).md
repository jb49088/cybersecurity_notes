
# Galois message authentication code (GMAC)

Galois message authentication code (GMAC) is a cryptographic algorithm used to verify the integrity and authenticity of data. GMAC is based on the Galois field, which is a mathematical structure used in many cryptographic protocols. It provides a method for generating a message authentication tag that ensures the data has not been tampered with during transmission.

GMAC is commonly used in conjunction with other encryption methods, such as Galois counter mode (GCM), to provide authenticated encryption. In this context, GMAC acts as the authentication component, ensuring that the ciphertext has not been altered. It is designed to be fast and efficient, particularly when implemented in hardware or parallelized environments.

One of the key advantages of GMAC is its ability to perform message authentication on large data streams without compromising security. It is widely used in network protocols, including TLS and IPsec, to secure communication and prevent data integrity issues.

---

See also:

- [[Galois counter mode (GCM)]]
- [[Message Authentication Code (MAC)]]
- [[Advanced encryption standard (AES)]]