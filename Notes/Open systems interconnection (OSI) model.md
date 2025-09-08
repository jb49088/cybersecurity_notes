
# Open systems interconnection (OSI) model

The open systems interconnection (OSI) model is a conceptual framework used to understand and describe how different network protocols interact within a communication system. It divides the process of communication into seven distinct layers, each of which handles specific tasks related to network operations. The OSI model helps standardize networking functions to enable interoperability between different systems and technologies.

The seven layers of the OSI model include:

- **Application Layer (Layer 7):** The application layer is the closest layer to the end user. It provides interfaces and protocols for applications to communicate over a network, such as HTTP, FTP, and SMTP. It interacts directly with software applications that rely on the network.
- **Presentation Layer (Layer 6):** The presentation layer focuses on data translation and encryption. It is responsible for converting data into a format that the receiving application can understand, ensuring data is properly compressed or encrypted as needed.
- **Session Layer (Layer 5):** The session layer manages the establishment, maintenance, and termination of communication sessions between applications. It ensures that data is properly synchronized and organized for communication, handling session recovery if needed.
- **Transport Layer (Layer 4):** The transport layer ensures the reliable transfer of data between two devices, managing flow control, error correction, and retransmission. Protocols like TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) operate at this layer.
- **Network Layer (Layer 3):** The network layer is responsible for routing data between different networks. It manages logical addressing, such as IP addresses, and handles the forwarding of packets. Routers operate at this layer to direct traffic across networks.
- **Data Link Layer (Layer 2):** The data link layer is responsible for establishing, maintaining, and terminating connections between devices on the same network. It ensures reliable data transfer by handling error correction and flow control. Common protocols include Ethernet and Wi-Fi.
- **Physical Layer (Layer 1):** The physical layer deals with the transmission of raw data bits over a physical medium (e.g., cables, switches, radio waves). It defines the hardware elements involved in the communication, such as electrical signals, cables, and network interfaces.
    
The OSI model helps in understanding and diagnosing network issues by breaking down complex network communication into manageable layers. By isolating problems to specific layers, network administrators can identify and resolve issues more effectively. It also promotes standardization and compatibility between different networking technologies and protocols.

---

See also:

- [[TCP ⁄ IP model]]
- [[Network Protocol]]
