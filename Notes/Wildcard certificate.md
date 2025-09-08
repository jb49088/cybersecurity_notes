
# Wildcard certificate

A wildcard certificate is an SSL/TLS certificate that secures a domain and all of its subdomains using a single certificate. Instead of requiring separate certificates for each subdomain, a wildcard certificate simplifies management and reduces costs.

A wildcard certificate uses an asterisk (`*`) as a placeholder for subdomains. For example, a certificate for `*.example.com` would secure:

- `www.example.com`
- `mail.example.com`
- `shop.example.com`

Wildcard certificates are useful for organizations that manage multiple subdomains under a single domain. They allow for easier deployment and flexibility, as new subdomains can be added without issuing a new certificate. However, they also come with risks—if the private key is compromised, all subdomains using that certificate are affected.

---

See also:

- [[Digital certificate]]
- [[Self-signed certificate]]
- [[Certificate authority (CA)]]