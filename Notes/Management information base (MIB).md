
# Management information base (MIB)

A management information base (MIB) is a collection of objects or variables that are managed by network management protocols like SNMP (Simple Network Management Protocol). It serves as a structured database that defines the data points, metrics, and statistics of devices on a network, such as routers, switches, servers, and other networked devices. The MIB organizes this information into a hierarchical format and allows network administrators to access and manage device data effectively.

Each object in a MIB is identified by an object identifier (OID), which acts as a unique reference to specific data points. These objects can represent a wide range of information, such as system uptime, CPU utilization, interface status, and network traffic statistics. The MIB structure is standardized, ensuring compatibility across different network devices and vendors.

Key features of MIB:

- **Hierarchical structure**: The MIB is organized in a tree-like structure, where each level represents a different category of information. This structure allows for easy navigation and management of data.
- **Standardization**: MIBs are defined by various standards (e.g., IETF) to ensure interoperability across devices from different vendors.
- **SNMP integration**: MIBs are used in conjunction with SNMP to retrieve or modify information from network devices. SNMP queries access specific OIDs within the MIB to collect real-time data or configure devices.

The MIB acts as a critical component in network management, providing administrators with the tools to monitor, configure, and troubleshoot devices efficiently.

---

See also:

- [[Object identifier (OID)]]
- [[Simple network management protocol (SNMP)]]