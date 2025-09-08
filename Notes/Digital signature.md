
# Digital signature

A digital signature is a cryptographic technique used to verify the authenticity and integrity of digital messages or documents. It functions similarly to a handwritten signature, providing assurance that a message or document has not been altered in transit and confirming the identity of the sender. Digital signatures use public-key cryptography to create a unique, verifiable signature that can be used to ensure non-repudiation in digital communication.

How it works:

1. **Hashing the Message**: The original message is passed through a cryptographic **hash function**, which produces a fixed-length string called the **hash value**. This hash is unique to the message; even a small change in the message results in a completely different hash.
2. **Encrypting the Hash**: The hash value is then **encrypted** with the sender's **private key**, creating the **digital signature**. This ensures that only the sender, who possesses the private key, can generate the signature.
3. **Verifying the Signature**: The recipient decrypts the digital signature using the sender’s **public key** to retrieve the original hash value. The recipient then hashes the received message and compares it with the decrypted hash. If they match, the message is verified as authentic and unchanged.

![[Image 2.78.png]]

![[Image 2.79.png]]

---

See also:

- [[Asymmetric encryption]]
- [[Hashing]]
- [[Authentication]]
- [[Integrity]]
- [[Non-repudiation]]
