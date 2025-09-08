
# Pyramid of pain

The Pyramid of Pain is a conceptual framework used in cybersecurity to describe the levels of difficulty that attackers face when trying to bypass detection and mitigation efforts. The model is often used to guide threat hunters, incident responders, and security professionals in identifying and countering various forms of cyber threats based on the complexity of the attack techniques. The pyramid illustrates that as security measures increase in sophistication, the level of difficulty for an attacker also rises.

![[Image 2.89.png|500]]

- **Hash values (bottom level):** At the base of the pyramid are hash values, which are unique identifiers for files. While identifying malicious files by their hash value is relatively easy for defenders, it is also the least painful for attackers to change or evade, making this method less effective over time.
- **IP addresses and domains:** The next level involves identifying malicious IP addresses or domains. Attackers can easily change these to bypass defenses, but monitoring IPs and domains can still provide useful detection.
- **Network/host artifacts:** This level focuses on identifying patterns in network traffic or host behavior. An attacker must modify their tactics or tools to avoid detection, making this level more challenging than simply changing an IP or domain.
- **Tactics, techniques, and procedures (TTPs):** At the higher level of the pyramid, the focus shifts to the attacker’s overall methods, techniques, and procedures. TTPs represent a strategic approach to cyberattacks. Identifying and mitigating TTPs requires deep analysis and proactive monitoring, making it significantly harder for attackers to adjust without altering their entire strategy.
- **Adversary capabilities (top level):** At the top of the pyramid are the full capabilities of an adversary, including their tradecraft, tools, and resources. Countering this requires comprehensive, ongoing analysis and intervention, making it the most painful for attackers to circumvent.
    
The Pyramid of Pain helps security professionals prioritize defense mechanisms and understand the level of effort required to disrupt adversary activities.

---

See also:

- [[Tactics, techniques, and procedures (TTP)]]