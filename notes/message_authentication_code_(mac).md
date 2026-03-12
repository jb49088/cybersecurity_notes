# Message Authentication Code (MAC)

A Message Authentication Code (MAC) is a cryptographic construct used to verify the integrity and authenticity of a message. It ensures that the message has not been tampered with and that it originates from a trusted sender.

MACs are generated using a secret key and the message itself. The resulting code is appended to the message and verified by the recipient using the same secret key. Unlike digital signatures, MACs rely on symmetric key cryptography, meaning both the sender and recipient share the same key.

There are different types of MACs, including:

- **Hash-based Message Authentication Code (HMAC):** Uses a cryptographic hash function like SHA-2 or SHA-3.
- **Cipher-based MAC (CMAC):** Uses block ciphers like AES.

MACs are widely used in secure communication protocols to protect data integrity and authenticity.

---

See also:

- [[hash-based_message_authentication_code_(hmac)]]
- [[cipher-based_message_authentication_code_(cmac)]]
- [[counter_mode_cbc-mac_protocol_(ccmp)]]
