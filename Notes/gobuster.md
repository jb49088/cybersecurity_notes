# gobuster

[[🏷️Cybersecurity tool]]

Gobuster is an open-source command-line tool used for brute-forcing URIs, DNS subdomains, virtual hostnames, and open Amazon S3 buckets. Written in Go, it is widely used in penetration testing and security assessments to discover hidden content and resources on web servers that are not publicly linked or indexed.

- **Directory and file brute-forcing:** Gobuster iterates through a wordlist to discover hidden directories and files on a target web server, revealing content that may not be visible through normal browsing.
- **DNS subdomain enumeration:** In DNS mode, gobuster attempts to enumerate valid subdomains of a target domain, helping identify additional attack surfaces or forgotten assets.
- **Virtual host discovery:** Gobuster can brute-force virtual hostnames on a web server, uncovering sites that share the same IP address but respond to different host headers.
- **Wordlist-driven:** The effectiveness of gobuster depends heavily on the quality and relevance of the wordlist used. Common wordlists such as those from SecLists are frequently paired with the tool.
- **Speed and concurrency:** Because it is written in Go, gobuster is highly performant and supports concurrent requests, making scans significantly faster than many comparable tools.

Gobuster is a staple in the reconnaissance and enumeration phases of penetration testing, helping security professionals map out a target's attack surface before deeper exploitation is attempted.

---

See also:

- [[Wordlist]]
- [[Enumeration]]
- [[Reconnaissance]]
- [[Directory traversal]]