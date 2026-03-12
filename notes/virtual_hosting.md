# Virtual hosting

Virtual hosting is a method that allows a single web server to host multiple websites or web applications on the same physical machine and IP address. By examining information in the HTTP request, the server determines which site or application the client is attempting to reach and responds accordingly, making the distinction invisible to the end user.

- **Name-based virtual hosting:** The most common form of virtual hosting, where the server uses the Host header in the HTTP request to determine which site to serve. Multiple domain names resolve to the same IP address, and the server differentiates between them using this header value.
- **IP-based virtual hosting:** Each hosted site is assigned a unique IP address on the same physical server. This approach is less common due to the scarcity of IPv4 addresses but can be used when SSL/TLS certificates or other requirements demand separate IPs.
- **Host header importance:** The Host header is central to how name-based virtual hosting functions. Manipulating or fuzzing this header is a common technique in bug bounty hunting, as misconfigurations can expose internal applications, admin panels, or development environments not intended to be publicly accessible.
- **Virtual host enumeration:** Because virtual hosts sharing an IP address are not always publicly listed or discoverable through DNS, security testers use tools like gobuster in vhost mode to brute-force potential hostnames and uncover hidden applications running on the same server.
- **Isolation concerns:** Poorly configured virtual hosting environments can lead to cross-site data leakage or unintended access between hosted applications, particularly in shared hosting environments.

Virtual hosting is a foundational web infrastructure concept that bug bounty hunters frequently encounter, as hidden virtual hosts can expose forgotten subdomains, staging environments, or internal tooling that significantly expands the attack surface of a target.

---

See also:

- [[ip_address]]
- [[internet_protocol_(ip)]]
- [[domain_name_system_(dns)]]
- [[hypertext_transfer_protocol_(http)]]
- [[hypertext_transfer_protocol_secure_(https)]]
- [[gobuster]]
- [[curl]]
- [[host_header_injection]]
