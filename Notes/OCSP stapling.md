
# OCSP stapling

OCSP stapling is a method used to improve the efficiency and scalability of certificate revocation checking during SSL/TLS handshakes. Normally, the online certificate status protocol (OCSP) requires a client to query the certificate authority (CA) directly to check if a certificate is still valid. However, this can become inefficient, especially for high-traffic websites.

With OCSP stapling, the certificate holder's server retrieves and stores the OCSP response, which includes the certificate's status. This status is then "stapled" into the SSL/TLS handshake and digitally signed by the CA. By doing so, the client can verify the certificate status directly from the server, reducing the need for repeated OCSP checks to the CA and improving performance.

---

See also:

- [[Online certificate status protocol (OCSP)]]
- [[Certificate authority (CA)]]
- [[Digital certificate]]
- [[Certificate revocation list (CRL)]]


