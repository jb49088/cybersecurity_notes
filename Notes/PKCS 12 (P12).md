
# PKCS 12 (P12)

PKCS 12 (Public-Key Cryptography Standards #12), commonly referred to as P12, is a binary file format used to store cryptographic objects, including private keys, public key certificates, and certificate chains in a single, secure container. It is widely used for securely exchanging cryptographic credentials between systems.

- **Secure storage:** Protects private keys with password-based encryption to prevent unauthorized access.
- **Interoperability:** Supported by various cryptographic tools and systems, including OpenSSL, Windows Certificate Store, and Java KeyStore (JKS).
- **Common use cases:** Used for TLS/SSL certificates, code signing, and email encryption to securely store and transport credentials.
- **File extension:** Typically uses `.p12` or `.pfx` file extensions, with `.pfx` being more commonly associated with Windows environments.
- **Encryption standards:** Supports strong encryption algorithms such as AES and Triple DES to enhance security.

PKCS 12 is a crucial format for managing and distributing cryptographic keys securely, ensuring authentication and encryption integrity across various applications.

---

See also:

- [[Public key Infrastructure (PKI)]]
- [[Digital certificate]]
- [[X.509]]