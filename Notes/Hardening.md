
# Hardening

Hardening refers to the process of securing systems, devices, and environments by reducing vulnerabilities and configuring them beyond their default settings. This involves applying tailored guidelines and updates to ensure optimal security, often using guides from manufacturers or trusted online sources.

- **Mobile devices:** Always-connected technologies like phones and tablets require robust security measures. Regular updates, including bug fixes and security patches, are essential to prevent vulnerabilities. Segmentation can separate company and personal data for enhanced protection, and devices should be managed using a Mobile Device Manager (MDM).
- **Workstations:** Desktops and laptops running Windows, macOS, or Linux need continuous monitoring and updates for their operating systems, applications, and firmware. Automated patching is often integrated into existing processes, and policy management systems like Active Directory Group Policy help enforce security. Removing unnecessary software reduces potential attack vectors.
- **Network infrastructure devices:** Devices such as switches and routers, which form the backbone of connectivity, require careful configuration. Authentication defaults must be changed, and security updates from manufacturers should be applied. These purpose-built devices often have embedded operating systems with limited access to reduce risks.
- **Cloud infrastructure:** Securing cloud management workstations is critical, as they control access to cloud environments. Enforcing least privilege for services, network settings, and applications helps minimize exposure. Endpoint Detection and Response (EDR) ensures devices accessing the cloud are secure, while regular backups, including cloud-to-cloud (C2C), protect against data loss.
- **Servers:** Servers, whether running Windows, Linux, or other platforms, require consistent updates, including security patches and service packs. Enforcing strong password policies and limiting user account privileges improves security. Network access should be restricted to essential services, and anti-virus and anti-malware tools should be employed for ongoing monitoring.
- **SCADA/ICS systems:** Supervisory Control and Data Acquisition (SCADA) and Industrial Control Systems (ICS) manage critical infrastructure like power plants and manufacturing. These systems must be heavily segmented to prevent external access while enabling real-time control and monitoring through distributed control systems.
- **Embedded systems:** Devices designed for specific functions, such as smart TVs or industrial controllers, often have limited update capabilities. Applying security patches promptly addresses vulnerabilities. Using segmentation and firewalls prevents unauthorized access and potential exploitation.
- **RTOS (Real-Time Operating Systems):** Found in industrial equipment, automobiles, and military environments, RTOS requires isolation to ensure uninterrupted operations. Running only essential services and securing communications with host-based firewalls minimizes risks.
- **IoT devices:** Internet of Things (IoT) devices, including smart home systems and wearable technology, often come with weak default passwords. Changing these defaults and applying updates promptly is crucial. Segmenting IoT devices on a separate VLAN enhances their security and prevents unauthorized access.

---

See also:

- [[Software update]]
- [[Configuration enforcement]]
- [[Endpoint]]