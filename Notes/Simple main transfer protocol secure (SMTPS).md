
# Simple mail transfer protocol secure (SMTPS)

[[🏷️Network protocol]]

Simple mail transfer protocol secure (SMTPS) is a protocol used for securely sending emails over the internet. It is an extension of the standard Simple Mail Transfer Protocol (SMTP), incorporating encryption to protect email communication during transmission.

- **Port number and protocol type:** SMTPS operates over port 465 using TCP (Transmission Control Protocol) to ensure reliable data transfer.
- **Encryption:** SMTPS uses SSL/TLS encryption to secure the email transmission, ensuring the confidentiality and integrity of the message while in transit.
- **Authentication:** It supports authentication mechanisms to verify the identity of the sending mail server, preventing unauthorized access and mitigating email spoofing risks.
- **Request/response model:** Like SMTP, SMTPS follows a request-response model, where the client sends an email request, and the server responds with status messages regarding the email's delivery status.
- **SMTP vs. SMTPS:** While SMTP can be used without encryption, SMTPS ensures that the communication channel between mail servers is encrypted, offering a secure alternative to the standard SMTP protocol.

SMTPS is crucial for maintaining privacy and security in email communications, particularly for sensitive information.

---

See also:

- [[Simple mail transfer protocol (SMTP)]]
- [[Post office protocol (POP)]]
- [[Post office protocol version 3 secure (POP3S)]]
- [[Internet message access protocol (IMAP)]]
- [[Internet message access protocol secure (IMAPS)]]