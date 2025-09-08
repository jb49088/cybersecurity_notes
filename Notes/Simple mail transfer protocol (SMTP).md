
# Simple mail transfer protocol (SMTP)

[[🏷️Network protocol]]

Simple mail transfer protocol (SMTP) is an Internet standard communication protocol used for sending and receiving email messages between email servers. It is responsible for routing and delivering email messages across networks.

- **Port numbers:** SMTP typically uses port 25 for communication between mail servers, port 587 for secure submission of emails (with STARTTLS), and port 465 for secure email transmission over SSL/TLS.
- **Protocol type:** SMTP operates over TCP (Transmission Control Protocol) to ensure reliable transmission of messages.
- **Message transfer:** SMTP facilitates the transfer of email messages from the sender’s email client to the recipient’s mail server and between intermediate mail servers.
- **Authentication:** While SMTP itself doesn't provide authentication, it can work with other protocols like POP3 or IMAP for retrieving messages, or be used alongside authentication methods like SMTP-AUTH to prevent unauthorized email sending.
- **Text-based protocol:** SMTP is a text-based protocol that communicates commands like HELO, MAIL FROM, RCPT TO, and DATA, to manage the email message flow.
- **Limitations:** SMTP is primarily used for sending emails, but it does not handle retrieving or storing messages, which is handled by protocols such as IMAP or POP3.

SMTP is a critical protocol for email delivery and is widely used across the internet for communication.

---

See also:

- [[Simple main transfer protocol secure (SMTPS)]]
- [[Post office protocol (POP)]]
- [[Post office protocol version 3 secure (POP3S)]]
- [[Internet message access protocol (IMAP)]]
- [[Internet message access protocol secure (IMAPS)]]