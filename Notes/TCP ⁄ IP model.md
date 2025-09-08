
# TCP ⁄ IP model

The TCP ⁄ IP model is a conceptual framework that defines a set of protocols used for communication over a network. It is the foundational model for the internet and most modern networking systems. Unlike the OSI model, which consists of seven layers, the TCP/IP model has four layers, each responsible for specific aspects of data communication.

The four layers of the TCP/IP model include:

1. **Link Layer (Network Interface Layer):** The link layer is responsible for the physical transmission of data over the network. It defines the protocols and standards that operate at the hardware level, including Ethernet, Wi-Fi, and other physical network technologies. This layer handles tasks such as framing, addressing, and error detection.
2. **Internet Layer:** The internet layer is responsible for routing data packets between devices across different networks. It uses logical addressing (IP addresses) to direct traffic and determine the best path for data to travel across the network. The primary protocol at this layer is the Internet Protocol (IP), which is responsible for addressing and packet forwarding.
3. **Transport Layer:** The transport layer ensures reliable data transfer between devices. It manages flow control, error correction, and data segmentation. Two key protocols operate at this layer: Transmission Control Protocol (TCP), which ensures reliable, ordered data transmission, provides error recovery, and retransmits lost data; and User Datagram Protocol (UDP), which offers faster, connectionless communication but does not guarantee reliability.
4. **Application Layer:** The application layer is where end-user applications interact with the network. It provides protocols that enable communication between applications running on different devices. Some common protocols at this layer include Hypertext Transfer Protocol (HTTP) for web browsing, File Transfer Protocol (FTP) for file transfer, and Simple Mail Transfer Protocol (SMTP) for email transmission.
    
The TCP/IP model is essential for understanding how data travels through a network and how different protocols work together to ensure communication. It is the basis for most modern networking, including the internet.

---

See also:

- [[Open systems interconnection (OSI) model]]
- [[Network Protocol]]