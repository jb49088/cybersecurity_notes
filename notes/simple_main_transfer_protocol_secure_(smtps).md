# Simple mail transfer protocol secure (SMTPS)

Simple mail transfer protocol secure (SMTPS) is a protocol used for securely sending emails over the internet. It is an extension of the standard Simple Mail Transfer Protocol (SMTP), incorporating encryption to protect email communication during transmission.

- **Port number and protocol type:** SMTPS operates over port 465 using TCP (Transmission Control Protocol) to ensure reliable data transfer.
- **Encryption:** SMTPS uses SSL/TLS encryption to secure the email transmission, ensuring the confidentiality and integrity of the message while in transit.
- **Authentication:** It supports authentication mechanisms to verify the identity of the sending mail server, preventing unauthorized access and mitigating email spoofing risks.
- **Request/response model:** Like SMTP, SMTPS follows a request-response model, where the client sends an email request, and the server responds with status messages regarding the email's delivery status.
- **SMTP vs. SMTPS:** While SMTP can be used without encryption, SMTPS ensures that the communication channel between mail servers is encrypted, offering a secure alternative to the standard SMTP protocol.

SMTPS is crucial for maintaining privacy and security in email communications, particularly for sensitive information.

---

See also:

- [[simple_mail_transfer_protocol_(smtp)]]
- [[post_office_protocol_(pop)]]
- [[post_office_protocol_version_3_secure_(pop3s)]]
- [[internet_message_access_protocol_(imap)]]
- [[internet_message_access_protocol_secure_(imaps)]]
