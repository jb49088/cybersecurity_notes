
# Generic routing encapsulation (GRE)

[[🏷️Network protocol]]

Generic routing encapsulation (GRE) is a tunneling protocol used to encapsulate a wide variety of network layer protocols in order to create a point-to-point connection across an IP network. GRE allows for the transmission of packets from one network to another, encapsulating them into IP packets for transport.

- **Tunneling protocol:** GRE is commonly used to create tunnels between two endpoints over an IP network, allowing the transport of data from one network to another in a secure and encapsulated format.
- **Protocol flexibility:** GRE can encapsulate a variety of Layer 3 protocols, including IPv4, IPv6, and even non-IP protocols, making it versatile for different network configurations.
- **Simplicity:** GRE is a simple protocol that does not provide encryption, meaning it is not inherently secure. It is often used in conjunction with other protocols, such as IPsec, to provide additional security.
- **Routing support:** GRE supports dynamic routing protocols, allowing it to adapt to changes in the network topology. It enables features such as multiprotocol routing and the ability to carry multicast traffic.
- **Use cases:** Common use cases for GRE include connecting remote sites in a Virtual Private Network (VPN), creating network overlays, and enabling the transport of multicast traffic or routing information across different networks.

While GRE is useful for network tunneling and routing, it is often paired with other protocols to address security and encryption needs.

---

See also:

- [[Encapsulation]]
- [[Virtual private network (VPN)]]
- [[Internet protocol security (IPsec)]]