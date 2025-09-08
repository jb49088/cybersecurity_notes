
# Mesh Topology

[[🏷️Network topology]]

The mesh topology is the most complex in terms of physical design. In this topology, each device is connected to every other device (see Figure 2.29). This topology is rarely found in wired LANs, mainly because of the complexity of the cabling. If there are x computers, there will be (x × (x – 1)) ÷ 2 cables in the network. For example, if you have five computers in a mesh network, it will use (5 × (5 – 1)) ÷ 2 = 10 cables. This complexity is compounded when you add another workstation. For example, your 5- computer, 10- cable network will jump to 15 cables if you add just one more computer. Imagine how the person doing the cabling would feel if you told them they had to cable 50 computers in a mesh network—they’d have to come up with (50 × (50 – 1)) ÷ 2 = 1,225 cables! (Not to mention figuring out how to connect them all.)

- **Figure 2.29** The mesh topology
![[Image 2.29.png]]

Because of its design, the physical mesh topology is expensive to install and maintain. Cables must be run from each device to every other device. The advantage you gain is high fault tolerance. With a mesh topology, there will always be a way to get the data from source to destination. The data may not be able to take the direct route, but it can take an alternate, indirect route. For this reason, the mesh topology is often used to connect multiple sites across WAN links. It uses devices called routers to search multiple routes through the mesh and determine the best path. However, the mesh topology does become inefficient with five or more entities because of the number of connections that need to be maintained.