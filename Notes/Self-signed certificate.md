
# Self-signed certificate

A self-signed certificate is a digital certificate that is signed by the same entity that issued it, rather than by a trusted certificate authority (CA). Because it is not verified by a third party, a self-signed certificate does not provide the same level of trust as a CA-issued certificate.

Self-signed certificates are commonly used for:

- **Testing and development**: Useful for internal environments where a trusted certificate is not necessary.
- **Internal applications**: Used within private networks where external trust validation is not required.
- **Personal encryption**: Can be used to encrypt emails or files without relying on an external authority.

While self-signed certificates provide encryption, they are not inherently trusted by browsers and operating systems. This can lead to security warnings when accessing websites that use them. To establish trust within an organization, a self-signed certificate can be manually installed on systems or distributed through an internal public key infrastructure (PKI).

---

See also:

- [[Digital certificate]]
- [[Wildcard certificate]]
- [[Certificate authority (CA)]]