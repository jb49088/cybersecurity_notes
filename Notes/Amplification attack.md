
# Amplification attack

[[🏷️Network attack]]

An amplification attack is a type of denial-of-service (DoS) attack where an attacker exploits a vulnerability in a third-party system to increase the volume of traffic directed at a target, overwhelming it. The goal of an amplification attack is to consume the target's resources (such as bandwidth or processing power) with minimal effort from the attacker.

- **Exploiting vulnerable services**: Attackers send a small request to a vulnerable service, which responds with a much larger reply, often in the form of data. Common protocols used in amplification attacks include DNS, NTP, and SNMP.
- **Reflection**: Many amplification attacks involve a reflective element, where the attacker sends requests to a vulnerable server with a forged source IP address (the target's IP address). This causes the server to send responses to the target, amplifying the traffic.
- **Targeting large networks**: Amplification attacks can generate traffic volumes that are much larger than what the attacker could generate on their own, making them effective even with limited resources.
- **Common examples**: DNS amplification attacks, NTP reflection attacks, and Memcached amplification attacks have been used to cause significant disruptions on websites and networks.
- **Mitigation strategies**: Preventing amplification attacks includes securing vulnerable services, configuring firewalls to block malicious traffic, rate-limiting requests, and using anti-DDoS (Distributed Denial of Service) protection services.

Amplification attacks are a serious threat to network security because they can cause significant disruptions while requiring minimal resources from the attacker.

---

See also:

- [[Smurf attack]]