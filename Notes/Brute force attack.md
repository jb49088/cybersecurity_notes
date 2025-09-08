
# Brute force attack

[[🏷️Password attack]]

A brute force attack involves systematically trying every possible password combination until the correct one is found. While this can be an effective method for breaking weak passwords, the process can be time-consuming, especially when strong hashing algorithms are used, which slow down the attack.

Brute force attacks can be categorized into two types:

- **Online brute force**: The attacker repeatedly attempts to log in to an account, entering different passwords until access is gained. This method is slow because most systems will lock accounts after a set number of failed login attempts, making it difficult to continue the attack.
- **Offline brute force**: The attacker gains access to a list of user credentials and password hashes, then attempts to calculate and compare the hashes to the stored ones. This method requires significant computational power but can be much faster than online attacks, as it doesn't rely on the login process and the associated lockout mechanisms.

To defend against brute force attacks, it’s important to use strong, complex passwords, enable account lockout after multiple failed attempts, and implement rate-limiting and multi-factor authentication (MFA).

---

See also:

- [[Password spraying]]
- [[Dictionary attack]]