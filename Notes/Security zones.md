
# Security zones

Security zones refer to logical or physical divisions of a network that help to establish clear boundaries for applying security policies. These zones are used to segment a network into areas with different levels of trust and security, allowing more precise control over traffic and access.

Zone-based security technologies provide a more flexible and secure method than traditional IP address ranges for controlling traffic between different segments of the network. By defining security zones, organizations can apply tailored policies to each zone, ensuring that only authorized traffic is allowed and that the right level of protection is provided for each area.

![[Image 2.67.png]]

Common security zones include:

- **Trusted zone**: This is typically where internal systems and resources reside, with higher levels of trust and access.
- **Untrusted zone**: Usually associated with external or public networks like the Internet, where security is weaker and stricter controls are required.
- **Screened zone**: A zone that acts as an intermediary, often containing systems such as firewalls or demilitarized zones (DMZ) that filter traffic between trusted and untrusted zones.
- **Servers zone**: Dedicated to application servers, database servers, and other critical infrastructure that require specific access control.

By clearly defining these zones and the traffic flow between them, organizations can enforce security policies that limit the exposure of sensitive systems and reduce the risk of attacks.

---

See also:

- [[Network segmentation]]







