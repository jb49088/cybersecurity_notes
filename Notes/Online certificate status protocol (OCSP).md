
# Online certificate status protocol (OCSP)

[[🏷️Network protocol]]

The online certificate status protocol (OCSP) is a protocol used to check the revocation status of digital certificates. It is an alternative to the Certificate Revocation List (CRL), which requires downloading a large file containing the revocation status of many certificates. OCSP allows for a more efficient, real-time query and response system for checking if a certificate has been revoked by the Certificate Authority (CA).

When a client (such as a web browser) connects to a server and receives a certificate, the client can use OCSP to query the CA or an OCSP responder to verify whether the certificate is still valid or has been revoked. The CA will return a signed response indicating the status of the certificate (e.g., "good", "revoked", or "unknown"). This process helps maintain trust and security by ensuring the client is communicating with a valid entity.

OCSP is commonly used in SSL/TLS certificates to verify the authenticity and integrity of websites. It's faster and more efficient than CRLs because it allows clients to check the certificate status in real-time without needing to download large revocation lists.

---

See also:

- [[Certificate revocation list (CRL)]]
- [[OCSP stapling]]
- [[Certificate authority (CA)]]
- [[Digital certificate]]