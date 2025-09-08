
# Deauthentication attack

[[🏷️Network attack]]

A Deauthentication attack is a type of denial-of-service (DoS) attack that targets wireless networks by exploiting the deauthentication process in the 802.11 Wi-Fi protocol. The attacker sends deauthentication frames, pretending to be the access point (AP) or client, which forces connected devices to disconnect from the network. This disruption can cause service outages, facilitate other attacks like on-path attacks, and potentially be used for credential harvesting or password cracking.

Deauthentication attacks work by sending deauthentication packets to a device, causing it to believe that the connection with the AP is no longer valid. As a result, the client is forced to disconnect and reconnect, during which time sensitive information, such as WPA/WPA2 handshakes, can be captured. This captured data can then be used for brute-forcing or cracking the network's security.

Common uses of Deauthentication attacks include:

- **Denial of Service**: Disrupting the connection between legitimate users and the wireless network.
- **Wi-Fi Cracking**: Capturing WPA/WPA2 handshakes during client reconnection attempts to crack the Wi-Fi password.
- **On-path attacks**: Intercepting communications between the client and AP by impersonating the AP during the reconnection phase.

To mitigate Deauthentication attacks, organizations can enable 802.11w (Management Frame Protection) to secure management frames and prevent spoofing. Implementing WPA3 encryption strengthens protection against such attacks while improving overall network security. Monitoring wireless networks for frequent deauthentication attempts allows for early detection and response. Additionally, limiting device connections and using MAC address filtering through access control measures can further reduce the risk of successful attacks.

---

See also:

- [[Denial of service (DoS)]]
- [[IEEE 802.11 (Wi-Fi)]]
- [[Access point (AP)]]
- [[On-path attack]]
- [[Wi-Fi Protected Access III (WPA3)]]
