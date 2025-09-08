
# Protected extensible authentication protocol (PEAP)

[[🏷️Network protocol]]

Protected extensible authentication protocol (PEAP) is a network authentication protocol that enhances security by encapsulating extensible authentication protocol (EAP) within a transport layer security (TLS) tunnel. PEAP is commonly used in wireless networks and VPNs to provide secure authentication without exposing user credentials.

PEAP operates by establishing a secure TLS session between the client and authentication server before transmitting authentication credentials. This prevents attackers from intercepting or tampering with authentication data.

- **Encapsulation of EAP:** Protects authentication exchanges by encrypting them within a TLS tunnel.
- **Mutual authentication:** Requires both the client and server to verify each other’s identities.
- **Credential protection:** Shields usernames and passwords from exposure during transmission.
- **Support for multiple authentication methods:** Works with EAP methods like EAP-MSCHAPv2 for username/password authentication.
- **Widely used in enterprise Wi-Fi networks:** Often deployed with WPA2-Enterprise or WPA3-Enterprise for secure wireless access.

PEAP enhances security by protecting authentication data from eavesdropping and man-in-the-middle attacks, making it a preferred choice for enterprise network authentication.

---

See also:

- [[Extensible authentication protocol (EAP)]]
- [[Transport Layer Security (TLS)]]
- [[Virtual private network (VPN)]]