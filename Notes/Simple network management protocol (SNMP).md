
# Simple network management protocol (SNMP)

[[🏷️Network protocol]]

Simple network management protocol (SNMP) is a protocol used for monitoring and managing network devices such as routers, switches, servers, and printers. It allows network administrators to collect performance data, detect faults, and configure devices remotely.

- **Port number and protocol type:** SNMP operates over port 161 using UDP for general communication, and port 162 using UDP for receiving trap messages.
- **Management Information Base (MIB):** SNMP uses a structured database called the Management Information Base (MIB), which defines the set of variables that devices can report on or be configured with.
- **Object Identifier (OID):** Each managed object within the MIB is identified by a unique Object Identifier (OID), which provides a hierarchical way to access device-specific data.
- **SNMP versions:** Different versions include SNMPv1, SNMPv2c, and SNMPv3, with SNMPv3 offering enhanced security features like encryption and authentication.
- **Trap messages:** SNMP agents send alerts known as **traps** to management systems when certain predefined conditions occur, helping with real-time network monitoring.

SNMP is widely used in enterprise networks for automated device management, monitoring network health, and troubleshooting performance issues.

---

See also:

- [[Management information base (MIB)]]
- [[Object identifier (OID)]]
- [[Internet Control Message Protocol (ICMP)]]