
# File transfer protocol secure (FTPS)

[[🏷️Network protocol]]

File transfer protocol secure (FTPS) is an extension of the standard File Transfer Protocol (FTP) that adds support for secure connections. FTPS uses encryption to protect the data and control channels during file transfer, ensuring that sensitive files are securely transmitted over a network.

- **Port number and protocol type:** FTPS typically operates over port 990 for implicit SSL/TLS encryption, or port 21 when using explicit SSL/TLS encryption, using TCP (Transmission Control Protocol) for reliable data transfer.
- **Encryption:** FTPS uses SSL/TLS encryption to secure the control and data channels, ensuring that all data transferred between the client and server is protected against eavesdropping and tampering.
- **Authentication:** FTPS supports certificate-based authentication to verify the identities of the client and server, helping to prevent unauthorized access to file transfer operations.
- **Request/response model:** FTPS follows the traditional FTP request-response model, where a client sends a request to the server for file transfer operations, and the server responds with status messages regarding the action being performed.
- **FTP vs. FTPS:** While FTP transfers data in plaintext, FTPS adds encryption, making it a more secure choice for file transfer, especially when dealing with sensitive or confidential information.

FTPS is commonly used for secure file transfers in industries that require compliance with data protection regulations, such as finance and healthcare.

---

See also:

- [[File transfer protocol (FTP)]]