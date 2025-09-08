
# Classless Inter-Domain Routing (CIDR)

CIDR, or Classless Inter-Domain Routing, is a method for allocating IP addresses and routing Internet Protocol packets. It allows for more efficient use of IP addresses compared to the older classful network design.

CIDR notation is a way to specify IP addresses and their associated network prefixes. It’s written in the format `IP address/Prefix length`. For example, `203.0.113.0/26`.

- **IP Address:** This is the unique identifier assigned to each device on a network.
- **Prefix Length:** The number after the slash (`/26` in this case) indicates how many bits of the IP address are part of the network portion. The remaining bits are available for host addresses within that network.

**Example: 203.0.113.0/26**

- The network address is `203.0.113.0`.
- The `/26` means that the first 26 bits (or the first three octets and the first two bits of the fourth octet: `203.0.113.00xxxxxx`) are the network portion. The remaining 6 bits in the fourth octet are used for device addresses within that network.

**IP Address Range in a /26 Subnet:**

- In `203.0.113.0/26`, the IP addresses range from `203.0.113.0` to `203.0.113.63`.
- This range includes 64 addresses: the first address (`203.0.113.0`) is reserved as the network address, and the last address (`203.0.113.63`) is typically reserved as the broadcast address.
- The remaining addresses (`203.0.113.1` to `203.0.113.62`) can be assigned to devices within the network.

**Example in Context:** If a company assigns the range `203.0.113.0/26` to its branch office:

- Each device in that office, such as computers or printers, will have an IP address within this range, like `203.0.113.15`.
- This setup allows for up to 62 devices to be assigned unique IP addresses within this network.