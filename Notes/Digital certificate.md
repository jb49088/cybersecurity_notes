
# Digital certificate

[[🏷️Cryptography]]

A digital certificate is a public key certificate that binds a public key with the identity of its holder through a digital signature. These certificates are used to establish trust in digital communications, enabling secure data exchange between parties. By incorporating a digital signature, they authenticate the identity of the certificate holder and verify the integrity of transmitted data.

Public key infrastructure (PKI) commonly relies on certificate authorities (CAs) to issue and manage digital certificates, adding an extra layer of trust. Alternatively, a web of trust approach uses endorsements from other users to verify identities. Certificates can be created using built-in operating system tools, such as windows domain services, or by employing third-party solutions.

## What’s in a digital certificate?

Digital certificates typically adhere to the X.509 standard format, which defines the structure and information they must contain. Key details in a certificate include:

- **Serial number**: A unique identifier for the certificate.
- **Version**: Indicates the X.509 version used.
- **Signature Algorithm**: Specifies the cryptographic algorithm used to create the certificate’s digital signature.
- **Issuer**: Identifies the certificate authority (CA) that issued the certificate.
- **Certificate Holder's Name**: Details the entity to which the certificate is issued.
- **Public Key**: Contains the public key of the certificate holder.
- **Extensions**: Optional fields providing additional functionality or constraints, such as usage restrictions.

Digital certificates play a critical role in enabling secure web communication, ensuring data authenticity, and establishing user and system trust.

---

See also:

- [[X.509]]
- [[Certificate signing request (CSR)]]
- [[Certificate revocation list (CRL)]]
- [[Certificate authority (CA)]]
- [[Registration authority (RA)]]
- [[Digital signature]]
- [[Self-signed certificate]]
- [[Wildcard certificate]]
- [[Online certificate status protocol (OCSP)]]