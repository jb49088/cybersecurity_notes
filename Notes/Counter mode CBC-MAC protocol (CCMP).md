
# Counter mode CBC-MAC protocol (CCMP)

Counter mode with cipher block chaining message authentication code protocol (CCMP) is a security protocol used in wireless networks to provide encryption, authentication, and message integrity. It is a key component of WPA2 (Wi-Fi Protected Access 2) and WPA3, ensuring secure communication over Wi-Fi by addressing vulnerabilities in older protocols like WEP.

- **Encryption:** CCMP uses the AES (Advanced Encryption Standard) algorithm in Counter Mode for data confidentiality, ensuring that transmitted data is securely encrypted.
- **Authentication and integrity:** It employs Cipher Block Chaining Message Authentication Code (CBC-MAC) to verify the authenticity of messages and ensure data integrity, preventing tampering or forgery.
- **Initialization vector (IV):** CCMP incorporates a 48-bit IV to enhance security and prevent replay attacks by ensuring that encryption keys are not reused for the same data.
- **Key management:** Operates as part of WPA2/3, relying on the 4-way handshake for secure key exchange and management between devices.
- **Performance:** Designed to provide robust security without significantly impacting network performance.

CCMP replaced the flawed TKIP (Temporal Key Integrity Protocol) in WPA and is considered a reliable and secure protocol for modern wireless networks. It is widely used to protect sensitive data and ensure trust in Wi-Fi communications.

---

See also:

- [[Wi-Fi Protected Access II (WPA2)]]
- [[Wi-Fi Protected Access III (WPA3)]]
- [[Counter mode (CTM)]]
- [[Cipher block chaining (CBC)]]
- [[Message Authentication Code (MAC)]]