
# Password-based key derivation function 2 (PBKDF2)

[[🏷️Key derivation function]]

Password-based key derivation function 2 (PBKDF2) is a cryptographic algorithm used to strengthen passwords by generating a secure key from a user-provided password and a salt. It is widely used in password hashing and encryption to make brute-force and dictionary attacks more difficult.

- **Key stretching:** PBKDF2 applies a hash function (such as SHA-256) multiple times to slow down brute-force attacks.
- **Salt usage:** A unique, random salt is added to each password to prevent **rainbow table** attacks.
- **Configurable iterations:** The number of hashing iterations can be increased to adapt to modern computing power, enhancing security.
- **Use cases:** PBKDF2 is commonly used in **password storage**, **disk encryption**, **Wi-Fi security (WPA2 and WPA3),** and **secure key derivation.**
- **Security considerations:** While PBKDF2 is still widely used, newer algorithms like **bcrypt** and **Argon2** offer better resistance against GPU and ASIC-based attacks.

PBKDF2 remains a strong choice for password hashing and encryption when implemented with a high number of iterations and a strong hash function.

---

See also:

- [[Key Derivation Function (KDF)]]
- [[bcrypt]]
