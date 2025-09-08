
# Key Derivation Function (KDF)

A Key Derivation Function (KDF) is a cryptographic algorithm used to generate one or more secret keys from an initial input, such as a password, passphrase, or master key. KDFs enhance the security of the derived keys by introducing additional computational complexity and randomness, making it harder for attackers to guess or brute-force the original input.

KDFs are commonly used in applications such as:

- **Password Hashing:** Transforming user passwords into secure, fixed-length representations for storage.
  <br>
- **Key Expansion:** Generating multiple cryptographic keys from a single master key in systems like TLS.
  <br>
- **Secure Key Generation:** Deriving keys for encryption, decryption, or authentication from a less secure input.

A secure KDF often incorporates techniques like salting (adding random data) and multiple iterations to resist attacks such as rainbow table and brute-force attacks. Examples of widely used KDFs include PBKDF2, bcrypt, Argon2, and HKDF.

---

See also:

- [[Key stretching]]
