
# Subject alternative name (SAN)

Subject alternative name (SAN) is an extension to the X.509 specification that allows additional identities to be associated with a digital certificate. While a standard SSL/TLS certificate identifies a single domain or hostname, SAN enables a certificate to secure multiple domains, subdomains, IP addresses, or email addresses under a single certificate.

SAN is commonly used in SSL/TLS certificates for securing multiple websites or services, reducing the need for separate certificates and simplifying certificate management.

- **Multi-domain support:** Allows a single certificate to cover multiple domain names, such as example.com, [www.example.com](http://www.example.com), and mail.example.com.
- **Wildcard support:** Can include wildcard entries to secure all subdomains of a domain (e.g., *.example.com).
- **IP address support:** Allows securing multiple IP addresses, both IPv4 and IPv6.
- **Email address support:** Can secure multiple email addresses for certificate-based email encryption.
- **Simplified management:** Reduces the complexity of managing individual certificates for each domain, improving efficiency and cost-effectiveness.

SAN is essential for businesses that operate multiple domains or services, offering a flexible and efficient way to secure them all with a single certificate.

---

See also:

- [[Digital certificate]]
- [[X.509]]