
# Ring Topology

[[🏷️Network topology]]

In a ring topology, each computer connects to two other computers, joining them in a circle and creating a unidirectional path where messages move from workstation to workstation. Each entity participating in the ring reads a message and then regenerates it and hands it to its neighbor on a different network cable. See Figure 2.28 for an example of a ring topology.

- **Figure 2.28** The ring topology
![[Image 2.28.png]]

The ring makes it difficult to add new computers. Unlike a star topology network, a ring topology network will go down if one entity is removed from the ring. Physical ring topology systems rarely exist anymore, mainly because the hardware involved was fairly expensive and the fault tolerance was very low.

> [!info] Note
> You might have heard of an older network architecture called Token Ring. Contrary to its name, it does not use a physical ring. It actually uses a physical star topology, but the traffic flows in a logical ring from one computer to the next.