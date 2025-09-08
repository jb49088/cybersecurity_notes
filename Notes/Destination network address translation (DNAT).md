
# Destination network address translation (DNAT)

Destination network address translation (DNAT) is a technique used in networking to modify the destination IP address of incoming packets as they pass through a router or firewall. It is commonly used to route traffic from external sources to internal servers or devices within a private network, making them accessible from the internet while keeping internal IP addresses hidden.

- **Traffic redirection:** DNAT allows external traffic to be redirected to specific internal resources, such as web servers or email servers, by altering the destination IP address in the packet headers.
- **Public to private network mapping:** DNAT maps public IP addresses (accessible from the internet) to private IP addresses within the internal network, enabling secure communication between external clients and internal servers.
- **Port forwarding:** Often used in conjunction with port forwarding, DNAT can direct specific types of traffic (e.g., HTTP on port 80) to the corresponding internal device or service.
- **Firewall and security:** DNAT helps with firewall management by enabling external access to specific services while keeping other internal resources isolated from the public network.
- **Load balancing:** DNAT can also be used for load balancing by distributing incoming traffic across multiple servers based on predefined rules.

DNAT is a valuable tool for managing network traffic, securing internal resources, and providing access to services hosted behind firewalls or NAT devices.

---

See also:

- [[Network address translation (NAT)]]
- [[Port forwarding]]