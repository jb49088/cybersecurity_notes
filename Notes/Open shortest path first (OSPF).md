
# Open shortest path first (OSPF)

[[🏷️Network protocol]]

Open shortest path first (OSPF) is a link-state routing protocol used in IP networks to determine the most efficient path for data transmission. It is widely used in large enterprise and service provider networks due to its ability to scale and quickly adapt to network changes.

- **Link-state routing protocol:** OSPF maintains a map of the network topology and calculates the shortest path using Dijkstra’s algorithm.
- **Hierarchical structure:** OSPF networks are divided into **areas**, reducing routing overhead and improving efficiency. The backbone area (Area 0) connects other areas.
- **Convergence and scalability:** OSPF converges quickly after network changes, making it suitable for large, dynamic networks.
- **Cost-based metric:** OSPF assigns a **cost** to each link, with lower-cost paths being preferred for routing traffic.
- **Authentication support:** OSPF includes authentication options to prevent unauthorized routing updates.
- **Multicast communication:** OSPF routers communicate using multicast addresses **224.0.0.5** (all OSPF routers) and **224.0.0.6** (designated routers).
- **Port and transport:** OSPF operates directly over **IP protocol number 89**, rather than using TCP or UDP.

By providing fast convergence, efficient routing updates, and strong scalability, OSPF is a preferred choice for dynamic and large-scale IP networks.

---

See also:

- [[Routing Information Protocol (RIP)]]
- [[Border gateway protocol (BGP)]]