# nftables

nftables is a modern Linux kernel packet filtering framework that serves as the successor to iptables, offering a unified and more efficient approach to managing network traffic rules. Introduced in Linux kernel 3.13, it consolidates the functionality of iptables, ip6tables, arptables, and ebtables into a single cohesive tool.

- **Unified framework:** Unlike iptables, which required separate tools for IPv4, IPv6, and Ethernet bridging, nftables handles all protocols through a single interface, simplifying rule management across different network layers.
- **Improved syntax:** nftables uses a cleaner and more expressive rule syntax compared to iptables, reducing complexity and making rule sets easier to read, write, and maintain.
- **Tables and chains:** Similar to iptables, nftables organizes rules into tables and chains, but offers greater flexibility in how they are defined. Administrators can create custom tables and chains without being restricted to predefined structures.
- **Sets and maps:** nftables natively supports sets and maps, allowing administrators to group IP addresses, ports, or other values together and reference them efficiently within rules, reducing redundancy and improving performance.
- **Atomic rule updates:** nftables allows entire rule sets to be loaded and replaced atomically, meaning changes take effect all at once without a window of inconsistency that could expose the system to traffic policy gaps.
- **Backward compatibility:** nftables provides compatibility layers and translation tools such as iptables-nft, allowing existing iptables rules to be used while transitioning to nftables.

nftables represents the current standard for packet filtering on Linux systems, offering better scalability, performance, and flexibility than its predecessor while maintaining the core principles of kernel-level traffic control.

---

See also:

- [[firewall]]
- [[iptables]]
- [[linux]]
