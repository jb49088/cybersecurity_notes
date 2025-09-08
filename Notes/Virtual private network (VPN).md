
# Virtual private network (VPN)

A Virtual private network (VPN) is a technology that facilitates encrypted, private communication over a public network such as the internet. By employing encapsulation and encryption, VPNs ensure data confidentiality, secure remote access, and connect geographically dispersed networks. Encapsulation wraps data with additional headers and trailers, effectively creating an encrypted "tunnel" through which information travels securely. This process safeguards sensitive data, making VPNs indispensable for businesses, remote workers, and anyone aiming to protect their online activity.

At the core of a VPN setup is the VPN concentrator, a device or software solution responsible for encryption, decryption, and encapsulation of data. These concentrators are often integrated with firewalls and can be implemented using specialized cryptographic hardware or software-based options. Client software, sometimes built into operating systems, enables devices to establish secure connections to the concentrator. Together, encryption and encapsulation ensure that data remains private and intact during its journey across untrusted public networks.

The primary function of a VPN is to maintain data privacy across the internet. Encapsulation creates the secure tunnel, while encryption secures the transmitted data, ensuring only authorized recipients can access the original information. Upon delivery, the encapsulated headers and trailers are removed to restore the data to its original form, ensuring confidentiality and reliability.

## SSL/TLS VPN

An SSL/TLS VPN leverages the Secure Sockets Layer (SSL) or Transport Layer Security (TLS) protocols, operating over TCP port 443. These protocols enable VPNs to establish secure connections while maintaining compatibility with existing firewalls, minimizing connectivity issues. SSL/TLS VPNs are commonly used for remote access due to their simplicity and minimal setup requirements. Unlike traditional VPNs, SSL/TLS VPNs do not require extensive configuration or large client software installations.

![[Image 2.33.png]]

Authentication for SSL/TLS VPNs is user-friendly, often bypassing the need for digital certificates or shared passwords required by IPsec-based systems. They are highly versatile, functioning through web browsers or lightweight VPN clients on various operating systems. These VPNs support on-demand access for remote devices, and some configurations enable always-on connectivity, providing uninterrupted secure communication.

## Site-to-Site IPsec VPN

Site-to-site IPsec VPNs are designed to connect entire networks, such as linking branch offices to a central headquarters. These VPNs rely heavily on encapsulation to create persistent encrypted tunnels that facilitate seamless communication between networks. They are typically always-on or nearly always active, ensuring continuous and reliable connectivity.

![[Image 2.68.png]]

Firewalls frequently serve as VPN concentrators in site-to-site configurations, making deployment more cost-effective and straightforward, as organizations often already have firewalls in place. The integration of encapsulation and encryption in these VPNs ensures secure and efficient inter-network communication, even over public networks.

---

See also:

- [[Encapsulation]]
- [[Encryption]]
- [[Secure sockets layer (SSL)]]
- [[Transport Layer Security (TLS)]]
- [[Internet protocol security (IPsec)]]
- [[Software-defined networking (SDN)]]