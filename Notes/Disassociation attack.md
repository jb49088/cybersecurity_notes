
# Disassociation attack

[[🏷️Network attack]]

Disassociation attacks are a type of denial-of-service (DoS) attack targeting wireless networks. They exploit the management frames in the 802.11 Wi-Fi protocol to forcibly disconnect devices from an access point (AP), disrupting the network connection.

- **How it works:** Attackers send spoofed disassociation frames, tricking devices into believing the AP has disconnected them. This causes devices to drop their connection and repeatedly attempt to reconnect.
- **Unauthenticated frames:** Older Wi-Fi standards do not authenticate management frames, making it easier for attackers to spoof them.
- **Selective targeting:** Attackers can target specific devices by spoofing their MAC addresses, causing disruption to individual users.
- **Impact:** Results in interrupted network access, dropped calls, failed downloads, and degraded performance for users.
- **Mitigation:** WPA3 with Protected Management Frames (PMF) prevents spoofing by encrypting and authenticating management frames. Wireless intrusion detection systems (WIDS) can also help monitor and identify such attacks.

Disassociation attacks highlight the importance of modern Wi-Fi security protocols to ensure stable and secure wireless communication.

---

See also:

- [[Denial of service (DoS)]]
- [[IEEE 802.11 (Wi-Fi)]]
- [[Access point (AP)]]
- [[Wi-Fi Protected Access III (WPA3)]]