Based off the formatting of these pages, I want you to write me pages when I give you a term. I don't like nested bullet points, and notice the titles with lack of capitalization

# Site survey

Site surveys are crucial for understanding the current wireless environment and ensuring effective network deployment. The goal is to evaluate existing conditions and make informed decisions to optimize wireless coverage, avoid interference, and plan for future needs.

- **Determine existing wireless landscape:** Start by sampling the existing wireless spectrum to understand the current state of wireless communication in the area.
- **Identify existing access points:** It’s important to locate and assess existing access points, especially if you don’t have control over all of them. This will help you account for any limitations or potential conflicts.
- **Work around existing frequencies:** Consider the layout and plan accordingly for potential interference. Ensure that the frequencies used by your network will not overlap with others in the vicinity, to maintain clear and reliable signal transmission.
- **Plan for ongoing site surveys:** The wireless environment will evolve over time, so it’s important to plan for periodic site surveys. Changes in the environment, such as new access points or construction, can impact the network's performance.
- **Heat maps:** Use heat maps to visualize wireless signal strengths across the area. These maps can help identify areas with weak signal coverage and guide improvements to ensure complete coverage.

By conducting regular site surveys, you ensure that the wireless network remains efficient and effective, adapting to changing conditions and maintaining optimal performance.

---

See also:

- [[IEEE 802.11 (Wi-Fi)]]
- [[Wireless Local Area Network (WLAN)]]
- [[Access point (AP)]]

# Due diligence

Due diligence is the process of thoroughly investigating and assessing risks before making a business decision. in cybersecurity, due diligence ensures that organizations evaluate security practices, compliance requirements, and potential vulnerabilities before engaging with vendors, acquiring technology, or entering partnerships.

- **Risk assessment:** Identifies potential threats and vulnerabilities in business operations, third-party vendors, or new technology.
- **Compliance verification:** Ensures adherence to industry regulations and security standards such as GDPR, HIPAA, or ISO 27001.
- **Vendor security evaluation:** Reviews the cybersecurity posture of third-party service providers to prevent supply chain attacks.
- **Financial and operational review:** Assesses financial stability and operational risks that could impact security and business continuity.
- **Ongoing monitoring:** Due diligence is not a one-time process but requires continuous evaluation to adapt to evolving risks.

By conducting due diligence, organizations can make informed decisions, mitigate security risks, and maintain compliance with legal and regulatory requirements.

---

See also:

- [[Supply chain analysis]]

# Cyber threat intelligence (CTI)

Cyber threat intelligence (CTI) is the process of collecting, analyzing, and applying information about cyber threats to improve security decision-making. CTI helps organizations anticipate, detect, and respond to threats more effectively by understanding attacker tactics, motives, and capabilities.

- **Threat identification:** Gathers intelligence on threat actors, malware, vulnerabilities, and attack patterns.
- **Proactive defense:** Enables organizations to anticipate threats and implement protective measures before an attack occurs.
- **Strategic, operational, tactical intelligence:** CTI is categorized into different levels, from high-level strategic insights to detailed technical indicators.
- **Indicators of compromise (IOCs):** Provides data on malicious activities such as IP addresses, domains, or file hashes used by attackers.
- **Integration with security tools:** Enhances SIEMs, firewalls, and endpoint security solutions with actionable intelligence.

CTI strengthens an organization’s security posture by providing real-time insights into emerging threats, helping to mitigate risks before they cause harm.

---

See also:

- [[Threat intelligence]]
- [[Tactics, techniques, and procedures (TTP)]]
- [[Indicators of compromise (IoC)]]
- [[Structured threat information expression (STIX)]]
- [[Trusted Automated eXchange of Indicator Information (TAXII)]]

# Single loss expectancy (SLE)

Single loss expectancy (SLE) is a metric used in risk management to estimate the potential financial loss associated with a single occurrence of a specific risk or threat. SLE helps organizations assess the cost of an incident should it happen, providing a basis for calculating broader financial impacts like the Annual Loss Expectancy (ALE).

The SLE is calculated by determining the **cost** of a single loss event, which could include factors like repair costs, recovery costs, lost revenue, and other related expenses. The formula for calculating SLE is:

**SLE = Asset Value × Exposure Factor**

- **Asset Value** refers to the monetary value of the asset at risk.
- **Exposure Factor** is the percentage of the asset's value that would be lost in the event of a risk occurring.

Understanding SLE is essential for organizations to assess the financial impact of specific threats and determine the appropriate security measures to mitigate those risks. When combined with the **Annual Rate of Occurrence (ARO)**, the SLE helps organizations calculate the **Annual Loss Expectancy (ALE)**, which provides a clear financial estimate of the potential losses from a given risk over the course of a year.

---

See also:

- [[Annual loss expectancy (ALE)]]

# Incident response plan (IRP)

