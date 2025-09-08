
# Dynamic host configuration protocol (DHCP)

[[🏷️Network protocol]]

Dynamic host configuration protocol (DHCP) is a network management protocol used to automatically assign IP addresses and other network configuration parameters to devices (clients) on a network. It reduces the need for manual configuration and helps maintain consistent network settings across devices.

- **Port numbers:** DHCP uses UDP port 67 for communication from the client to the server, and UDP port 68 for communication from the server to the client.
- **Protocol type:** DHCP operates over UDP (User Datagram Protocol) because it is lightweight and does not require a connection-oriented service.
- **Address assignment:** DHCP assigns IP addresses dynamically from a pre-defined pool, ensuring devices can join the network without requiring manual configuration.
- **Lease time:** DHCP assigns IP addresses with a lease time, meaning the address is temporarily allocated to a device. Once the lease expires, the device must request a new IP address.
- **Configuration options:** In addition to assigning IP addresses, DHCP can also provide other essential network configuration information, such as default gateway addresses, DNS servers, and subnet masks.
- **Types of DHCP messages:** The DHCP process involves several message types, including **DHCPDISCOVER**, **DHCPOFFER**, **DHCPREQUEST**, and **DHCPACK**, used to negotiate and confirm settings between the client and server.

DHCP simplifies network administration by automating IP address assignment, ensuring devices can seamlessly connect to the network.

---

See also:

- [[Internet protocol (IP)]]
