
# Load balancer

[[🏷️Networking device]]

A load balancer is a device or software solution that distributes incoming traffic across multiple servers to ensure optimal utilization, efficiency, and reliability of resources. The load balancer makes sure that no single server becomes overwhelmed with too much traffic, providing a smoother experience for end users. It works invisibly to the user, who doesn’t notice the distribution of requests among multiple servers.

In large-scale environments such as web server farms or database farms, load balancers are crucial for ensuring the system remains responsive and operational. They also contribute to **fault tolerance** by ensuring that server outages do not disrupt service, and they can quickly shift traffic to operational servers with minimal downtime.

There are two main types of load balancing configurations:

- **Active/active load balancing**: All servers in the pool are actively handling traffic, which provides better resource utilization and scalability. Additional features like TCP offload, SSL offload, caching, and prioritization can further optimize performance and speed.
    
- **Active/passive load balancing**: Some servers are designated as active and handle all incoming traffic, while passive servers remain on standby. If an active server fails, one of the passive servers automatically takes its place, minimizing service disruptions.

Load balancers are fundamental for high-availability and scalability in modern network infrastructures.

---

See also:

- [[High availability (HA)]]
- [[Scalability]]