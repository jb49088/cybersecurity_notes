
# Border gateway protocol (BGP)

[[🏷️Network protocol]]

Border gateway protocol (BGP) is the primary routing protocol used to exchange routing information and determine the best paths between autonomous systems (AS) on the internet. As the backbone of global internet routing, BGP enables data to travel efficiently across multiple networks by selecting optimal paths based on routing policies and rules.

- **Path vector protocol:** BGP uses a path vector mechanism to determine the best routes, maintaining a record of the AS paths that data must traverse.
- **Autonomous systems:** Each AS is a network or group of networks managed by a single organization with defined routing policies. BGP enables communication between these systems.
- **Routing decisions:** Decisions are based on policies, not just shortest paths, allowing network administrators to control traffic flows.
- **Internal vs. External BGP:** Internal BGP (iBGP) operates within an AS, while External BGP (eBGP) manages communication between different AS.
- **Convergence:** BGP updates ensure that routers across the internet have consistent and accurate information about available paths.

BGP is a critical component of the internet's infrastructure, but its complexity and reliance on trust between AS make it a potential target for attacks like route hijacking and prefix misconfiguration. As a result, measures like Resource Public Key Infrastructure (RPKI) are used to improve the security and reliability of BGP routing.

---

See also:

