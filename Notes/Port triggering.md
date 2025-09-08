
# Port Triggering

[[🏷️Networking]]

Port triggering is a technique used in networking to allow incoming traffic through a router or firewall when certain outgoing traffic is detected on specific ports. Unlike port forwarding, which establishes a static rule for specific ports, port triggering is dynamic and temporary. It opens specific ports only when a predefined trigger event occurs on a particular port, allowing the router or firewall to automatically respond to certain outgoing traffic.

When a device within the local network sends a request to a specific port (the trigger port), the router "triggers" and temporarily opens a set of incoming ports (triggered ports) for the return traffic. These opened ports remain active only for the duration of the session, and they are closed once the session ends. This makes port triggering more secure than static port forwarding, as it ensures that the ports are not permanently open to the outside world.

Port triggering is often used for applications or services that require dynamic communication, such as online gaming, video conferencing, or VoIP, where the server may initiate connections back to the client on different ports. It helps maintain the security of the network by limiting exposure to the internet while still enabling necessary communication.

---

See also:

- [[Port forwarding]]
- [[Network address translation (NAT)]]
- [[Firewall]]
- [[Voice over internet protocol (VoIP)]]