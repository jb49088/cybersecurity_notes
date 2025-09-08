
# Cryptographic Key

A cryptographic key is a string of data used in conjunction with a cryptographic algorithm to encrypt or decrypt information. Keys are fundamental to the operation of encryption and decryption processes, ensuring that only authorized parties can access or modify data.

There are two primary types of cryptographic keys:

- **Symmetric Keys:** The same key is used for both encryption and decryption. Both the sender and recipient must securely share this key beforehand. Common symmetric key algorithms include AES and DES.
  <br>
- **Asymmetric Keys:** This involves a pair of keys—one public and one private. The public key encrypts data, while the private key is used for decryption. Only the recipient, who holds the private key, can decrypt messages encrypted with their public key. RSA and ECC are examples of asymmetric key systems.

The security of a cryptographic system depends on the strength and secrecy of the keys. In most systems, key management, including generation, distribution, and storage, is critical to ensuring the overall security of the cryptographic process.

---

See also:

- [[Public key Infrastructure (PKI)]]
- [[Encryption]]
- [[Symmetric encryption]]
- [[Asymmetric encryption]]
- [[Advanced encryption standard (AES)]]
- [[Data encryption standard (DES)]]
- [[Rivest shamir adleman (RSA)]]
- [[Elliptic-curve cryptography (ECC)]]