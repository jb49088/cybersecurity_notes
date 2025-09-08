
# IEEE 802.1X

IEEE 802.1X is a standard for port-based network access control, commonly used in Ethernet and Wi-Fi networks to authenticate devices before granting them access to the network. It defines how devices (known as supplicants) must authenticate themselves with a network switch, wireless access point (AP), or other network access devices (known as authenticator) using a centralized authentication server (typically via the RADIUS protocol).

Key components of IEEE 802.1X include:

- **Supplicant**: The device requesting access to the network (e.g., a computer or smartphone).
- **Authenticator**: The network device (e.g., a switch or access point) that controls access to the network and forwards authentication requests to the authentication server.
- **Authentication Server**: A centralized server, typically using RADIUS, that validates the credentials of the supplicant and decides whether access should be granted.

The main objective of IEEE 802.1X is to enhance network security by ensuring that only authorized devices can access the network. This is particularly useful in environments with high security requirements, such as enterprise networks or public Wi-Fi hotspots. The protocol operates by enforcing authentication before allowing any data traffic, thus protecting the network from unauthorized access.

---

See also:

- [[Network access control (NAC)]]
- [[AAA server]]
