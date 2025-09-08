
# Remotely triggered black hole (RTBH)

Remotely triggered black hole (RTBH) is a network security technique used to mitigate distributed denial-of-service (DDoS) attacks by redirecting malicious traffic away from a targeted network. RTBH allows network administrators to quickly filter or "blackhole" harmful traffic, preventing it from reaching the victim's infrastructure.

RTBH works by dynamically updating the routing tables to drop incoming traffic to specific IP addresses or networks under attack. This technique is typically implemented with the help of upstream service providers or routers that can trigger the blackhole remotely.

- **DDoS mitigation:** Quickly isolates and blocks malicious traffic without requiring manual intervention.
- **Real-time protection:** Enables rapid response to attacks by triggering blackholes as soon as suspicious activity is detected.
- **Traffic redirection:** Redirects malicious traffic to a null route, effectively dropping it from the network.
- **Minimal impact on legitimate traffic:** Only affected IP addresses or subnets are blackholed, ensuring minimal disruption to regular network traffic.
- **Collaboration with ISPs:** Often requires cooperation with internet service providers to implement and trigger blackholes at the network level.

RTBH is a valuable tool for quickly mitigating large-scale DDoS attacks, improving the resilience of networks and preventing service disruptions.

---

See also:

- [[Distributed denial of service (DDoS)]]