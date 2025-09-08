

# Phases of pen tests

Penetration testing is a systematic approach to evaluating the security of systems and networks by simulating attacks. This process is divided into three key phases: reconnaissance, running the test, and cleaning up.

## First Phase∶ Reconnaissance

Penetration tests begin with a reconnaissance phase, where the testers seek to gather as much information as possible about the target organization. In a known-environment test, the testers enter the exercise with significant knowledge, but they still seek to supplement this knowledge with additional techniques. 

**Passive reconnaissance** techniques seek to gather information without directly engaging with the target. There a variety of open source intelligence (OSINT) techniques that fit into the category of passive reconnaissance. Common passive reconnaissance techniques include performing lookups of domain information using DNS and WHOIS queries, performing web searches, reviewing public websites, and similar tactics. 

**Active reconnaissance** techniques directly engage the target in intelligence gathering. These techniques include the use of port scanning to identify open ports on systems, footprinting to identify the operating systems and applications in use, and vulnerability scanning to identify exploitable vulnerabilities.

> [!info] Note
> Know the difference between passive and active reconnaissance techniques. Passive techniques do not directly engage the target, whereas active reconnaissance directly engages the target. 

One common goal of penetration testers is to identify wireless networks that may present a means of gaining access to an internal network of the target without gaining physical access to the facility. Testers use a technique called war driving, where they drive by facilities in a car equipped with high-end antennas and attempt to eavesdrop on or connect to wireless networks. Recently, testers have expanded this approach to the use of drones and unmanned aerial vehicles (UAVs) in a technique known as war flying.

## Second Phase∶ Running the Test

During the penetration test, the testers follow the same process used by attackers. You'll learn more about this process in the discussion of the Cyber Kill Chain in Chapter 14, “Monitoring and Incident Response.” However, you should be familiar with some key phases of the test as you prepare for the exam: 

- **Initial access** occurs when the attacker exploits a vulnerability to gain access to the organization's network.

- **Privilege escalation** uses hacking techniques to shift from the initial access gained by the attacker to more advanced privileges, such as root access on the same system.

- **Pivoting, or lateral movement**, occurs as the attacker uses the initial system compromise to gain access to other systems on the target network.

- Attackers establish **persistence** on compromised networks by installing backdoors and using other mechanisms that will allow them to regain access to the network, even if the initial vulnerability is patched. 

Penetration testers make use of many of the same tools used by real attackers as they perform their work. Exploitation frameworks, such as Metasploit, simplify the use of vulnerabilities by providing a modular approach to configuring and deploying vulnerability exploits.

## Third Phase∶ Cleaning Up

At the conclusion of a penetration test, the testers conduct close-out activities that include presenting their results to management and cleaning up the traces of their work. Testers should remove any tools that they installed on systems as well as any persistence mechanisms that they put in place. The close-out report should provide the target with details on the vulnerabilities discovered during the test and advice on improving the organization's cybersecurity posture.