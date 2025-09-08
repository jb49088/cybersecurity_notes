
# Mandatory access control (MAC)

[[🏷️Access control model]]

Mandatory access control (MAC) is a security model in which the operating system enforces strict policies to control access to resources based on predefined classifications. Users and resources are assigned security labels, and access is determined by these labels.

- **Operating system enforcement:** Access permissions are controlled by the operating system, not individual users. This ensures a consistent and centralized application of policies.
- **Object labeling:** Every resource, such as files or data, is assigned a security label (e.g., confidential, secret, top secret) that determines its sensitivity level.
- **Access rules:** Administrators define the rules that determine which users can access specific security levels, ensuring only authorized individuals gain access.
- **Immutable by users:** Users cannot alter their access levels or the security labels of objects, ensuring the integrity of the control system.

Mandatory access control is commonly used in environments requiring high levels of security, such as government or military systems, where strict access restrictions are necessary to protect sensitive information.

---

See also:

- [[Attribute-based access control (ABAC)]]
- [[Discretionary access control (DAC)]]
- [[Role-based access control (RBAC)]]
- [[Rule-based access control (RBAC)]]
- [[SELinux]]