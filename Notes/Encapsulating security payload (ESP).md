
# Encapsulating security payload (ESP)

[[🏷️Network protocol]]

Encapsulating security payload (ESP) is a protocol used within the IPsec (Internet Protocol Security) suite to provide confidentiality, data integrity, authentication, and optional anti-replay protection for IP packets. Unlike the Authentication Header (AH), ESP offers encryption in addition to the data integrity and authentication it provides.

ESP works by encapsulating the original IP packet in a new IP packet with an ESP header and trailer. The payload, which is the original data, is encrypted to ensure confidentiality. The ESP trailer includes a checksum to ensure data integrity and can also contain an anti-replay field to prevent attackers from resending captured packets.

Key features of ESP include:

- **Confidentiality:** Encrypts the payload to protect the data from unauthorized access.
- **Data Integrity:** Provides a checksum to ensure the data has not been altered in transit.
- **Authentication:** Verifies the identity of the sender using cryptographic methods.
- **Anti-Replay Protection:** Helps prevent replay attacks by incorporating sequence numbers.

ESP is widely used to secure virtual private networks (VPNs) and other secure communication channels, ensuring both privacy and integrity in sensitive data transfers.

---

See also:

- [[Internet protocol security (IPsec)]]
- [[Virtual private network (VPN)]]
- [[Internet key exchange (IKE)]]
- [[Authentication header (AH)]]
