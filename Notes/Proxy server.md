
# Proxy server

[[🏷️Networking]]

A proxy server acts as an intermediary between users and external networks, receiving and forwarding user requests on their behalf. This mechanism is widely used to enhance security, manage traffic, and provide additional functionality such as caching, access control, URL filtering, and content scanning.

Proxies come in two main forms:

- **Explicit proxies**: Require applications or users to be configured to use the proxy.
- **Transparent proxies**: Operate invisibly to the user, requiring no configuration on the client side.

Proxies can be categorized as follows:

- **Application proxies**: Most proxies are application-specific, meaning they understand the applications they serve, such as HTTP, HTTPS, or FTP. These proxies are critical for providing application-layer security and optimizing specific protocols. Some proxies are multipurpose, supporting several applications, while simpler forms like NAT (Network Address Translation) operate only at the network level.
- **Forward proxy**: An internal proxy designed to manage and control user access to external networks like the Internet. It is often used for web filtering, content monitoring, and caching to improve performance and security.

![[Diagram 1.00]]

- **Reverse proxy**: Focuses on inbound traffic, directing it from external networks to internal servers. This type of proxy enhances security by obscuring internal server details and balancing traffic loads among multiple servers.

![[Diagram 1.03]]

- **Open proxy**: A third-party proxy that is publicly accessible and often uncontrolled. These proxies are frequently exploited to bypass security controls, creating significant security risks.

![[Diagram 1.04]]

Proxies are essential tools in modern network architectures, offering versatility in securing, optimizing, and monitoring network communications.

---

See also:

- [[Network address translation (NAT)]]
- [[Load balancer]]
- [[Content filtering]]