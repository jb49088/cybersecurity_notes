
# New technology LAN manager (NTLM)

[[🏷️Network protocol]]

New technology LAN manager (NTLM) is a suite of authentication protocols used by Microsoft Windows systems to provide authentication, integrity, and confidentiality within local area networks (LANs). NTLM was introduced to replace the older LAN Manager (LM) authentication system and is still in use today, although it is largely superseded by more secure protocols like Kerberos.

- **Authentication process:** NTLM uses a challenge-response mechanism to verify the identity of users. It relies on a hashed password to ensure the security of user credentials during the authentication process.
- **Compatibility:** NTLM is supported by older versions of Windows and systems that do not support Kerberos, making it essential in mixed environment setups.
- **NTLMv1 and NTLMv2:** NTLM has two main versions: NTLMv1, which is considered insecure, and NTLMv2, which offers better security with stronger hashing algorithms and protection against certain types of attacks.
- **Vulnerabilities:** NTLM is vulnerable to various attacks, including pass-the-hash, relay, and brute-force attacks, which is why it is considered less secure than modern authentication methods.
- **Fallback authentication:** NTLM can be used as a fallback protocol when Kerberos authentication is unavailable, but its use is discouraged due to security concerns.

While NTLM is still used in some environments, its limitations and vulnerabilities make it advisable to migrate to more secure authentication protocols like Kerberos wherever possible.

---

See also:

- [[Kerberos]]
- [[Active directory (AD)]]
- [[Windows]]