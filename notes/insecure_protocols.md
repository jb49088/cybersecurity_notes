# Insecure protocols

Insecure protocols are communication methods that lack adequate security measures, exposing data to potential interception, tampering, or unauthorized access. Common examples include using HTTP instead of HTTPS, or older protocols like FTP or Telnet, which transmit information in plaintext without encryption.

Risks of insecure protocols include:

- **Data Interception:** Sensitive information, such as passwords or personal data, can be captured during transmission.
- **Data Tampering:** Unencrypted communication can be altered by attackers during transit.
- **Credential Theft:** Login credentials transmitted over insecure protocols are vulnerable to capture by attackers.

To mitigate these risks, organizations should replace insecure protocols with secure alternatives, such as:

- **HTTPS:** Encrypts web traffic to ensure secure communication over the internet.
- **SFTP or FTPS:** Secure file transfer protocols that encrypt data during transmission.
- **SSH:** Secures remote access and replaces plaintext protocols like Telnet.

Regular audits and enforcement of secure communication standards help protect against vulnerabilities associated with insecure protocols.

---

See also:

- [[encryption]]
- [[hypertext_transfer_protocol_secure_(https)]]
- [[ssh_file_transfer_protocol_(sftp)]]
- [[transport_layer_security_(tls)]]
- [[man-in-the-middle_(mitm)]]
