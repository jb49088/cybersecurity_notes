
# Temporal key integrity protocol (TKIP)

[[🏷️Network protocol]]

Temporal key integrity protocol (TKIP) is a security protocol used in Wi-Fi networks to enhance encryption and protect data transmissions. It was introduced as part of the IEEE 802.11i standard to improve the security of the original Wired Equivalent Privacy (WEP) encryption, addressing its vulnerabilities while maintaining compatibility with older hardware.

TKIP was later replaced by more secure encryption protocols, such as AES in WPA2, due to emerging security weaknesses.

- **WEP enhancement:** Designed as an upgrade to WEP without requiring new hardware.
- **Dynamic key generation:** Generates a unique encryption key for each packet, reducing the risk of key reuse attacks.
- **Message integrity check (MIC):** Prevents packet tampering and forgery by verifying data integrity.
- **RC4-based encryption:** Uses the RC4 cipher with per-packet key mixing to strengthen security.
- **Superseded by WPA2:** Vulnerabilities in TKIP led to the adoption of AES-based encryption in WPA2 and WPA3.

Although TKIP was a significant improvement over WEP, it is now considered insecure and is no longer recommended for modern Wi-Fi networks.

---

See also:

- [[Wired Equivalent Privacy (WEP)]]
- [[Advanced encryption standard (AES)]]
- [[Wi-Fi Protected Access II (WPA2)]]
- [[Wi-Fi Protected Access III (WPA3)]]