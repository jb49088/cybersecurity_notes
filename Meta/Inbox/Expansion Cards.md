# Expansion Cards

An expansion card (also known as an adapter card) is simply a circuit board that you install
into a computer to increase the capabilities of that computer. Expansion cards come in
varying formats for different uses, but the important thing to note is that no matter what
function a card has, the card being installed must match the bus type of the motherboard
into which it is being installed. For example, you can install a PCIe network card into a PCIe
expansion slot only.

For today’s integrated components (those built into the motherboard), you might not need an adapter to achieve the related services, but you will still need to install a driver—a software program that lets the operating system talk to the hardware—to make the integrated devices function with the operating system. Most motherboard manufacturers supply drivers with their motherboards, typically on a flash drive, that contain all the device drivers needed to get the built- in electronics recognized by the operating system. Execution of the driver’s setup program generally results in all components working properly.

## Graphics Card/Video Card

A graphics card (sometimes called video card) is the expansion card that you put into a computer to allow the computer to present information on some kind of display, typically a monitor or a projector. A graphics card is also responsible for converting the data sent to it by the CPU into the pixels, addresses, and other items required for display. Sometimes, video cards can include dedicated chips to perform some of these functions, thus accelerating the speed of display.

You will encounter two classes of graphics cards: onboard cards and add-on cards. Onboard (or integrated) cards are built into the motherboard. As mentioned earlier, you need to install a device driver to get them to work properly, but those often come packaged with the motherboard itself. The upside to an integrated card is that it frees up an expansion slot. The manufacturer can either leave the slot open or design the motherboard and/or case to be smaller. One downside is that if the graphics card fails, you need a new motherboard, or you can install an add- on card. A second downside is that the onboard video cards aren’t typically high-end. Onboard cards generally share system memory with the processor, which limits the quality of graphics one can produce. If the user wants great graphics from a powerful graphics card, then an add-on card is almost always the way to go. For example, serious gamers will always insist on a separate graphics card.

As for add-on cards, PCIe is the preferred expansion slot type. You might be able to find the rare, outdated motherboard that still offers a legacy AGP slot, and you might see some cheap PCI graphics cards, but they are uncommon. The technology on which PCIe was designed performs better for video than those on which AGP and PCI are based. Figure 1.42 shows an example of a PCIe x16 graphics card. The graphics card pictured is 10.6" (270 mm) long and takes up quite a bit of space inside the case. Most cards today have built-in fans like this one does to reduce the chance of overheating.

- **Figure 1.42** A PCIe graphics expansion card
![[Image 1.42.png]]

There is an extensive range of graphics cards available today on the market. For everyday
usage, cards with 1–2 GB of video memory are inexpensive and will do the trick. For gamers, high-end cards with a minimum of 8 GB GDDR5 are recommended. Of course, over the lifespan of this book, that number is sure to increase. (As of this writing, cards with 24 GB GDDR6 are available.) High-end graphics cards can easily cost several thousand dollars.

The main two standards for graphics cards are the NVIDIA GeForce series and the AMD Radeon (formerly ATI Radeon) line. Gamers will debate the pros and cons of each platform but know that you can get a range of performance, from good to phenomenal, from either one. When looking for a card, know how much memory is wanted or needed and how many and which types of video ports (such as HDMI or DisplayPort) are available. 

## Multimedia

The most basic and prolific multimedia adapter is the sound card. Video capture cards also
offer multimedia experiences but are less common than sound cards.

### Sound Cards

Just as there are devices to convert computer signals into printouts and video information, there are devices to convert those signals into sound. These devices are known as sound cards. Although sound cards started out as pluggable adapters, this functionality is one of the most common integrated technologies found on motherboards today. A sound card typically has small, round 1⁄8 jacks on the back of it for connecting microphones, headphones, and speakers as well as other sound equipment. Older sound cards used a DA15 game port, which could be used for either joysticks or Musical Instrument Digital Interface (MIDI) controllers. Figure 1.43 shows an example of a sound card with a DA15 game port.

- **Figure 1.43** A classic sound card
![[Image 1.43.png]]

