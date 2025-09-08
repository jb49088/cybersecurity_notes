
# Distributed Denial of Service (DDoS)

[[🏷️Network attack]]

A Distributed Denial of Service (DDoS) attack is a type of cyberattack where multiple compromised systems (often referred to as a "botnet") are used to flood a target system or network with an overwhelming amount of traffic. The goal of a DDoS attack is to exhaust the target's resources—such as bandwidth, server capacity, or application performance—causing the target to become slow, unreliable, or completely unavailable to legitimate users.

Unlike a standard Denial of Service (DoS) attack, which originates from a single machine, a DDoS attack uses a distributed network of compromised devices, making it much harder to stop and mitigate. These devices are typically infected with malware that allows attackers to control them remotely, often without the knowledge of the device owners.

DDoS attacks can take many forms, including:

- **Volume-Based Attacks**: The attacker sends an overwhelming amount of traffic to consume the bandwidth of the target. Common methods include UDP floods, ICMP floods, and other traffic injection techniques.
  <br>
- **Protocol Attacks**: These attacks target the network layer and aim to exhaust server resources or intermediate devices like firewalls. Examples include SYN floods and Ping of Death attacks.
  <br>
- **Application Layer Attacks**: These attacks target the web application layer by sending seemingly legitimate requests that consume significant server resources. Examples include HTTP floods or slowloris attacks.

DDoS attacks are often used as a smokescreen for other types of cybercrime, such as data breaches or ransomware attacks. Attackers may also use DDoS as a form of protest or extortion, demanding payment in exchange for ceasing the attack.

---

See also:

- [[Denial of service (DoS)]]
- [[ICMP Flood]]
