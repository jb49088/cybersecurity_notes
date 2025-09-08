# Bridge protocol data unit (BPDU)

A bridge protocol data unit (BPDU) is a type of data message used in networking, specifically in the Spanning Tree Protocol (STP), to maintain a loop-free topology in Ethernet networks. BPDUs are exchanged between network bridges (switches) to help them determine the best path for data traffic and avoid network loops, which can cause broadcast storms and network failures.

BPDUs contain information about the network topology, such as:

- Root Bridge Identifier: The switch with the lowest bridge ID, considered the "root" of the network.

- Path Cost: The cumulative cost to reach the root bridge.

- Sender’s Bridge ID: Identifies the switch sending the BPDU.

- Port Identifier: Identifies the port from which the BPDU was sent.

There are two main types of BPDUs:

- Configuration BPDU: Used for the Spanning Tree Protocol to share information about the network topology and elect the root bridge.

- Topology Change Notification BPDU (TCN): Indicates that the network topology has changed and a reconfiguration of the spanning tree is needed.

BPDU communication ensures that network switches can detect and avoid loops, providing network resilience and stability.

---

See also:




