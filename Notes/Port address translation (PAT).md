
# Port address translation (PAT)

Port address translation (PAT) is a technique used in networking to map multiple private IP addresses to a single public IP address or a few public IP addresses. It is commonly used in conjunction with network address translation (NAT) to allow devices on a local network to access the internet while using a limited number of public IP addresses.

PAT works by modifying the source port number in the IP header of outbound traffic. When multiple devices from the internal network communicate with the internet, PAT assigns a unique port number to each connection, allowing the router or firewall to track which internal device made the request. This ensures that the response from the external server reaches the correct device on the internal network.

- **Conservation of IP addresses:** PAT helps maximize the use of available public IP addresses, allowing multiple internal devices to share a single public IP.
- **Security:** PAT hides the internal network structure, providing an additional layer of security by making internal IP addresses less visible to external entities.
- **Scalability:** By mapping many private IP addresses to one public IP address, PAT enables large networks to access the internet without requiring an individual public IP for each device.

PAT is particularly useful in environments where the number of public IP addresses is limited or expensive, such as in home networks or small-to-medium businesses.

---

See also:

- [[Network address translation (NAT)]]
- [[IP address]]