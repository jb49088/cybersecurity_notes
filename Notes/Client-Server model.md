
# Client-Server

The client-server model (also known as server-based model) is better than the peer-to-peer model for large networks (say, more than 10 computers) that need a more secure environment and centralized control. Server-based networks use one or more dedicated, centralized servers. All administrative functions and resource sharing are performed from this point. This makes it easier to share resources, perform backups, and support an almost unlimited number of users.

This model also offers better security than the peer-to-peer model. However, the server needs more hardware than a typical workstation/server computer in a peer-to-peer resource model. In addition, it requires specialized software (the NOS) to manage the server’s role in the environment. With the addition of a server and the NOS, server-based networks can easily cost more than peer-to-peer resource models. However, for large networks, it’s the only choice. An example of a client-server resource model is shown in Figure 2.25.

- **Figure 2.25** The client-server resource model
![[Image 2.25.png]]

Server-based networks are often known as domains. The key characteristic of a server- based network is that security is centrally administered. When you log into the network, the login request is passed to the server responsible for security, sometimes known as a domain controller. (Microsoft uses the term domain controller, whereas other vendors of server products do not.) This is different from the peer-to-peer model, where each individual workstation validates users. In a peer-to-peer model, if the user jsmith wants to be able to log into different workstations, they need to have a user account set up on each machine. This can quickly become an administrative nightmare! In a domain, all user accounts are stored on the server. User jsmith needs only one account and can log into any of the workstations in the domain.

Client-server resource models are the desired models for companies that are continually growing, that need to support a large environment, or that need centralized security. Server-based networks offer the flexibility to add more resources and clients almost indefinitely into the future. Hardware costs may be higher, but with the centralized administration, managing resources becomes less time consuming. Also, only a few administrators need to be trained, and users are responsible for only their own work environment.

> [!info] Note
> If you are looking for an inexpensive, simple network with little setup required, and there is no need for the company to grow in the future, then the peer-to-peer network is the way to go. If you are looking for a network to support many users (more than 10 computers), strong security, and centralized administration, consider the server- based network your only choice.

Whatever you decide, always take the time to plan your network before installing it. A network is not something you can just throw together. You don’t want to find out a few months down the road that the type of network you chose does not meet the needs of the company—this could be a time-consuming and costly mistake.

