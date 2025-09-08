| Syntax                                          | Description                                                   |
| ----------------------------------------------- | ------------------------------------------------------------- |
| src/ dsthost (host name or IP)                  | Filter by source or destination IP address or host            |
| ether src/ dst host (ethernet host name or IP)  | Ethernet host filtering by source or destination              |
| src/ dstnet (subnet mask in CIDR)               | Filter by subnet                                              |
| tcp/udp src/dst port ( port number)             | Filter TCP or UDP packets by source or destination port       |
| tcp/udp src/dst port range ( port number range) | Filter TCP or UDP packets by source or destination port range |
| ether/ip broadcast                              | Filter for Ethernet or IP broadcasts                          |
| ether/ip multicast                              | Filter for Ethernet or IP multicasts                          |