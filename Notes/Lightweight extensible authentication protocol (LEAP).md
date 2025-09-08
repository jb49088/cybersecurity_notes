
# Lightweight extensible authentication protocol (LEAP)

[[🏷️Network protocol]]

Lightweight extensible authentication protocol (LEAP) is a proprietary wireless LAN (WLAN) authentication method developed by Cisco. It is designed to provide secure authentication for devices connecting to wireless networks. LEAP is based on the Extensible Authentication Protocol (EAP) and is widely used in enterprise environments to manage wireless network access.

- **Authentication process:** LEAP uses a challenge-response mechanism where the client and server exchange encrypted information to verify the identity of the user or device attempting to access the network.
- **Mutual authentication:** LEAP provides mutual authentication, ensuring that both the client and the network authenticate each other, reducing the risk of man-in-the-middle attacks.
- **Dynamic WEP keys:** LEAP generates dynamic Wired Equivalent Privacy (WEP) keys during the authentication process to encrypt data sent over the wireless network, enhancing security by preventing the use of static keys.
- **EAP-based:** LEAP leverages the Extensible Authentication Protocol (EAP), allowing flexibility in how authentication methods are deployed. It is commonly used with RADIUS servers to centralize authentication management.
- **Security concerns:** While LEAP was widely used in earlier wireless networks, it has known security vulnerabilities, including susceptibility to offline dictionary attacks, making it less secure compared to more modern protocols like EAP-TLS.

LEAP was once a popular choice for wireless authentication in enterprise settings but is now considered less secure and is gradually being phased out in favor of more secure authentication methods.

---

See also:

- [[Extensible authentication protocol (EAP)]]
- [[Remote authentication dial-in user service (RADIUS)]]