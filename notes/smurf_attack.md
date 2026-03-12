# Smurf attack

A smurf attack is a network attack that is performed when an attacker sniffs an authorized user’s IP address and floods it with packets. Once the spoofed packet reaches the broadcast address, it is sent to all of the devices and servers on the network.

In a smurf attack, IP spoofing is combined with a denial of service (DoS) technique to flood the network with unwanted traffic. For example, the spoofed packet could include an [[internet_control_message_protocol_(icmp)]] ping. As you learned earlier, ICMP is used to troubleshoot a network. But if too many ICMP messages are transmitted, the ICMP echo responses overwhelm the servers on the network and they shut down. This creates a denial of service and can bring an organization’s operations to a halt.

An important way to protect against a smurf attack is to use an advanced [[firewall|firewall]] that can monitor any unusual traffic on the network. Most [[next-generation_firewall_(ngfw)|next_generation_firewalls_(ngfws)]] include features that detect network anomalies to ensure that oversized broadcasts are detected before they have a chance to bring down the network.

---

See also:

- [[denial_of_service_(dos)]]
- [[internet_control_message_protocol_(icmp)]]
- [[amplification_attack]]
- [[reflection_attack]]
