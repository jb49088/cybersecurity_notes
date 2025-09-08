
# Time-based one-time password (TOTP)

Time-based one-time password (TOTP) is a security mechanism used for two-factor authentication (2FA) that generates a unique, temporary code based on the current time and a shared secret key. It enhances security by requiring users to enter a time-sensitive code in addition to their standard login credentials.

TOTP is widely used in authentication apps like Google Authenticator, Microsoft Authenticator, and Authy to protect online accounts from unauthorized access.

- **Time-dependent codes:** Generates a new code every 30 or 60 seconds, reducing the risk of replay attacks.
- **Based on a shared secret key:** Uses a secret key known to both the server and the authenticator app to generate the codes.
- **Algorithm-driven security:** Uses the HMAC-based one-time password (HOTP) algorithm with a time-based element.
- **Offline functionality:** Does not require an internet connection, as codes are generated locally on the user’s device.
- **Widespread adoption:** Used for securing online accounts, VPNs, and enterprise systems.

TOTP provides a strong layer of security, making it a common choice for multi-factor authentication (MFA) in modern applications.

---

See also:

- [[One-Time Password (OTP)]]
- [[HMAC-based one-time password (HOTP)]]