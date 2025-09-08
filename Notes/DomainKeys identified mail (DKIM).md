
# DomainKeys identified mail (DKIM)

[[🏷️Network protocol]]

DomainKeys identified mail (DKIM) is an email authentication method designed to detect email spoofing and prevent unauthorized use of a domain in email messages. DKIM uses public-key cryptography to sign outgoing email messages with a cryptographic signature that is verified by the receiving mail server. This allows the recipient to confirm that the message was indeed sent by the domain owner and that it has not been altered in transit.

In DKIM, the sending mail server generates a unique signature for each email message by hashing certain parts of the message (e.g., headers and body) and encrypting this hash with a private key. This signature is then attached to the email as a DKIM-Signature header. The receiving mail server, using the public key published in the DNS record of the sending domain, can verify the authenticity of the signature.

A typical DKIM implementation involves the following components:

- **Private Key**: Stored securely on the sending mail server and used to create the cryptographic signature for the email.
- **Public Key**: Published in the DNS of the sending domain. It is used by receiving mail servers to verify the DKIM signature.
- **DKIM Signature**: Added to the email header, containing information about the signing domain, the public key's location, and the hash of the message content.

DKIM is often used in conjunction with other authentication methods, such as Sender Policy Framework (SPF) and Domain-based Message Authentication, Reporting & Conformance (DMARC), to provide comprehensive protection against email-based attacks.

---

See also:

- [[Sender policy framework (SPF)]]
- [[Domain-based message authentication, reporting, and conformance (DMARC)]]
- [[Domain name system (DNS)]]
- [[Mail gateway]]