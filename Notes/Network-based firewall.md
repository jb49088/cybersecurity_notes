# Network-based firewall

[[🏷️Network security]]

A network-based firewall is a security device or software solution positioned at the boundary of a network, controlling traffic flow between different network segments or between an internal network and the internet. Rather than protecting a single host, a network-based firewall enforces policy for all traffic passing through it, making it the first line of defense in most network architectures.

- **Perimeter enforcement:** Network-based firewalls sit at network boundaries, inspecting traffic entering and leaving the network. All external traffic must pass through the firewall before reaching internal hosts, making it a natural choke point for filtering.
- **Stateful inspection:** Modern network firewalls track the state of connections using a connection table, allowing return traffic for established sessions while blocking unsolicited inbound packets. This is more effective than simple stateless filtering which evaluates each packet in isolation.
- **Rule-based traffic filtering:** Administrators define rules based on source/destination IP, port, protocol, and direction. Traffic matching allow rules is forwarded, everything else is dropped or rejected.
- **Network address translation (NAT):** Network firewalls commonly perform NAT, translating private internal IP addresses to a public-facing address. This provides a layer of obscurity by hiding internal network topology from external observers.
- **Segmentation:** Beyond perimeter defense, network firewalls are used to segment internal networks into zones, restricting traffic between departments, VLANs, or trust levels. This limits blast radius if a segment is compromised.
- **Blind spot — lateral movement:** A network firewall only sees traffic that crosses its boundary. Traffic between two hosts on the same network segment never passes through it, meaning an attacker who has gained internal access can move laterally without touching the perimeter firewall at all.
- **Offensive relevance:** From an attacker's perspective, bypassing or pivoting past a network firewall is a primary objective during exploitation. Techniques include tunneling traffic over allowed protocols, exploiting misconfigured rules, and abusing outbound connections which are often less restricted than inbound.

Network-based firewalls are a foundational control in any network architecture, but their effectiveness depends entirely on traffic being forced through them. Any path that bypasses the firewall renders its rules irrelevant.

---

See also:

- [[Firewall]]
- [[Host-based firewall]]
- [[Network address translation (NAT)]]
- [[Network segmentation]]
- [[Defense in depth]]
- [[Next-generation firewall (NGFW)]]
