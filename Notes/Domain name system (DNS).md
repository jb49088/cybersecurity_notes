
# Domain name system (DNS)

[[🏷️Network protocol]]

Domain name system (DNS) is a hierarchical system used to translate human-readable domain names into machine-readable IP addresses. It is a critical component of the internet, enabling users to access websites and services by using easy-to-remember domain names rather than numeric IP addresses.

- **Port numbers:** DNS primarily operates over port 53 for both TCP and UDP connections.
- **Protocol type:** DNS uses both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). UDP is used for most queries due to its faster, connectionless nature, while TCP is used for tasks like zone transfers.
- **Resolution process:** DNS resolves domain names by querying a series of DNS servers (root servers, authoritative name servers) until it finds the corresponding IP address.
- **Caching:** DNS servers and clients cache results to improve performance and reduce the load on servers, storing the results for a specific time (TTL – Time to Live).
- **Record types:** DNS supports various record types, including **A records** (IPv4 addresses), **AAAA records** (IPv6 addresses), **MX records** (mail servers), and **CNAME records** (canonical names).
- **Security concerns:** DNS is vulnerable to attacks like DNS spoofing and cache poisoning, so DNSSEC (DNS Security Extensions) is often used to add a layer of security by digitally signing data.

DNS plays an essential role in enabling easy access to websites and services, translating domain names into IP addresses that computers use to communicate.

---

See also:

- [[DNS filtering]]
- [[DNS poisoning]]
- [[DNS tunneling]]