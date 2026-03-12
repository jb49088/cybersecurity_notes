# Cipher-based Message Authentication Code (CMAC)

Cipher-based Message Authentication Code (CMAC) is a cryptographic technique used to ensure the integrity and authenticity of a message. CMAC is based on symmetric block ciphers, such as AES or DES, and is designed to generate a fixed-length tag from a message and a secret key.

CMAC works by dividing the message into blocks and encrypting each block sequentially, with the final block incorporating padding if necessary. The resulting tag, or MAC, is appended to the message and can be verified by the recipient using the same key.

CMAC is an improvement over older techniques like CBC-MAC, as it addresses vulnerabilities associated with variable-length messages. CMAC is widely used in secure communication protocols where symmetric encryption is employed.

---

See also:

- [[message_authentication_code_(mac)]]
- [[advanced_encryption_standard_(aes)]]
- [[data_encryption_standard_(des)]]
- [[block_cipher]]
- [[hash-based_message_authentication_code_(hmac)]]
