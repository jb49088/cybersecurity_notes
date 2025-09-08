
# Microsoft challenge handshake authentication protocol (MSCHAP)

[[🏷️Network protocol]]

Microsoft challenge handshake authentication protocol (MSCHAP) is a variation of the standard challenge handshake authentication protocol (CHAP) designed by Microsoft for secure authentication over networks. It is commonly used in virtual private networks (VPNs), dial-up connections, and wireless networks to verify user identities and provide encrypted communication.

- **Authentication mechanism:** MSCHAP works by sending a challenge from the server to the client, which responds with an encrypted value based on a shared secret (such as a password). The server then verifies the response to authenticate the user.
- **Two versions:** MSCHAP has two versions: MSCHAPv1 and MSCHAPv2. MSCHAPv2 provides stronger security by using mutual authentication, ensuring both the client and server verify each other’s identities.
- **Encryption:** MSCHAP uses encryption to protect the authentication exchange, providing confidentiality during the authentication process.
- **Vulnerabilities:** MSCHAP, particularly MSCHAPv1, is considered weak by modern security standards due to vulnerabilities that make it susceptible to attacks such as dictionary and brute-force attacks. MSCHAPv2 offers improved security, but it still has limitations and should be avoided in favor of more secure protocols like EAP-TLS.
- **Legacy use:** MSCHAP is still used in some older systems, but many organizations have transitioned to more secure authentication methods due to its vulnerabilities.

MSCHAP, especially in its earlier form (MSCHAPv1), is no longer considered secure for modern networks, and its use is generally discouraged in favor of stronger protocols that offer better protection against contemporary security threats.

---

See also:

- [[Challenge Handshake Authentication Protocol (CHAP)]]