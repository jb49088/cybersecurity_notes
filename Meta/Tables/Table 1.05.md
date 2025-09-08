| **Port Number** | **Service name** | **Transport protocol** | **Description**                                                                                                         | 
| --------------- | ---------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 7               | Echo             | TCP, UDP               | Echo service                                                                                                            |
| 20              | FTP-data         | TCP, SCTP              | File Transfer Protocol data transfer                                                                                    |
| 21              | FTP              | TCP, UDP, SCTP         | File Transfer Protocol (FTP) control connection                                                                         |
| 22              | SSH-SCP          | TCP, UDP, SCTP         | Secure Shell, secure logins, file transfers (scp, sftp), and port forwarding                                            |
| 23              | Telnet           | TCP                    | Telnet protocol--unencrypted text communications                                                                        |
| 25              | SMTP             | TCP                    | Simple Mail Transfer Protocol, used for email routing between mail servers                                              |
| 53              | DNS              | TCP, UDP               | Domain Name System name resolver                                                                                        |
| 67              | DHCP Server      | UDP                    | Used by the DHCP server to receive client requests for IP addresses.                                                    |
| 68              | DHCP Client      | UDP                    | Used by the DHCP client to receive responses from the DHCP server.                                                      |
| 69              | TFTP             | UDP                    | Trivial File Transfer Protocol                                                                                          |
| 80              | HTTP             | TCP,UDP,SCTP           | Hypertext Transfer Protocol (HTTP) uses TCP in versions 1.x and 2. HTTP/3 uses QUIC, a transport protocol on top of UDP |
| 110             | POP3             | TCP                    | Post Office Protocol version 3, used for retrieving emails from a server.                                               |
| 143             | IMAP             | TCP                    | Internet Message Access Protocol; used for accessing email on a server.                                                 |
| 587             | SMTP             | TCP                    | SMTP with STARTTLS; used for securely submitting email from clients to servers.                                         |
| 993             | IMAPS            | TCP                    | IMAP Secure; uses SSL/TLS to encrypt email access points.                                                               |
| 995             | POP3S            | TCP                    | POP3 Secure; uses SSL/TLS to encrypt email retrieval sessions.                                                          |
