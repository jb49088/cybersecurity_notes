
# Layer 2 tunneling protocol (L2TP)

[[🏷️Network protocol]]

Layer 2 tunneling protocol (L2TP) is a VPN tunneling protocol used to securely transmit data over public and private networks. It is often combined with IPsec for encryption, as L2TP itself does not provide built-in encryption. L2TP is an evolution of Point-to-Point Tunneling Protocol (PPTP) and Layer 2 Forwarding (L2F), offering improved security and flexibility.

- **Port number and protocol type:** L2TP operates over UDP port 1701 and does not use TCP to avoid connection overhead.
- **Encryption:** L2TP alone does not provide encryption, but it is commonly paired with IPsec (L2TP/IPsec) for strong encryption and authentication.
- **Authentication:** L2TP supports PPP authentication methods such as PAP, CHAP, and MS-CHAPv2, but security is greatly enhanced when combined with IPsec.
- **Encapsulation:** L2TP encapsulates PPP frames and transmits them over an IP network, making it more secure and flexible than PPTP.
- **Performance:** L2TP introduces additional overhead due to double encapsulation (L2TP and IPsec), which can result in slightly lower performance compared to other VPN protocols.
- **Security:** When used with IPsec, L2TP/IPsec provides strong security, but it is less efficient than newer protocols like OpenVPN and WireGuard.

L2TP is widely supported across operating systems and network devices, making it a popular VPN solution, especially when paired with IPsec for secure communications.

---

See also:

- [[Point-to-point tunneling protocol (PPTP)]]
- [[Internet protocol security (IPsec)]]
- [[Virtual private network (VPN)]]