In our section on graphics cards, we noted that integrated cards have inferior performance to add-on ones, and though the same holds true for sound cards, the difference isn’t quite as drastic. Many of today’s motherboards come equipped with 5.1 or 7.1 analog or digital audio and support other surround sound formats as well. For everyday users and even many gamers, integrated audio is fine.

For users who need extra juice, such as those who produce movies or videos or do other audio/video (A/V) editing, a specialized add- on sound card is a must. Very good quality sound cards can be found for under $100, compared with cheaper models around $20— there isn’t a huge difference in price as there is with CPUs and video cards. Look for a card with a higher sampling rate (measured in kilohertz [kHz]) and higher signal- to- noise ratio (measured in decibels [dB]). The de facto standard for sound cards is the Sound Blaster brand. Although other brands exist, they will often tout “Sound Blaster compatibility” in their advertising to show that they are legit.

> [!info] Note
> Integrated motherboard audio will typically have about a 90 kHz sampling rate and 85–90 dB signal-to-noise ratio (SNR or S/N). A good add-on sound card can provide sampling of 190 kHz or more and an SNR of 115 dB or higher. The difference is noticeable, especially in professional productions that may be played at loud volumes.

In addition to audio output, many A/V editors will require the ability to input custom music from an electronic musical keyboard or other device. A term you will hear in relation to this is the MIDI standard. As noted earlier, old sound cards would sometimes have a round 
5-pin MIDI port, which was used to connect the musical keyboard or other instrument to the computer. Today, digital musical instrument connections are often made via USB. Nonetheless, you will still see the term MIDI compatible used with a lot of digital musical devices.

### Video Capture Cards 

A video capture card is a standalone add-on card often used to save a video stream to the
computer for later manipulation or sharing. This can be video from an Internet site, or video
from an external device such as a digital camera or smartphone. Video-sharing sites on the
Internet make video capture cards quite popular with enterprises and Internet users alike.
Video capture cards need and often come with software to aid in the processing of 
multi-media input. While video and sound cards are internal expansion devices, capture cards can be internal (PCIe) or external (USB).

Not all video capture cards record audio signals while processing video signals. If this feature is important to you or the end user, be sure to confirm that the card supports it. Also know that capture cards work with standard video resolutions, and specific cards might be limited on the resolutions they support. Double-check the specifications to make sure the card will meet the need, and also make sure to get reviews of the software used with the device.

## Network Interface Card

A network interface card (NIC) is an expansion card that connects a computer to a network so that it can communicate with other computers on that network. It translates the data from the parallel data stream used inside the computer into the serial data stream that makes up the frames used on the network. Internal cards have a connector for the type of expansion bus on the motherboard (PCIe or PCI) and external cards typically use USB. In addition to physically installing the NIC, you need to install drivers for the NIC in order for the computer to use the adapter to access the network. Figure 1.45 shows a PCIe x1 Ethernet NIC with an RJ-45 port.

- **Figure 1.44** A network interface card
![[Image 1.44.png]]

> [!info] Note
> Many computers, especially mobile devices, have NIC circuitry integrated into their motherboards. Therefore, a computer with an integrated NIC wouldn’t need to have a NIC expansion card installed unless it was faster or you were using the second NIC for load balancing (splitting the traffic between two cards to increase speed), security, or fault-tolerance (having a backup in case one fails) applications.

You will see two different types of network cards: wired and wireless. A wired card has an interface for the type of network it is connecting to (such as fiber connectors, Registered Jack 45 [RJ-45] for unshielded twisted pair [UTP], antenna for wireless, or BNC for legacy coax). Wireless cards of course don’t need to use wires, so they won’t necessarily have one of these ports. Some do, just for compatibility or desperate necessity.

Wireless NICs have the unique characteristic of requiring that you configure their connecting device before configuring the NIC. Wired NICs can generally create a link and begin operation just by being physically connected to a hub or switch. The wireless access point or ad hoc partner computer must also be configured before secure communication, at a minimum, can occur by using a wireless NIC. Figure 1.46 shows a PCI wireless NIC for a desktop computer. On the back of it (the left side of the picture) is the wireless antenna.

- **Figure 1.45** A wireless NIC 
![[Image 1.45.png]]

