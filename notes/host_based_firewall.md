# Host-based firewall

[[🏷️Network security]]

A host-based firewall is a software firewall running directly on an individual endpoint or server, controlling traffic at the operating system level. Unlike network-based firewalls which protect an entire network, host-based firewalls enforce policy specific to the host they run on, filtering traffic regardless of where it originates — including other machines on the same local network.

- **Per-host enforcement:** Rules are applied directly on the machine itself, meaning every connection attempt — whether from the internet, the local network, or even another compromised internal host — is subject to inspection. This makes host-based firewalls effective against lateral movement that network firewalls cannot see.
- **Granular control:** Host-based firewalls can enforce rules based on specific applications, users, or processes in addition to ports and protocols. This allows tighter policy than a network firewall which has no visibility into what process is making a connection.
- **Defense in depth:** Host-based firewalls are a critical layer in a defense in depth strategy. If an attacker bypasses the network perimeter, individual hosts still enforce their own rules. A compromised machine on the network cannot freely communicate with other hosts if each one is running its own firewall.
- **East-west traffic filtering:** In environments where machines communicate heavily with each other — servers, VMs, containers — host-based firewalls control this east-west traffic that never touches the network perimeter. This is especially relevant in cloud and virtualized environments.
- **Common implementations:** nftables and iptables on Linux, Windows Defender Firewall on Windows, and pf on BSD systems are all host-based firewall implementations. These are configurable at a low level, allowing precise rule construction as you've been doing with nftables.
- **Offensive relevance:** Attackers who gain access to a network must still contend with host-based firewalls on each target. Common evasion approaches include binding to already-allowed ports, abusing allowed outbound connections for C2 communication, and disabling or tampering with the firewall if sufficient privileges are obtained — which is why protecting firewall configuration and monitoring for changes is important.
- **Limitations:** Host-based firewalls rely on the host itself being trustworthy. If an attacker achieves sufficient privilege on a machine, they can modify or disable the firewall entirely. This contrasts with a network firewall which an attacker on the internal network generally cannot directly modify.

Host-based firewalls are an essential complement to network-based controls, ensuring that security does not collapse entirely if the perimeter is breached.

---

See also:

- [[Firewall]]
- [[Defense in depth]]
- [[nftables]]
- [[iptables]]
- [[Lateral movement]]
- [[Network-based firewall]]
