
# Demilitarized zone (DMZ)

A demilitarized zone (DMZ) is a physical or logical subnetwork that separates an internal network from an untrusted network, typically the internet. It serves as a buffer zone that limits direct access between the internal systems of an organization and external networks, enhancing the security of the internal infrastructure.

The DMZ typically hosts services that need to be accessible from the outside world, such as web servers, mail servers, and DNS servers, while keeping the internal network and its sensitive systems isolated. The idea is that any attack targeting services in the DMZ should be contained, minimizing the risk to internal systems.

Key characteristics of a DMZ include:

- **Isolation**: Internal systems are isolated from the external network by placing them in the DMZ, reducing the exposure to attacks.
- **Access control**: Access between the internal network and the DMZ is tightly controlled using firewalls, intrusion detection/prevention systems (IDS/IPS), and other security measures.
- **Public-facing services**: Servers that must be accessed by external users are placed in the DMZ, reducing the risk to internal systems.

A well-configured DMZ can significantly enhance network security by providing an additional layer of protection between external and internal resources.

---

See also:

- [[Firewall]]
- [[Network segmentation]]
- [[Jump server]]