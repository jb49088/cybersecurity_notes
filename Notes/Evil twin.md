
# Evil twin

[[🏷️Network attack]]

An evil twin is a type of Wi-Fi spoofing attack where a malicious actor sets up a rogue access point that mimics a legitimate wireless network. The goal is to trick users into connecting to the fake network, allowing the attacker to intercept, monitor, or manipulate their network traffic. Evil twin attacks are often used for credential theft, data interception, or man-in-the-middle attacks.

- **Impersonation**: The rogue access point broadcasts the same name (SSID) as a legitimate network, often in a public space like a coffee shop or airport, making it hard for users to distinguish between the real and fake networks.
- **Traffic interception**: Once users connect to the evil twin, the attacker can monitor and capture sensitive information such as login credentials, emails, and credit card details.
- **On-path attacks**: In some cases, the attacker can alter the traffic between the user and the internet, injecting malicious content or redirecting users to phishing sites.
- **Deauthentication attacks**: An attacker may use deauthentication frames to forcibly disconnect users from the legitimate access point, increasing the likelihood they will connect to the evil twin instead.
- **Protection**: To defend against evil twin attacks, users should avoid connecting to open or unsecured networks, use VPNs to encrypt their traffic, and ensure that any sensitive communications are done over HTTPS.

Evil twin attacks highlight the importance of being cautious when connecting to public Wi-Fi and using encryption methods to protect sensitive data.

---

See also:

- [[Service set identifier (SSID)]]
- [[On-path attack]]
- [[Deauthentication attack]]