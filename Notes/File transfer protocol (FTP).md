
# File transfer protocol (FTP)

[[🏷️Network protocol]]

File Transfer Protocol (FTP) is a standard network protocol used for transferring files between computers over a TCP/IP network. It allows users to upload, download, and manage files on remote servers, commonly used in web development, file sharing, and system administration.

- **Port numbers:** FTP uses port 21 for the control connection (commands) and port 20 for the data connection (file transfers).
- **Protocol type:** FTP uses TCP (Transmission Control Protocol) for reliable and ordered data delivery.
- **Active mode:** In active mode, the client connects to the server on port 21, and the server opens a random port for data transfer.
- **Passive mode:** In passive mode, the client requests a specific port from the server for data transfer, making it suitable for clients behind firewalls.
- **Authentication:** FTP generally requires a username and password for login, although anonymous FTP allows access without authentication.
- **Unencrypted protocol:** FTP transmits data, including login credentials, in plaintext, which can be vulnerable to interception. Secure alternatives like FTPS and SFTP are used for encrypted transfers.
- **File management:** FTP allows users to upload, download, rename, delete, and manage files on remote servers.

FTP is widely used for transferring files but lacks encryption, which can be a security concern for sensitive data.

---

See also:

- [[SSH file transfer protocol (SFTP)]]
- [[File transfer protocol secure (FTPS)]]
- [[Trivial File Transfer Protocol (TFTP)]]