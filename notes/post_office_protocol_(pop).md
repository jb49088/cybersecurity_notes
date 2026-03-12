# Post office protocol (POP)

Post office protocol (POP) is an email retrieval protocol used by email clients to retrieve messages from a mail server. POP allows users to download emails from a mail server to their local devices for offline reading.

- **Port number and protocol type:** POP typically operates over port 110 using TCP.
- **Email retrieval:** POP downloads email messages from the mail server to the user's local device, removing them from the server in the process (unless configured otherwise). This ensures that the email is stored locally for offline access.
- **Version:** The original POP protocol (POP2) has largely been replaced by POP3, which is more widely used and offers additional features, including the ability to leave copies of messages on the server.

POP is a simple and efficient method of downloading email, but its lack of synchronization between devices and server can make it less suitable for modern email management compared to newer protocols like IMAP.

---

See also:

- [[post_office_protocol_version_3_secure_(pop3s)]]
- [[simple_mail_transfer_protocol_(smtp)]]
- [[internet_message_access_protocol_(imap)]]
