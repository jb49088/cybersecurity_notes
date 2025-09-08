
# Real-time transport protocol (RTP)

[[🏷️Network protocol]]

Real-time transport protocol (RTP) is a network protocol used for delivering real-time audio, video, and other time-sensitive data over IP networks. It is widely used in applications such as VoIP (Voice over IP), video conferencing, streaming media, and telephony services.

- **Port number and protocol type:** RTP typically operates over dynamic UDP port ranges, often starting at 5004, to ensure low-latency data transmission.
- **Packet-based transmission:** RTP breaks multimedia streams into packets and transmits them in sequence, enabling efficient streaming of real-time data.
- **Synchronization:** RTP includes timestamps and sequence numbers to help receivers reconstruct the correct order of packets and synchronize audio and video streams.
- **Jitter compensation:** RTP works with jitter buffers to handle network delays and variations in packet arrival times, ensuring smooth playback.
- **No built-in encryption:** RTP itself does not include security features, but Secure RTP (SRTP) is used to provide encryption and authentication for secure communications.

RTP is a core protocol in real-time communication applications, ensuring smooth and synchronized media delivery across networks.

---

See also:

- [[Secure real-time transport protocol (SRTP)]]
- [[Voice over internet protocol (VoIP)]]