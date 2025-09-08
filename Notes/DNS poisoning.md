
# DNS poisoning

[[🏷️Network attack]]

DNS poisoning, also known as DNS spoofing, is an attack where attackers manipulate domain name system (DNS) records to redirect users to malicious websites. By corrupting DNS data, attackers can impersonate legitimate services, enabling phishing, malware distribution, and data theft. This attack can be carried out by compromising a DNS server to alter records, modifying a client’s local host file (which takes precedence over DNS queries), or intercepting valid DNS queries and injecting fake responses in real time as part of an on-path attack.

DNS poisoning impacts include redirecting users to phishing websites to steal credentials, delivering malware through malicious sites, and disrupting services by misdirecting traffic away from legitimate resources. To mitigate these attacks, organizations can implement DNSSEC to validate DNS responses, restrict access to host files to prevent unauthorized changes, and use intrusion detection systems and firewalls to block spoofing attempts. Additional measures include patching DNS software regularly and adopting encrypted DNS protocols like DNS over HTTPS (DoH) or DNS over TLS (DoT).

---

See also:

- [[Domain name system (DNS)]]
- [[Domain hijacking]]
- [[On-path attack]]
- [[DNS over HTTPS (DoH)]]

