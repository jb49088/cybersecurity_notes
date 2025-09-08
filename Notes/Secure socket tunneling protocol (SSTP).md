
# Secure socket tunneling protocol (SSTP)

[[🏷️Network protocol]]

Secure socket tunneling protocol (SSTP) is a VPN protocol developed by Microsoft that uses SSL/TLS to securely transmit data over a network. SSTP creates a secure tunnel between a client and a server, using port 443, which allows it to bypass firewalls and other network restrictions commonly imposed on other VPN protocols.

- **Port number and protocol type:** SSTP operates over TCP port 443 and uses SSL/TLS for encryption.
- **Encryption and security** – SSTP uses SSL/TLS to encrypt the entire communication channel, ensuring secure data transfer. This makes it highly effective in protecting against eavesdropping, man-in-the-middle attacks, and other security threats.
- **Bypassing firewalls** – Since SSTP uses TCP port 443, the same port used for HTTPS traffic, it can bypass most firewalls and network filters that may block other VPN protocols.
- **Microsoft integration** – SSTP is natively supported on Microsoft Windows platforms, making it a popular choice for users within a Microsoft-centric environment.
- **Authentication** – SSTP supports certificate-based authentication, allowing clients and servers to verify each other’s identity before establishing the VPN tunnel.
- **Reliable and secure** – SSTP provides a reliable and secure connection, particularly when operating in environments where other VPN protocols like PPTP or L2TP/IPSec might be blocked or less effective.

SSTP is a preferred VPN protocol for users looking for secure and reliable remote access, especially in environments with stringent network restrictions.

---

See also:

- [[Virtual private network (VPN)]]