
# Data packet

A data packet is a fundamental unit of information that travels across a network from one device to another. When data is transmitted, it's encapsulated in a packet that includes details on its origin, destination, and content. This information is specified through a port number, which helps computers manage and prioritize network traffic.

Each packet is akin to a physical letter. It has a header containing the destination device's [[IP address|IP address]], [[MAC address|MAC address]], and a protocol number that instructs how to process the packet's content. The packet's body carries the actual message, and the footer acts like a signature, marking the end of the packet.

The flow of data packets can reflect network performance, with [[Bandwidth|bandwidth]] being a key measure. All data packets include an IP address and are known as IP packets in [[Transmission control protocol (TCP)|TCP]] connections or datagrams in [[User datagram protocol (UDP)|UDP]] connections. 

**Image 2.34** Format of an IPv4 packet
![[Image 2.34.png]]

An IPv4 packet is made up of two sections, the header and the data:

- An IPv4 header format is determined by the IPv4 protocol and includes the IP routing information that devices use to direct the packet. The size of the IPv4 header ranges from 20 to 60 bytes. The first 20 bytes are a fixed set of information containing data such as the source and destination IP address, header length, and total length of the packet. The last set of bytes can range from 0 to 40 and consists of the options field.
  <br>
- The length of the data section of an IPv4 packet can vary greatly in size. However, the maximum possible size of an IPv4 packet is 65,535 bytes. It contains the message being transferred over the internet, like website information or email text.

**Image 2.35** Header of an IPv4 packet
![[Image 2.35.png]]

There are 13 fields within the header of an IPv4 packet:

- **Version (VER):** This 4 bit component tells receiving devices what protocol the packet is using. The packet used in the illustration above is an IPv4 packet.
  <br>
- **IP Header Length (HLEN or IHL):** HLEN is the packet’s header length. This value indicates where the packet header ends and the data segment begins.
  <br>
- **Type of Service (ToS):** Routers prioritize packets for delivery to maintain quality of service on the network. The ToS field provides the router with this information.
  <br>
- **Total Length:** This field communicates the total length of the entire IP packet, including the header and data. The maximum size of an IPv4 packet is 65,535 bytes.
  <br>
- **Identification:** IPv4 packets can be up to 65, 535 bytes, but most networks have a smaller limit. In these cases, the packets are divided, or fragmented, into smaller IP packets. The identification field provides a unique identifier for all the fragments of the original IP packet so that they can be reassembled once they reach their destination.
  <br>
- **Flags:** This field provides the routing device with more information about whether the original packet has been fragmented and if there are more fragments in transit.
  <br>
- **Fragmentation Offset:** The fragment offset field tells routing devices where in the original packet the fragment belongs.
  <br>
- **Time to Live (TTL):** TTL prevents data packets from being forwarded by routers indefinitely. It contains a counter that is set by the source. The counter is decremented by one as it passes through each router along its path. When the TTL counter reaches zero, the router currently holding the packet will discard the packet and return an ICMP Time Exceeded error message to the sender.
  <br>
- **Protocol:** The protocol field tells the receiving device which protocol will be used for the data portion of the packet.
  <br>
- **Header Checksum:** The header checksum field contains a checksum that can be used to detect corruption of the IP header in transit. Corrupted packets are discarded.
  <br>
- **Source IP Address:** The source IP address is the IPv4 address of the sending device.
  <br>
- **Destination IP Address:** The destination IP address is the IPv4 address of the destination device.
  <br>
- **Options:** The options field allows for security options to be applied to the packet if the HLEN value is greater than five. The field communicates these options to the routing devices.