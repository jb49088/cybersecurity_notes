
# Software-defined networking (SDN)

Software-defined networking (SDN) is an approach to networking that separates the data plane, control plane, and management plane to provide more flexibility, scalability, and centralized control over the network infrastructure. This separation allows for the centralization of network management, which is ideal for dynamic environments like the cloud.

- **Infrastructure layer / Data plane:** This layer processes network frames and packets, performing tasks such as forwarding, trunking, encrypting, and NAT (Network Address Translation). It handles the actual data transmission within the network.
- **Control layer / Control plane:** This layer manages the data plane’s actions. It includes tasks like managing routing tables, session tables, and NAT tables, as well as handling dynamic routing protocol updates that help determine the most efficient path for network traffic.
- **Application layer / Management plane:** This layer is responsible for configuring and managing the devices. It is typically accessed through interfaces such as SSH, a web browser, or APIs to control and automate network functions.

SDN enhances network flexibility by allowing centralized control, making it especially well-suited for cloud environments and large-scale infrastructures.

---

See also:

- [[Cloud Service Provider (CSP)]]
- [[Cloud computing]]