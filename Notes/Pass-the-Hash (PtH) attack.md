
# Pass-the-Hash (PtH) attack

[[🏷️Password attack]]

A Pass-the-Hash (PtH) attack allows attackers to authenticate as a user without knowing their plaintext password. Instead, they use the hashed representation of the password obtained from compromised systems. These credentials can be gained through various methods, including on-path attacks, where the attacker intercepts network traffic containing hashed credentials.

Once the hash is captured, the attacker can use it to authenticate on the target system, gaining unauthorized access, escalating privileges, or moving laterally within the network. This attack exploits weaknesses in authentication protocols that accept hashed credentials as equivalent to the original password.

![[Image 3.44.png|center|700]]

Mitigating PtH attacks involves enforcing strong authentication methods, such as multifactor authentication (MFA), minimizing the use of cached credentials, and regularly updating and salting hashes to invalidate stolen credentials.

---

See also:

- [[On-path attack]]
- [[Hash value]]
- [[Multi-factor authentication (MFA)]]
- [[Salting]]
