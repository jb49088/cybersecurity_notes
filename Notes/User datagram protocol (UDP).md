
# User datagram protocol (UDP)

[[🏷️Network protocol]]

User datagram protocol (UDP) is a core component of the Internet protocol suite, designed for connectionless communication. Unlike TCP, UDP focuses on speed and efficiency rather than reliability, making it suitable for applications where real-time data transfer is more critical than error correction.

- **Connectionless communication:** UDP does not establish a connection before sending data, reducing latency and enabling faster transmissions.
- **Low overhead:** UDP does not include mechanisms for acknowledgment, retransmission, or ordering, resulting in minimal protocol overhead.
- **Best-effort delivery:** Data packets (datagrams) are sent without guarantees of delivery or sequence, making it less reliable than TCP but faster.
- **Broadcast and multicast support:** UDP is ideal for scenarios where data needs to be sent to multiple recipients simultaneously, such as streaming or group communication.
- **Common use cases:** UDP is widely used for real-time applications like voice over IP (VoIP), video streaming, online gaming, and Domain Name System (DNS) queries.

While UDP sacrifices reliability, its efficiency and low latency make it an essential protocol for scenarios where speed and timeliness are more critical than data integrity.

---

See also:

- [[Transmission control protocol (TCP)]]
- [[Internet protocol (IP)]]