An incident response plan (IRP) is a structured approach to handling and managing security incidents, cyberattacks, and data breaches. The goal of an IRP is to mitigate damage, reduce recovery time and costs, and minimize the impact on business operations. A well-prepared IRP ensures that organizations can effectively respond to incidents in a coordinated and efficient manner.

An effective IRP typically includes the following key elements:

- **Preparation**: Establishing a strong security foundation, including creating the IRP, assembling an incident response team, and conducting training and simulations.
- **Identification**: Detecting and identifying potential incidents. This involves monitoring systems for signs of unusual activity, analyzing logs, and validating alerts.
- **Containment**: Taking immediate action to limit the impact of the incident, such as isolating affected systems, blocking malicious traffic, or applying temporary fixes.
- **Eradication**: Removing the root cause of the incident, such as malware or unauthorized access, and addressing any vulnerabilities that allowed the incident to occur.
- **Recovery**: Restoring systems to normal operations, verifying that they are secure, and monitoring for any signs of lingering issues.
- **Lessons learned**: Conducting a post-incident review to analyze the effectiveness of the response, identify areas for improvement, and update the IRP accordingly.

A robust incident response plan (IRP) is essential for minimizing disruption during security incidents, protecting sensitive data and critical systems, ensuring compliance with industry regulations, and maintaining customer trust and organizational reputation. By investing in a well-designed, regularly updated IRP, organizations can effectively mitigate risks and reduce the impact of cyber threats.

---

See also:

- [[Incident]]
- [[Disaster recovery plan (DRP)]]
- [[Business continuity plan (BCP)]]

# Universal serial bus (USB)

Universal serial bus (USB) is a widely used standard for connecting devices to computers and other electronic systems. It defines the cables, connectors, and protocols for data transfer and power supply between devices. Initially developed in the mid-1990s, USB has become the standard interface for a wide range of peripherals, including keyboards, mice, printers, external storage devices, smartphones, and more.

USB allows for plug-and-play functionality, enabling devices to be easily connected or disconnected without restarting the computer. It supports both data transfer and power delivery, making it a versatile solution for various applications. There are different versions of USB, each offering faster speeds and improved capabilities:

- USB 1.1 and 2.0: Older versions, with USB 2.0 offering data transfer rates of up to 480 Mbps.

- USB 3.x: Introduced higher transfer speeds, with USB 3.0 offering up to 5 Gbps and USB 3.1 reaching 10 Gbps.

- USB4: The latest version, offering speeds of up to 40 Gbps, while also supporting Thunderbolt 3 and USB-C connectors.

USB has become a crucial part of everyday computing, providing a universal and reliable way to connect and power devices across many different platforms.

---

See also:

- [[Peripheral devices]]

# Extensible authentication protocol (EAP)

Extensible authentication protocol (EAP) is a flexible authentication framework used in network access protocols. Rather than being a single authentication method, EAP provides a structure that supports various authentication mechanisms, allowing customization and extensibility.

- **Authentication Framework**: EAP defines the architecture for authentication but does not specify a single method, enabling support for multiple approaches.
- **Custom EAP Methods**: Vendors and manufacturers can develop their own EAP methods, allowing integration of proprietary authentication techniques.
- **Integration with Standards**: EAP operates in compliance with RFC standards, ensuring interoperability across devices and platforms.
- **802.1X Integration**: EAP works seamlessly with the IEEE 802.1X standard to control network access. It ensures that devices are authenticated before gaining access to the network.

By supporting diverse authentication methods and working alongside protocols like 802.1X, EAP is widely used in wireless and wired network environments to enhance security and flexibility.

---

See also:

- [[IEEE 802.1X]]
- [[Lightweight extensible authentication protocol (LEAP)]]
- [[Protected extensible authentication protocol (PEAP)]]

# Load balancer

A load balancer is a device or software solution that distributes incoming traffic across multiple servers to ensure optimal utilization, efficiency, and reliability of resources. The load balancer makes sure that no single server becomes overwhelmed with too much traffic, providing a smoother experience for end users. It works invisibly to the user, who doesn’t notice the distribution of requests among multiple servers.

In large-scale environments such as web server farms or database farms, load balancers are crucial for ensuring the system remains responsive and operational. They also contribute to **fault tolerance** by ensuring that server outages do not disrupt service, and they can quickly shift traffic to operational servers with minimal downtime.

There are two main types of load balancing configurations:

- **Active/active load balancing**: All servers in the pool are actively handling traffic, which provides better resource utilization and scalability. Additional features like TCP offload, SSL offload, caching, and prioritization can further optimize performance and speed.
    
- **Active/passive load balancing**: Some servers are designated as active and handle all incoming traffic, while passive servers remain on standby. If an active server fails, one of the passive servers automatically takes its place, minimizing service disruptions.

Load balancers are fundamental for high-availability and scalability in modern network infrastructures.

---

See also:

- [[High availability (HA)]]
- [[Scalability]]