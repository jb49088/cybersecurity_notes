
# SYN Flood

[[🏷️Network attack]]

A SYN flood attack is a type of Denial of Service (DoS) attack that targets the way TCP connections are established. To understand this better, let's first look at how a TCP connection is set up. It starts with a three-step handshake process seen in [[Diagram 1.07]].

1. **SYN Request:** The device wanting to connect sends a SYN (synchronize) request to the server.
2. **SYN/ACK Response:** The server responds with a SYN/ACK (synchronize/acknowledge) packet, confirming it received the request and is ready for the final step.
3. **ACK Completion:** The device sends an ACK (acknowledge) packet to complete the connection.

In a SYN flood attack, malicious actors exploit this process by sending a flood of SYN packets to the server, overwhelming it with more connection requests than it can handle. Since the server can't complete the handshake because it's waiting for the final ACK packets that never come, it gets bogged down and can't process legitimate requests, effectively crashing or slowing down its services.