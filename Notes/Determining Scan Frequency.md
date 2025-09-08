
# Determining Scan Frequency

Cybersecurity professionals depend on automation to help them perform their duties in a efficient, effective manner. Vulnerability scanning tools allow the automated scheduling of scans to take the burden off administrators. Image 2.41 shows and example of how these scans might be configured in Tenable's Nessus product. Nessus was one of the first vulnerability scanners on the market and remains widely used today. Administrators may designate a schedule that meets their security, compliance, and business requirements.

![[Image 2.41.png]]

Administrators should configure these scans to provide automated alerting when they detect new vulnerabilities. Many security teams configure their scans to produce automated email reports of scan results, such as the report shown in Image 2.42.

![[Image 2.42.png]]

Many different factors influence how often an organization decides to conduct vulnerability scans against its systems:

- The organization's risk appetite is its willingness to tolerate risk within the environment. If an organization is extremely risk averse, they may choose to conduct scans more frequently to minimize the amount of time between when a vulnerability comes into existence and when it is detected by a scan.
- Regulatory requirements, such as those imposed by the Payment Card Industry Data Security Standard (PCI DSS) or the Federal Information Security Modernization Act (FISMA), may dictate a minimum frequency for vulnerability scans. These requirements may also come from corporate policies.
- Technical constraints may limit the frequency of scanning. For example, the scanning system may only be capable of performing a certain number of scans per day, and organizations may need to adjust scan frequency to ensure that all scans complete successfully.
- Business constraints may limit the organization from conducting resource-intensive vulnerability scans during periods of high business activity to avoid disruption of critical processes.
- Licensing limitations may curtail the bandwidth consumed by the scanner or the number of scans that may be conducted simultaneously.

Cybersecurity professionals must balance each of these considerations when planning a vulnerability scanning program. It is usually wise to begin small and slowly expand the scope and frequency of vulnerability scans over time to avoid overwhelming the scanning infrastructure or enterprise systems.

