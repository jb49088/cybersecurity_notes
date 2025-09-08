
# ifconfig & traceroute

[[🏷️Linux command]]

The `ifconfig` and `traceroute` commands manage network interfaces and trace the route of network packets in Linux.

The `ifconfig` command will give you the list of all the network interfaces along with the IP addresses, MAC addresses and other information about the interface.

`ifconfig`

There are multiple parameters that can be used, but we’ll work with the basic command here.

![[Image 3.23.png]]

The `traceroute` command is used to trace the route of network packets and determine the path they take to reach a specific destination.

When working with `traceroute`, you can simply specify the IP address, hostname, or domain name of the endpoint.

`traceroute <destination address`

![[Image 3.24.png]]

Now, obviously, `localhost` is just one hop (the network interface itself). You can try this same command with any other domain name or IP address to see all the routers your data packets pass through to reach the destination.