
# Internet protocol (IP)

[[🏷️Network protocol]]

Internet protocol (IP) is the fundamental protocol for routing and addressing data across networks, enabling devices to communicate with each other over the internet. It provides a standardized way to deliver packets of data from a source device to a destination device.

- **Packet-based communication:** IP divides data into smaller units called packets, which are transmitted independently and reassembled at the destination.
- **Logical addressing:** Each device on a network is assigned a unique IP address, used to identify the source and destination of data packets.
- **Versioning:** There are two main versions of IP in use:
    - **IPv4:** Uses 32-bit addresses, supporting approximately 4.3 billion unique addresses.
    - **IPv6:** Uses 128-bit addresses, providing a vastly larger address space and improved functionality.
- **Routing:** IP enables packets to traverse multiple networks and routers, using routing tables to find the best path to the destination.
- **Unreliable delivery:** IP does not guarantee delivery, packet order, or error correction; these tasks are handled by higher-level protocols like TCP.
- **Fragmentation and reassembly:** IP handles the fragmentation of large packets to fit within the maximum transmission unit (MTU) of the network and reassembles them at the destination.

IP is the backbone of modern networking, supporting protocols like TCP and UDP to create reliable and efficient communication systems.

---

See also:

- [[IP address]]
- [[Transmission control protocol (TCP)]]
- [[User datagram protocol (UDP)]]