
# Network address translation (NAT)

Network address translation (NAT) is a technique used in networking to modify the source or destination IP addresses of packets as they pass through a router or firewall. NAT helps improve security and manage IP address usage, especially in networks with limited public IP addresses.

- **IP address conservation:** NAT allows multiple devices within a private network to share a single public IP address. This is especially useful when there are fewer available public IP addresses than devices needing internet access.
- **Private and public IP addresses:** Devices in a private network are assigned private IP addresses (e.g., 192.168.x.x), which are not routable on the public internet. NAT translates these private addresses to a public IP address when accessing external resources.
- **Types of NAT:**
    - **Static NAT:** A one-to-one mapping between a private IP address and a public IP address.
    - **Dynamic NAT:** Maps a private IP address to a pool of public IP addresses, assigning a public address from the pool as needed.
    - **Port Address Translation (PAT):** Also known as "overloading," PAT maps multiple private IP addresses to a single public IP address, distinguishing them by different port numbers.
- **Security benefits:** NAT hides the internal network structure, making it more difficult for external attackers to target specific devices within a private network.
- **Limitations:** NAT can interfere with certain protocols that rely on direct addressing, such as some peer-to-peer applications or VOIP services, requiring additional configuration like NAT traversal techniques.

NAT plays a vital role in modern networking by enabling more efficient use of IP addresses and improving network security.

---

See also:

- [[IP address]]
- [[Dynamic host configuration protocol (DHCP)]]

  