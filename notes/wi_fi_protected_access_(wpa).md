# Wi-Fi Protected Access (WPA)

WPA, or Wi-Fi Protected Access, is a security protocol designed to secure wireless networks. The first version, known as WPA, was introduced in 2003 as a response to vulnerabilities found in the earlier [[30-39_educational/33_networking_&_the_cloud/33.10_■_network_protocols/33.17_security_protocols/wired_equivalent_privacy_(wep)|wep_(wired_equivalent_privacy)]] standard.

**Key Features of WPA:**

1. **TKIP (Temporal Key Integrity Protocol):** WPA implemented TKIP to enhance security by using per-packet keys, which made it much harder for attackers to decipher encrypted data.
   <br>
2. **Authentication:** WPA introduced a more secure method of user authentication, allowing for both pre-shared keys (PSK) for home networks and the [[ieee_802.11_(wi-fi)|ieee_802.1x]] standard for enterprise environments.
   <br>
3. **Improved Encryption:** WPA uses the RC4 stream cipher along with TKIP, improving upon the static key approach used in WEP.
   <br>
4. **Message Integrity Check:** WPA includes a mechanism to ensure that messages sent over the network have not been altered, further protecting data integrity.

WPA marked a significant improvement over WEP, but it was later succeeded by [[wi-fi_protected_access_ii_(wpa2)|wpa2]], which introduced even stronger security features, including the use of AES (Advanced Encryption Standard). WPA has since been phased out in favor of WPA2 and [[wi-fi_protected_access_iii_(wpa3)|wpa3]], which offer enhanced security measures.

---

See also:

- [[wi-fi_protected_access_ii_(wpa2)]]
- [[wi-fi_protected_access_iii_(wpa3)]]
