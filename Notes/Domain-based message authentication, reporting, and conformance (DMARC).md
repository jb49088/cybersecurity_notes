
# Domain-based message authentication, reporting, and conformance (DMARC)

[[🏷️Network protocol]]

Domain-based message authentication, reporting, and conformance (DMARC) is an email authentication protocol used to protect domains from unauthorized use, such as email spoofing or phishing attacks. DMARC allows domain owners to specify how email from their domain should be authenticated using Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM). It also provides a way for domain owners to receive reports on email authentication activity.

DMARC works by publishing a DMARC record in the DNS of the domain. This record defines the policy for handling emails that fail SPF and DKIM checks, which can include actions like quarantine or reject. DMARC also enables the generation of reports, which provide valuable insights into email traffic and security events.

A typical DMARC policy might include the following options:

- **none**: No specific action is taken; only reports are generated.
- **quarantine**: Emails that fail DMARC checks are marked as suspicious and may be placed in the spam folder.
- **reject**: Emails that fail DMARC checks are outright rejected by the receiving mail server.

DMARC helps prevent malicious actors from impersonating a legitimate domain, thus protecting both the domain owner and recipients from phishing and spam attacks.

---

See also:

- [[Sender policy framework (SPF)]]
- [[DomainKeys identified mail (DKIM)]]
- [[Domain name system (DNS)]]
- [[Mail gateway]]
