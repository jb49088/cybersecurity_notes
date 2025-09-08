
# Key exchange

Key exchange is a method used to securely share encryption keys between parties, allowing them to communicate securely. It typically involves two approaches:

- **Out-of-Band:** Keys are exchanged using a separate, secure channel outside the communication network, reducing the risk of interception.
- **In-Band:** Keys are exchanged within the communication channel, often using public-key cryptography to securely send a symmetric key.

Key exchange often uses asymmetric encryption to exchange a symmetric key. The public key encrypts the symmetric key, and the recipient uses their private key to decrypt it. This allows both parties to use the symmetric key for faster encryption and decryption of data.

A session key is a temporary symmetric key generated for a specific communication session. Once the session ends, the session key is discarded, providing extra security for future communications.

Algorithms like Diffie-Hellman and Elliptic Curve Diffie-Hellman (ECDH) enable two parties to derive a shared symmetric key without directly transmitting it. These methods ensure that key material is never exposed, even during the exchange.

![[Image 3.30.png]]

---

See also:

- [[Asymmetric encryption]]
- [[Symmetric encryption]]
- [[Diffie-Hellman (DH)]]
- [[Elliptic Curve Diffie-Hellman (ECDH)]]
- [[Public key Infrastructure (PKI)]]
- [[Session key]]