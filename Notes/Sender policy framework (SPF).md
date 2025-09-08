
# Sender policy framework (SPF)

[[🏷️Network protocol]]

Sender policy framework (SPF) is an email authentication protocol designed to prevent unauthorized senders from sending emails on behalf of a domain. It helps to combat email spoofing, phishing, and spam by allowing domain owners to specify which mail servers are authorized to send emails for their domain. SPF works by checking the "From" address of an incoming email against a list of authorized mail servers published in the domain's DNS records.

An SPF record is a type of DNS record that lists the IP addresses or hostnames of the servers allowed to send email on behalf of the domain. When an email is received, the recipient's mail server performs an SPF check to see if the sending server is on the list. If the email fails the SPF check, it is typically flagged as suspicious or rejected, depending on the recipient's configuration.

A typical SPF record might include the following components:

- **v=spf1**: Specifies the version of SPF being used (always "spf1").
- **ip4**: Specifies an IPv4 address or range that is authorized to send emails for the domain.
- **ip6**: Specifies an IPv6 address or range that is authorized to send emails for the domain.
- **include**: Refers to another domain's SPF record, which is useful for third-party services (e.g., email marketing platforms).
- **all**: Specifies how to handle mail from unauthorized sources, usually as “-all” (reject) or “~all” (soft fail).

An example of an SPF record might look like this:

`v=spf1 ip4:192.168.0.1 include:_spf.google.com -all`

This record indicates that only the IP address `192.168.0.1` and any server listed in `_spf.google.com` are authorized to send emails on behalf of the domain, and all other senders should be rejected.

SPF is a critical component of email security and works in conjunction with other protocols like DKIM and DMARC to ensure that email messages are authentic and come from trusted sources.

---

See also:

- [[DomainKeys identified mail (DKIM)]]
- [[Domain-based message authentication, reporting, and conformance (DMARC)]]
- [[Domain name system (DNS)]]
- [[Mail gateway]]