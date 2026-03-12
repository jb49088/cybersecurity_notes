# Bind shell

A bind shell is a type of remote access technique where a listener is opened directly on the target machine, and the attacker connects inward to that listener to receive shell access. It is the conceptual opposite of a reverse shell, where the target initiates the connection outward to the attacker.

- **How it works:** After achieving code execution on a target, the attacker deploys a payload that instructs the target to open a port and bind a shell to it, meaning any connection made to that port receives interactive shell access. The attacker then connects to that port from their own machine to interact with the shell.
- **Why reverse shells are preferred:** Bind shells are frequently blocked by egress and ingress firewall rules that restrict unsolicited inbound connections to the target. Because the attacker must initiate the connection to the target, any firewall or network control between them that drops unexpected inbound traffic will prevent the bind shell from being reached, making reverse shells a more reliable choice in most real-world scenarios.
- **When bind shells are useful:** Bind shells become preferable in situations where the attacker cannot receive inbound connections on their own machine, such as when operating behind NAT or a restrictive firewall on their end. If the target is directly reachable but the attacker's machine is not, a bind shell avoids the need for the attacker to expose a listener.
- **Port selection:** The port chosen for the bind shell listener on the target can influence detectability. Using commonly expected ports may help blend in with legitimate traffic, while unusual high-numbered ports may attract less immediate attention from automated monitoring depending on the environment.
- **Detection:** Bind shells are detectable through network monitoring tools and host-based intrusion detection systems watching for unexpected listening ports on a machine. Commands like `netstat` or `ss` will reveal open listeners, making bind shells more easily discoverable during incident response than reverse shells that leave no persistent listener on the target.

Bind shells are a foundational concept in understanding remote access techniques, and while reverse shells are more commonly used in practice, understanding both models and their respective tradeoffs is essential for anyone working in offensive security or network defense.

---

See also:

- [[Reverse shell]]
- [[Remote code execution (RCE)]]
- [[Netcat]]
- [[Firewall]]
- [[Network address translation (NAT)]]
