
# Point-to-point tunneling protocol (PPTP)

[[🏷️Network protocol]]

Point-to-Point Tunneling Protocol (PPTP) is a VPN protocol used to create encrypted tunnels for secure communication over public or private networks. It is based on the Point-to-Point Protocol (PPP) and was one of the first VPN protocols widely adopted for remote access and site-to-site connections.

- **Port number and protocol type:** PPTP operates over TCP port **1723** and uses the GRE (Generic Routing Encapsulation) protocol for tunneling.
- **Encryption:** PPTP supports MPPE (Microsoft Point-to-Point Encryption) for securing data, but it is considered weak by modern security standards.
- **Authentication:** Since PPTP is based on PPP, it supports PPP authentication methods such as PAP, CHAP, and MS-CHAPv2, though some of these have known vulnerabilities.
- **Performance:** PPTP is lightweight and offers fast speeds due to its low encryption overhead, making it suitable for older systems or low-bandwidth connections.
- **Security concerns:** PPTP has multiple known vulnerabilities, including weak encryption and susceptibility to man-in-the-middle attacks, making it unsuitable for sensitive data transmission.

Due to its security flaws, PPTP is generally not recommended, with more secure alternatives such as L2TP/IPsec, OpenVPN, and WireGuard being preferred.

---

See also:

- [[Virtual private network (VPN)]]
- [[Point-to-Point Protocol (PPP)]]
- [[Layer 2 tunneling protocol (L2TP)]]