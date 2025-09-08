
# Registration authority (RA)

A registration authority (RA) is an entity in a public key infrastructure (PKI) responsible for verifying the identity of individuals or organizations requesting digital certificates. It acts as an intermediary between certificate applicants and a certification authority (CA), ensuring that only authorized entities receive certificates.

- **Identity verification:** The RA validates the identity of the applicant, ensuring that the provided information matches the entity requesting the certificate.
- **Certificate requests:** Once the applicant's identity is verified, the RA forwards the request to the CA for the issuance of a digital certificate.
- **Policy enforcement:** RAs ensure compliance with the PKI policies and guidelines for certificate issuance, renewal, and revocation.
- **Certificate revocation:** In some cases, the RA may play a role in initiating the revocation process if a certificate is compromised or no longer needed.
- **Delegated authority:** While the CA ultimately issues the certificates, the RA provides the critical validation step, streamlining the certification process.

RAs are essential to the PKI ecosystem, providing a layer of trust by verifying identities and ensuring that digital certificates are only issued to legitimate entities.

---

See also:

- [[Certificate authority (CA)]]
- [[Digital certificate]]