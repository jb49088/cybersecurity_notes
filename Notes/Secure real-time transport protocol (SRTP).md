
# Secure real-time transport protocol (SRTP)

[[🏷️Network protocol]]

Secure real-time transport protocol (SRTP) is an extension of the Real-time Transport Protocol (RTP) that provides encryption, authentication, and integrity for real-time audio and video communications. It is commonly used in VoIP, video conferencing, and streaming applications to protect sensitive media data from eavesdropping and tampering.

- **Port number and protocol type:** SRTP operates over the same dynamic UDP port ranges as RTP, typically starting at 5004, ensuring secure, low-latency media transmission.
- **Encryption:** SRTP uses AES (Advanced Encryption Standard) to encrypt media streams, preventing unauthorized access and ensuring confidentiality.
- **Authentication and integrity:** SRTP includes message authentication codes (HMAC-SHA1) to verify data integrity and prevent tampering or replay attacks.
- **Key management:** SRTP relies on external protocols such as DTLS-SRTP or MIKEY to securely exchange encryption keys between communication endpoints.
- **Low overhead:** SRTP is optimized for real-time applications, adding minimal processing overhead while maintaining high performance and low latency.

SRTP is widely adopted in secure VoIP, teleconferencing, and multimedia streaming to ensure private and authenticated real-time communications.

---

See also:

- [[Real-time transport protocol (RTP)]]