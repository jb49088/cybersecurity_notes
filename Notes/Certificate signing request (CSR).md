
# Certificate signing request (CSR)

A certificate signing request (CSR) is a message sent from an applicant to a Certificate Authority (CA) to apply for a digital certificate. It contains information about the organization or individual requesting the certificate, including the public key that will be used in the certificate.

The process begins by creating a key pair, which consists of a private key and a corresponding public key. The applicant generates the CSR by sending the public key to the CA, along with identifying details. The CA then validates the request, confirming key ownership and verifying domain ownership, email addresses, and other necessary information to ensure the legitimacy of the request.

Once validated, the CA digitally signs the certificate with its private key. The signed certificate is then returned to the applicant, who can now use it for secure communications. This process helps ensure that the identity associated with the public key is legitimate and trusted by users and systems relying on the certificate.

![[Image 2.73.png|center|600]]

---

See also:

- [[Certificate authority (CA)]]
- [[Digital certificate]]
- [[Digital signature]]
- [[Public key]]
- [[Private key]]


