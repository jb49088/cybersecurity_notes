
# Network time protocol (NTP)

[[🏷️Network protocol]]

Network time protocol (NTP) is a protocol used to synchronize the clocks of computers and devices over a network. It ensures that all devices within a network maintain the same time, which is essential for time-sensitive applications and accurate logging of events.

- **Port number and protocol type:** NTP operates over port 123 using UDP (User Datagram Protocol) for low-latency communication.
- **Time synchronization:** NTP synchronizes the device clock with a reference time source, such as an atomic clock or GPS system, to provide highly accurate timekeeping.
- **Hierarchy of servers:** NTP uses a hierarchical system of servers called stratum levels, with stratum 1 servers being directly connected to reference time sources, and stratum 2 or higher servers synchronizing with them.
- **Accuracy:** NTP can provide synchronization accuracy in the range of milliseconds over the internet, and even microseconds on local networks.
- **Offset correction:** NTP accounts for network delays and adjusts time calculations accordingly to maintain synchronization.

NTP is crucial for applications that depend on precise timing, such as logging, cryptographic protocols, and financial transactions.

---

See also:
