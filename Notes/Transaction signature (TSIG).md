
# Transaction signature (TSIG)

Transaction signature (TSIG) is a security mechanism used in DNS to authenticate and secure communications between DNS servers. It ensures the integrity and authenticity of DNS messages by using shared secret keys and cryptographic hashing. TSIG is commonly used for securing zone transfers, dynamic DNS (DDNS) updates, and other DNS transactions that require authentication.

- **Mutual authentication:** Uses pre-shared keys to authenticate communication between DNS servers.
- **Message integrity:** Prevents tampering by applying a cryptographic signature to DNS messages.
- **Replay attack protection:** Includes a timestamp to ensure requests are valid and not reused.
- **Commonly used for DNS zone transfers:** Secures the transfer of DNS records between primary and secondary servers.
- **Limited scalability:** Requires manual key management, making it less practical for large-scale DNS deployments.

TSIG enhances DNS security by protecting critical transactions from unauthorized modifications and forgery.

---

See also:

- [[Domain name system (DNS)]]