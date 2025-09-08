
# Internet protocol security (IPsec)

[[🏷️Network protocol]]

Internet protocol security (IPsec) is a suite of protocols used to secure IP communications by authenticating and encrypting each IP packet in a communication session. IPsec is commonly used to establish Virtual Private Network (VPN) tunnels, ensuring secure data transmission over untrusted networks like the internet.

- **Port number and protocol type:** IPsec operates over UDP port 500 (for IKE) and ESP (IP protocol 50) and AH (IP protocol 51) for data transport.
- **Encryption and security** – IPsec provides encryption and authentication using various algorithms, including AES (Advanced Encryption Standard) and 3DES (Triple Data Encryption Standard), to secure the communication channel.
- **Protocols** – IPsec operates using two main protocols:
    - **Authentication Header (AH):** Provides authentication for data packets and ensures integrity but does not offer encryption.
    - **Encapsulating Security Payload (ESP):** Provides both encryption and authentication, ensuring data confidentiality and integrity.
- **Transport and tunnel modes** – IPsec can operate in two modes:
    - **Transport mode:** Only the payload (data) of the IP packet is encrypted or authenticated.
    - **Tunnel mode:** The entire IP packet, including the header, is encrypted, providing full protection for communication between networks.
- **Key exchange** – IPsec relies on the Internet Key Exchange (IKE) protocol to securely exchange cryptographic keys between peers, ensuring the security of the session.
- **Authentication methods** – IPsec can use digital certificates, Pre-shared Keys (PSK), or RSA encryption for authenticating devices.

IPsec is widely used for creating secure VPN tunnels between devices, such as remote access VPNs and site-to-site VPNs, ensuring private communication over public networks.

---

See also:

- [[Virtual private network (VPN)]]
- [[Internet key exchange (IKE)]]
- [[Encapsulating security payload (ESP)]]
- [[Authentication header (AH)]]
