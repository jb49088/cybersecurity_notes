
# Authentication header (AH)

Authentication header (AH) is a component of the IPsec (Internet Protocol Security) suite that provides data integrity, authentication, and optional anti-replay protection for IP packets. Unlike encryption protocols, AH does not provide confidentiality; instead, it ensures that the data has not been tampered with and verifies the authenticity of the sender.

AH operates by adding a header to the original IP packet, which contains cryptographic information used for authentication. This header covers most of the IP packet, ensuring its integrity during transmission. However, certain fields in the IP header, like those that change in transit (e.g., TTL), are excluded from the authentication process.

Key features of Authentication Header include:

- **Data Integrity:** Ensures that the data has not been altered in transit.
- **Authentication:** Verifies the identity of the sender using cryptographic methods.
- **Anti-Replay Protection:** Prevents attackers from resending intercepted packets by incorporating sequence numbers.

AH is often used in conjunction with the Encapsulating Security Payload (ESP) protocol, which provides encryption, to create a more comprehensive security solution. AH is particularly useful in scenarios where data integrity and authentication are prioritized over confidentiality.

---

See also:

- [[Internet protocol security (IPsec)]]
- [[Virtual private network (VPN)]]
- [[Encapsulating security payload (ESP)]]
- [[Internet key exchange (IKE)]]