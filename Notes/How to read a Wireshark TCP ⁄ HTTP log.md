# How to read a Wireshark TCP/HTTP log

In this reading, you’ll learn how to read a Wireshark TCP/HTTP log for network traffic between employee website visitors and the company’s web server. Most network protocol analyzers tools will provide this same information.

## Log entry number and time 

![[Table 1.21|no-link no-title clean]]

This Wireshark TCP log section provided to you starts at log entry number (No.) 47, which is 3.144521 seconds after the logging tool started recording. This indicates that approximately 47 messages were sent and received by the web server in the 3.144521 seconds after starting the log. This rapid traffic speed is why the tool tracks time in milliseconds. 

## Source and destination IP addresses

![[Table 1.22|no-link no-title clean]]

The source and destination columns contain the source IP address of the machine that is sending a packet and the intended destination IP address of the packet. In this log file, the IP address 192.0.2.1 belongs to the company’s web server. The range of IP addresses in 198.51.100.0/24 belong to the employees’ computers. 

> [!Note]
> The statement "The range of IP addresses in 198.51.100.0/24 belong to the employees' computers" refers to the subnet that includes all IP addresses from `198.51.100.0` to `198.51.100.255`. See: [[Classless Inter-Domain Routing (CIDR)]] for more information.

## Protocol type and related information

![[Table 1.23|no-link no-title clean]]

The Protocol column indicates that the packets are being sent using the TCP protocol, which is at the transport layer of the TCP/IP model. In the given log file, you will notice that the protocol will eventually change to HTTP, at the application layer, once the connection to the web server is successfully established.

The Info column provides information about the packet. It lists the source port followed by an arrow → pointing to the destination port. In this case, port 443 belongs to the web server. Port 443 is normally used for encrypted web traffic.

The next data element given in the Info column is part of the three-way handshake process to establish a connection between two machines. In this case, employees are trying to connect to the company’s web server: 

- The \[SYN\] packet is the initial request from an employee visitor trying to connect to a web page hosted on the web server. SYN stands for “synchronize.”   
- The \[SYN, ACK\] packet is the web server’s response to the visitor’s request agreeing to the connection. The server will reserve system resources for the final step of the handshake. SYN, ACK stands for “synchronize acknowledge.”  
- The \[ACK\] packet is the visitor’s machine acknowledging the permission to connect. This is the final step required to make a successful TCP connection. ACK stands for “acknowledge.”

The next few items in the Info column provide more details about the packets. However, this data is not needed to complete this activity. If you would like to learn more about packet properties, please visit [Microsoft’s Introduction to Network Trace Analysis](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/introduction-to-network-trace-analysis-3-tcp-performance/ba-p/3737115).

## Normal website traffic

A normal transaction between a website visitor and the web server would be like:

![[Table 1.24|no-link no-title clean]]

Notice that the handshake process takes a few milliseconds to complete. Then, you can identify the employee’s browser requesting the sales.html webpage using the HTTP protocol at the application level of the TCP/IP model. Followed by the web server responding to the request.

## The Attack

As you learned previously, malicious actors can take advantage of the TCP protocol by flooding a server with SYN packet requests for the first part of the handshake. However, if the number of SYN requests is greater than the server resources available to handle the requests, then the server will become overwhelmed and unable to respond to the requests. This is a network level denial of service (DoS) attack, called a SYN flood attack, that targets network bandwidth to slow traffic. A SYN flood attack simulates a TCP connection and floods the server with SYN packets. A DoS direct attack originates from a single source. A distributed denial of service (DDoS) attack comes from multiple sources, often in different locations, making it more difficult to identify the attacker or attackers. 

![[Image 2.62.png| center |]]

There are two tabs at the bottom of the log file. One is labeled “Color coded TCP log.” If you click on that tab, you will find the server interactions with the attacker’s IP address (203.0.113.0) marked with red highlighting (and the word “red” in column A). 

![[Table 1.25|no-link no-title clean]]

Initially, the attacker’s SYN request is answered normally by the web server (log items 52-54). However, the attacker keeps sending more SYN requests, which is abnormal. At this point, the web server is still able to respond to normal visitor traffic, which is highlighted and labeled as green. An employee visitor with the IP address of 198.51.100.14 successfully completes a SYN/ACK connection handshake with the webserver (log item nos. 55, 56, 58). Then, the employee’s browser requests the sales.html webpage with the GET command and the web server responds (log item no. 60 and 62).

![[Table 1.26|no-link no-title clean]]

In the next 20 rows, the log begins to reflect the struggle the web server is having to keep up with the abnormal number of SYN requests coming in at a rapid pace. The attacker is sending several SYN requests every second. The rows highlighted and labeled yellow are failed communications between legitimate employee website visitors and the web server.

The two types of errors in the logs include:

- An HTTP/1.1 504 Gateway Time-out (text/html) error message. This message is generated by a gateway server that was waiting for a response from the web server. If the web server takes too long to respond, the gateway server will send a timeout error message to the requesting browser.  
- An \[RST, ACK\] packet, which would be sent to the requesting visitor if the \[SYN, ACK\] packet is not received by the web server. RST stands for reset, acknowledge. The visitor will receive a timeout error message in their browser and the connection attempt is dropped. The visitor can refresh their browser to attempt to send a new SYN request.

![[Table 1.27|no-link no-title clean]]

As you scroll through the rest of the log, you will notice the web server stops responding to  legitimate employee visitor traffic. The visitors receive more error messages indicating that they cannot establish or maintain a connection to the web server. From log item number 125 on, the web server stops responding. The only items logged at that point are from the attack. As there is only one IP address attacking the web server, you can assume this is a direct DoS SYN flood attack.