> [!info] Real World Scenario
> **The Way of the Dinosaur...**
> 
> >
> 
> Before high- speed, wireless Internet was available pretty much everywhere you went, wannabe web users needed to connect to the Internet using the plain old telephone system (POTS). Doing so required a device called a modem.
> 
> >
> 
> Old telephone lines were analog, and of course computers are digital. The modem got its name because it modulated and demodulated analog and digital signals to enable computers to connect to each other over analog telephone lines. Modems look a bit like network cards, but the connector is smaller. Instead of the 8-pin RJ-45 connector, phone lines use the 4-pin RJ-11 connector. For those of you interested in history, a modem is shown in Figure 1.46. Notice it has two connectors. It’s probably too hard to see in Figure 1.46, but modems with two connectors have a small telephone icon etched into the faceplate. This tells you which connector to use to plug into the wall, and which one to plug a telephone into. If the modem was in use, the telephone could not be used. Only one connection at a time!
> - **Figure 1.46** An internal analog modem
> ![[Image 1.46.png]]

## Input/Output

An input/output card is often used as a catchall phrase for any expansion card that enhances the system, allowing it to interface with devices that offer input to the system, output from the system, or both. The following are common examples of modern I/O cards:

- USB cards
- Storage cards, such as eSATA
- Thunderbolt cards

Figure 1.47 shows a 7-port PCIe x1 USB expansion card (left) next to an eSATA card (right). USB cards commonly come in 2-, 4-, and 7-port configurations, whereas eSATA cards often have one or two external ports. This eSATA card also has two internal SATA connectors on the top (left, in the picture) of the card. You’ll also find cards that have multiple port types, such as eSATA and USB. 

- **Figure 1.47** USB and eSATA expansion cards
![[Image 1.47.png]]

These cards are to be installed in a compatible slot on the motherboard. Their configuration is minimal, and it is usually completed through the operating system’s Plug and Play (PnP) process. Nevertheless, check the BIOS settings after installation for new entries in the menu structure. It’s the job of the BIOS to track all the hardware in the system and supply resources as needed. For example, a new Thunderbolt expansion card might allow you to configure whether attached Thunderbolt devices should be allowed to wake the system, how long a delay should be observed before waking the system, and various settings for how to use memory and other resources.

## Adapter Configuration

Expansion cards might require configuration. However, most can be recognized automatically by a PnP operating system. In other words, resources are handed out automatically without jumper settings, or the installation of device drivers is handled or requested automatically. Supplying the drivers might be the only form of configuration required.

Some adapters, however, require more specific configuration steps during installation.
For example:

- Two or more PCIe graphics adapters that support SLI (see Chapter 1, “Motherboards, Processors, and Memory,”) must be bridged together with special hardware that comes with the adapters.
- Most sound cards tend to work with no specific configuration, but advanced features will need to be implemented through the operating system or through utilities that came with the adapter.
- The functions of video capture cards are sometimes not native to the operating system and therefore come with advanced utilities that must be learned and configured before the adapters will work as expected.
- Wireless network adapters often require the installation of a screw- on antenna, which should be postponed until after the card is fully inserted and physically secured in the system. Software configuration that allows these cards to communicate with a wireless access point can be challenging for the novice.
- Wired network adapters tend to be easier to configure than wireless ones. Nevertheless, even wired NICs might require manual configuration of certain protocol settings, such as IP addressing, duplex, and speed, in order for them to be productive.

In general, installation and configuration steps for expansion cards can be summarized
as follows:

1. Ensure that the computer is powered off.
2. Install the adapter into an open slot.
3. Connect power, if needed. (This most often applies to video cards.)
4. After booting up the computer, install the driver. (Again, Plug and Play may take care of this automatically for you.)
5. If the card isn’t recognized or providing the expected functionality, check the BIOS for configuration settings.
6. For other configuration options, use the utility provided by the manufacturer, if applicable. 

In any event, consult the documentation provided with your adapter or the manufacturer’s website for additional configuration requirements or options. The more specialized the adapter, the more likely it will come with specialty-configuration utilities.

> [!info] Note
> For the exam, you will be expected to know how to install and configure add- on cards. The types of expansion cards in the exam objectives are sound, video, capture, and network interface. 
