
# Post office protocol version 3 secure (POP3S)

[[🏷️Network protocol]]

Post office protocol version 3 secure (POP3S) is a secure version of the Post Office Protocol version 3 (POP3), used for retrieving email messages from a mail server. POP3S enhances the security of the traditional POP3 protocol by adding SSL/TLS encryption, ensuring that email communications are securely transmitted.

- **Port number and protocol type:** POP3S operates over port **995** using TCP (Transmission Control Protocol) for reliable data transfer.
- **Encryption:** POP3S uses SSL/TLS encryption to protect the communication between the email client and server, securing the email content and preventing unauthorized access or tampering during transmission.
- **Authentication:** POP3S supports secure authentication methods to verify the identity of both the client and server, helping to mitigate risks such as unauthorized access or email account compromises.
- **Request/response model:** POP3S operates with a request-response model, where the client sends requests to the server to download or manage email messages, and the server responds with the requested data or status information.
- **POP3 vs. POP3S:** While POP3 operates without encryption, POP3S adds SSL/TLS encryption, making it a more secure method for retrieving email messages and protecting sensitive data.

POP3S is commonly used when security is critical, offering encrypted communication for email retrieval and ensuring privacy and data protection during the entire process.

---

See also:

- [[Post office protocol (POP)]]
- [[Simple mail transfer protocol (SMTP)]]
- [[Internet message access protocol (IMAP)]]