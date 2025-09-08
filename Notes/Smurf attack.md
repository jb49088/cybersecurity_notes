
# Smurf attack

[[🏷️Network attack]]

A smurf attack is a network attack that is performed when an attacker sniffs an authorized user’s IP address and floods it with packets. Once the spoofed packet reaches the broadcast address, it is sent to all of the devices and servers on the network.

In a smurf attack, IP spoofing is combined with a denial of service (DoS) technique to flood the network with unwanted traffic. For example, the spoofed packet could include an [[Internet Control Message Protocol (ICMP)]] ping. As you learned earlier, ICMP is used to troubleshoot a network. But if too many ICMP messages are transmitted, the ICMP echo responses overwhelm the servers on the network and they shut down. This creates a denial of service and can bring an organization’s operations to a halt.

An important way to protect against a smurf attack is to use an advanced [[Firewall|firewall]] that can monitor any unusual traffic on the network. Most [[Next-generation firewall (NGFW)|next generation firewalls (NGFWs)]] include features that detect network anomalies to ensure that oversized broadcasts are detected before they have a chance to bring down the network.

---

See also:

- [[Denial of service (DoS)]]
- [[Internet Control Message Protocol (ICMP)]]
- [[Amplification attack]]
- [[Reflection attack]]

