
# SSH file transfer protocol (SFTP)

[[🏷️Network protocol]]

SSH file transfer protocol (SFTP) is a secure file transfer protocol that operates over the secure shell (SSH) protocol. It provides a secure and encrypted method for transferring files between a client and a server, ensuring data integrity and confidentiality.

- **Port number:** SFTP operates over port 22, the same port used by SSH.
- **Protocol type:** SFTP uses TCP (Transmission Control Protocol) for reliable and ordered data delivery.
- **Encryption:** SFTP encrypts both the data and the authentication process, providing a secure channel for file transfer.
- **Authentication:** Users authenticate using SSH keys or passwords, leveraging the security of SSH for both access and data transfer.
- **File management:** SFTP allows users to upload, download, rename, delete, and list files on the remote server, similar to traditional FTP but with added security.
- **No separate data connection:** Unlike FTP, which requires separate control and data channels, SFTP uses a single encrypted connection for both commands and data transfer.
- **Security benefits:** SFTP is widely preferred over FTP because it offers strong encryption and protection against eavesdropping, man-in-the-middle attacks, and data tampering.

SFTP is the secure alternative to FTP, offering a reliable solution for secure file transfers in both corporate and personal environments.

---

See also:

- [[Secure shell (SSH)]]
- [[File transfer protocol (FTP)]]
