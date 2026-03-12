# Netcat

Netcat is a lightweight command-line networking utility often referred to as the Swiss army knife of networking, capable of reading and writing data across network connections using TCP or UDP. It is one of the most versatile and widely used tools in both system administration and offensive security due to its simplicity, portability, and broad range of applications.

- **Basic connectivity:** At its core, Netcat opens raw TCP or UDP connections between two machines, making it useful for testing connectivity, transferring data, and debugging network services. A basic connection is established with `nc <target> <port>`, while a listener is started with `nc -lvnp <port>`.
- **Reverse shell listener:** Netcat is the most commonly used tool for catching reverse shells. Running a listener with `nc -lvnp 4444` instructs Netcat to listen on port 4444 and print any incoming connection to the terminal, providing an interactive shell when a reverse shell payload connects back.
- **Bind shell creation:** Netcat can create a bind shell by combining a listener with the -e flag to execute a shell on connection, though the -e flag is disabled in some distributions such as Netcat OpenBSD for security reasons. Alternative methods using named pipes can achieve the same result on restricted versions.
- **File transfer:** Netcat can transfer files between machines by piping file contents into a Netcat connection on one end and redirecting the output to a file on the other, providing a quick and dependency-free method of moving files during an engagement when other transfer methods are unavailable.
- **Port scanning:** Netcat can perform basic port scanning using the -z flag, which attempts connections without sending data, making it a lightweight alternative to more fully featured scanners when only basic port availability checking is needed.
- **Ncat and alternatives:** Ncat, distributed as part of the Nmap project, is a modernized reimplementation of Netcat that adds SSL support, access control, and broker mode. Socat is another powerful alternative that extends Netcat's capabilities significantly, supporting encrypted connections and more complex relay configurations.
- **Availability on targets:** Because Netcat is a standard utility present on many Linux systems, it is frequently used not just by attackers on their own machines but as a tool already available on compromised targets for pivoting, transferring files, or establishing additional connections.

Netcat's combination of simplicity and flexibility makes it an indispensable tool in offensive security, present in nearly every penetration tester's workflow and essential knowledge for anyone working toward bug bounty hunting or CTF competitions.

---

See also:

- [[Reverse shell]]
- [[Bind shell]]
- [[Remote code execution (RCE)]]
- [[Nmap]]
