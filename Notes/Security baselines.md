
# Security baselines

Security baselines establish the foundational security requirements for an application or environment, ensuring consistency and protection across all instances. They define critical parameters such as firewall settings, patch levels, and operating system file versions. These baselines are vital for maintaining a secure environment and often require frequent updates to address emerging threats.

Integrity measurements play a key role in ensuring adherence to security baselines. Regular checks compare the current state of the system against documented baselines. Any deviation is promptly addressed to maintain the integrity and security of the environment.

Creating security baselines involves developing a set of foundational security policies. Many baselines are provided by manufacturers, including application developers, operating system manufacturers, and appliance vendors. For example, Windows 10 offers over 3,000 group policy settings, though only a subset pertains to security. These baselines serve as a reference point to ensure that all instances meet required security standards.

Deploying baselines involves translating established policies into actionable configurations. This is typically managed through centrally administered consoles, leveraging deployment mechanisms like Active Directory Group Policy or Mobile Device Management (MDM) tools. Automation is essential for scaling the deployment to hundreds or thousands of devices efficiently.

Maintaining security baselines is an ongoing process. While many baselines remain static as best practices, others require updates in response to new vulnerabilities, application updates, or operating system changes. Regular testing ensures compatibility and avoids conflicts, especially in complex enterprise environments where differing baselines might occasionally contradict each other.

---

See also:

- [[Anomaly-based detection]]