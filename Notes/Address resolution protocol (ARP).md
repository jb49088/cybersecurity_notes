
# Address resolution protocol (ARP)

[[🏷️Network protocol]]

The Address Resolution Protocol (ARP) is a network protocol used to map an IP address to a physical machine address, also known as a Media Access Control (MAC) address, within a local network. ARP is crucial for ensuring that data packets are correctly delivered to the appropriate devices on a network, as IP addresses alone cannot directly identify devices on the data link layer.

- **IP to MAC mapping**: ARP resolves an IP address to a MAC address by broadcasting a request packet to the network, asking "Who has this IP address?" The device with the matching IP address replies with its MAC address.
- **ARP cache**: Devices store the IP-to-MAC address mappings in a local ARP cache for faster access, reducing the need for repeated ARP requests. This cache can become outdated or vulnerable to manipulation.
- **Types of ARP requests**:
    - **ARP request**: A broadcast message asking for the MAC address associated with a specific IP address.
    - **ARP reply**: A unicast message providing the MAC address in response to an ARP request.
- **ARP spoofing/poisoning**: A security vulnerability where an attacker sends fake ARP replies to associate their own MAC address with another device's IP address, enabling man-in-the-middle attacks or denial of service (DoS) attacks.
- **Uses in networking**: ARP operates within local area networks (LANs) to ensure proper communication between devices. It is used by both IPv4 and legacy protocols.

ARP plays a vital role in network communication, ensuring that devices can identify each other based on their IP addresses and properly route data packets.

---

See also:

- [[Media access control (MAC)]]
- [[MAC address]]
- [[ARP poisoning]]