
# Asymmetric encryption

Asymmetric encryption, also known as public-key cryptography, is a method of encryption that uses a pair of keys to secure data. Unlike symmetric encryption, which uses the same key for both encryption and decryption, asymmetric encryption relies on two distinct keys: a public key and a private key.

- **Public Key**: This key is shared openly with anyone who wants to send encrypted data to the recipient. It is used to encrypt the data, but it cannot be used to decrypt it.
- **Private Key**: The private key is kept secret and only known to the recipient. It is used to decrypt the data that was encrypted with the corresponding public key.

Asymmetric encryption is commonly used for one-time exchanges, such as establishing a secure connection or key exchange during a handshake. After this, symmetric encryption is typically employed for ongoing communication since it is faster and better suited for encrypting large amounts of data.

![[Image 2.81.png]]

---

See also:

- [[Symmetric encryption]]
- [[Digital signature]]
- [[Public key Infrastructure (PKI)]]
- [[Secure sockets layer (SSL)]]
- [[Transport Layer Security (TLS)]]
