
# Galois counter mode (GCM)

Galois counter mode (GCM) is a mode of operation used in symmetric-key cryptography to provide both data confidentiality and integrity. GCM combines the CTM (Counter Mode) of encryption with the Galois Message Authentication Code (GMAC) to provide authenticated encryption. This mode is commonly used in protocols such as TLS (Transport Layer Security) and IPsec to secure communication over the internet.

In GCM, data is encrypted using CTM, which makes it fast and efficient. At the same time, it generates an authentication tag using GMAC, which ensures the integrity of the data by verifying that it has not been tampered with during transmission. This authentication tag helps detect any changes to the ciphertext, providing protection against replay attacks and other forms of data manipulation.

GCM is popular due to its high performance and strong security properties. It is designed to be parallelizable, meaning it can process data more quickly on modern processors, making it ideal for use in high-speed networks and environments that require low latency.

---

See also:

- [[Counter mode (CTM)]]
- [[Galois message authentication code (GMAC)]]
- [[Message Authentication Code (MAC)]]
- [[Advanced encryption standard (AES)]]
- [[Wi-Fi Protected Access III (WPA3)]]
- [[Transport Layer Security (TLS)]]
- [[Internet protocol security (IPsec)]]