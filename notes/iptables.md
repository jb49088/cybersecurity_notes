# iptables

iptables is a command-line utility on Linux systems that allows administrators to configure, manage, and inspect the packet filtering rules of the Linux kernel firewall. It acts as the primary interface for defining how network traffic is handled, including which packets are accepted, dropped, or forwarded based on defined rules.

- **Chains:** iptables organizes rules into chains, which represent different points in the packet processing pipeline. The three default chains are INPUT (incoming traffic), OUTPUT (outgoing traffic), and FORWARD (traffic being routed through the system).
- **Tables:** Rules are grouped into tables based on their purpose. The most commonly used tables are the filter table for general packet filtering, the nat table for network address translation, and the mangle table for packet alteration.
- **Rules and matches:** Each rule specifies match conditions such as source IP, destination IP, protocol, or port, and an associated target action such as ACCEPT, DROP, or REJECT. Packets are evaluated against rules in order until a match is found.
- **Stateful filtering:** iptables supports stateful packet inspection through the conntrack module, allowing rules to be written based on the state of a connection, such as NEW, ESTABLISHED, or RELATED.
- **Persistence:** By default, iptables rules are not saved across reboots. Tools like iptables-save and iptables-restore, or service managers, are used to persist rule sets between system restarts.
- **nftables successor:** iptables is gradually being replaced by nftables, a more modern framework that offers improved performance and a simplified rule syntax, though iptables remains widely used and supported.

iptables is a foundational tool for network security on Linux systems, enabling administrators to enforce traffic policies, protect services, and control the flow of data at the kernel level.

---

See also:

- [[firewall]]
- [[nftables]]
- [[linux]]
