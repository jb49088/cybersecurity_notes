# Cables and Connectors

Peripheral devices used with a computer need to attach to the motherboard somehow. They do so through the use of ports and cables. A port is a generic name for any connector on a computer or peripheral into which a cable can be plugged. A cable is simply a way of connecting a peripheral or other device to a computer using multiple copper or fiber-optic conductors inside a common wrapping or sheath. Typically, cables connect two ports: one on the computer and one on some other device. 

The A+ exam objectives break cables and connectors into two different subobjectives, but really they need to be discussed together. After all, a cable without a connector doesn’t do much good, and neither does a connector without a cable. In the following sections, we’ll look at three different classifications of cables and the connectors that go with them: peripheral, video, and hard drive.

## Peripheral Cables and Connectors

Some cables are for specific types of devices only. For example, HDMI can transmit audio as well as video, and SCSI supports more than just hard drives. For the most part, though, we associate HDMI with video and SCSI with storage devices. 

Unlike HDMI and SCSI, the cables and connectors in this section are specifically designed to connect a variety of devices. For example, someone may have a USB hub with a wireless mouse, network card, Lightning cable (to charge an iPhone), and flash drive all attached at the same time. Those four devices serve very different purposes, but they all share the USB connection in common. We’ll start with the highly popular USB and then discuss Lightning ports, Thunderbolt cables, and serial cables. 

### Universal Serial Bus

Universal Serial Bus (USB) cables are used to connect a wide variety of peripherals, such as keyboards, mice, digital cameras, printers, scanners, hard drives, and network cards, to computers. USB was designed by several companies, including Intel, Microsoft, and IBM, and is currently maintained by the USB Implementers Forum (USB-IF).

USB technology is fairly straightforward. Essentially, it is designed to be Plug and Play—just plug in the peripheral and it should work, provided that the software is installed to support it. Many standard devices have drivers that are built into the common operating systems or automatically downloaded during installation. More complex devices come with drivers to be installed before the component is connected.

USB host controllers can support up to 127 devices, which is accomplished through the use of a 7-bit identifier. The 128th identifier, the highest address, is used for broadcasting to all endpoints. Realistically speaking, you’ll probably never get close to this maximum. Even if you wanted to try, you won’t find any computers with 127 ports. Instead, you would plug in a device known as a USB hub (shown in Figure 1.93) into one of your computer’s USB ports, which will give you several more USB ports from one original port. Understand that a hub counts as a device for addressing purposes. Hubs can be connected to each other, but interconnection of host controllers is not allowed; each one and its connected devices are isolated from other host controllers and their devices. As a result, USB ports are not considered networkable ports. Consult your system’s documentation to find out if your USB ports operate on the same host controller. 

- **Figure 1.93** A 4-port USB hub
![[Image 1.93.png]]

Another nice feature of USB is that devices can draw their power from the USB cable, so you may not need to plug in a separate power cord. This isn’t universally true, though, as some peripherals still require external power. 

#### USB Standards

Even though USB was released in 1996, the first widely used standard was USB 1.1, which was released in 1998. It was pretty slow—only 12 Mbps at full speed and 1.5 Mbps at low speed—so it was only used for keyboards, mice, and printers. When USB 2.0 came out in 2000 with a faster transfer rate of 480 MBps (called Hi-Speed), video devices were possible. The newer USB 3.x and USB4 standards have increased throughput even further. Table 3.1 lays out the specifications and speeds for you.

- **Table 3.1** USB specifications

| Specification | Release year | Maximum speed | Trade name   | Color |
| ------------- | ------------ | ------------- | ------------ | ----- |
| USB 1.1       | 1998         | 12 Mbps       | Full-Speed   | White |
| USB 2.0       | 2000         | 480 Mbps      | Hi-Speed     | Black |
| USB 3.0       | 2008         | 5 Gbps        | SuperSpeed   | Blue  |
| USB 3.1       | 2013         | 10 Gbps       | SuperSpeed+  | Teal  |
| USB 3.2       | 2017         | 20 Gbps       | SuperSpeed+  | Red   |
| USB4          | 2019         | 40 Gbps       | USB4 40 Gbps | n/a   | 

The USB 1.x and 2.x specifications didn’t recommend a specific color for the ports, but when USB 3.0 was released, the USB Implementers Forum suggested that the ports and cable connectors be colored blue, to signify that they were capable of handling higher speeds.

Device manufacturers are not required to follow the color-coding scheme, so you may see some inconsistency. A yellow USB port is “always on,” meaning it’s capable of charging a connected device even if the PC is sleeping or shut down.

USB4 is the newest standard, and it’s based on Thunderbolt 3 specifications. Other features of USB4 include:

- Up to 40 Gbps data transfers (there is a 20 Gbps standard and a 40 Gbps one)
- Support for DisplayPort and PCIe tunnelling
- Support for dual 4k video displays or one 8k display
- Compatibility with Thunderbolt 3 and Thunderbolt 4 devices
- Backward compatibility with USB down to USB 2.0
- Required use of USB-C connectors

#### USB Power

As mentioned previously, USB ports provide power to devices plugged into them. Typical power for attached USB devices is 5V. The maximum current (amps) and wattage will
depend on the connected device and USB standard being used.

All USB ports are also capable of functioning as charging ports for devices such as tablets, smartphones, and smart watches. The charging standard, called USB Battery Charging, was released in 2007. USB Power Delivery (PD) was developed in 2012. Technically, they are different standards, but in practice, USB ports are capable of supporting both standards at the same time. Table 3.2 outlines some of the versions and the maximum power that they provide. The newest version, USB PD 3.1, requires the use of a USB-C cable. 

- **Table 3.2** USB power standards

| Standard                                                                        | Year | Maximum power  |
| ------------------------------------------------------------------------------- | ---- | -------------- |
| USB Battery Charging 1.0                                                        | 2007 | 5V,1.5A (7.5)  |
| USB Battery Charging 1.2                                                        | 2010 | 5V, 5A (20W)   |
| USB Power Delivery 1.0                                                          | 2012 | 20V, 5A (100W) |
| USB Power Delivery 2.0 (specified use of Type- C connectors but only up to 15W) | 2014 | 5V, 3A (15W)   |
| USB Power Delivery 3.0                                                          | 2015 | 20V, 5A (100W) |
| USB Power Delivery 3.1                                                          | 2021 | 48V, 5A (240W) |

A smartphone or tablet typically needs a minimum of about 7.5 watts to charge properly. The Battery Charging 1.0 standard was good enough, but not for larger devices. For example, about 20 watts is required to power a small laptop computer, and standard 15- inch laptops can require 60 watts or more. With USB PD, one USB port can now provide enough power for a laptop as well as a small printer. 

Because of the capabilities of USB PD, it’s becoming common to see devices up to laptop size lose their standard AC power ports and adapters—they may just have a USB-C port instead. To get the full capabilities of USB PD, you need to use a USB- C port and cable.

#### USB Cables and Connectors

In order to achieve the full speed of the specification that a device supports, the USB cable
needs to meet that specification as well. In other words, USB 1.x cables cannot provide
USB 2.0 and 3.x performance, and USB 2.0 cables cannot provide USB 3.x performance.

Otherwise, the connected device will have to fall back to the maximum version supported by the cable. This is usually not an issue, except for the lost performance, but some high- performance devices will refuse to operate at reduced levels. Note that all specifications are capable of Low Speed, which is a 1.5 Mbps performance standard that has existed since the beginning of USB time.

Throughout most of its history, USB has relied on a small suite of standard connectors. The two broad classifications of connectors are designated Type-A and Type-B connectors, and there are micro and mini versions of each. A standard USB cable has some form of Type-A connector on the end that plugs into the computer or hub, and some form of Type-B or proprietary connector on the device end. Figure 1.94 shows five classic USB 1.x/2.0 cable connectors. From left to right, they are as follows:

- Micro-USB
- Mini-USB
- Type-B
- Type-A female
- Type-A male

- **Figure 1.94** Standard USB connectors
![[Image 1.94.png]]

Small form factor devices, including many smartphones and smaller digital cameras, use a micro-USB or mini-USB connector, unless the manufacturer has developed its own proprietary connector. Micro-USB connectors (and modified ones) are popular with many Android phone manufacturers.

In 2014, a new connector named USB Type-C (or simply USB-C) was developed. USB-C is designed to replace Type-A and Type-B, and, unlike its predecessors, it’s reversible. That means no more flipping the connector over several times to figure out which way it connects. Type-C cables will also be able to provide more power to devices than classic cables were. Figure 1.95 shows a Type-C connector and a Type-A connector. You can see that while the Type-A connector is rectangular- shaped, the Type-C connector has rounded corners and looks more like an elongated oval.

- **Figure 1.95** USB Type-C (top) and Type-A (bottom)
![[Image 1.95.png]]

> [!info] Note
> One point of confusion for many is dissociating the connector type from the standard. Because USB 3.1 and USB-C were both released around the same time, people often think that they are one and the same—but they’re not. USB 3.1 can be implemented using classic A and B connectors, and USB 2.0 can work over a Type-C connector. 

USB was designed to be a short-distance technology. Because of this, USB cables are limited in length. USB 1.x and 2.0 can use cables up to 5 meters long, whereas USB 3.x can use cables up to 3 meters long. The maximum length of a USB4 cable is even shorter yet at 80 centimeters (0.8 meters). In addition, if you use hubs, you should never use more than five hubs between the system and any component.

Despite the seemingly locked-up logic of USB connectivity, it is occasionally necessary to alter the interface type at one end of a USB cable. For that reason, there are a variety of simple, passive converters on the market with a USB interface on one side and a USB or different interface on the other. Along with adapters that convert USB Type-A to USB Type-B, there are adapters that will convert a male connector to a female one. In addition, you can convert USB to a lot of other connector types, such as USB to Ethernet (shown in Figure 1.96), USB to SATA, USB to eSATA, USB to PS/2, USB to serial, and a variety of others. 

- **Figure 1.96** Kensington USB to Ethernet adapter
![[Image 1.96.png]]

### Lightning

Introduced in 2012 with the iPhone 5, the Lightning connector is Apple’s proprietary connector for iPhones and iPads. It’s an 8-pin connector that replaced Apple’s previous 30-pin dock connector. A standard Lightning cable has a USB Type-A connector on one end and the Lightning connector on the other, as shown in Figure 1.97. It’s not keyed, meaning that you can put it in with either edge up. 

- **Figure 1.97** Lightning cable
![[Image 1.97.png]]

Lightning cables support USB 2.0. You will find cables that are USB-C to Lightning, as well as various Lightning adapters, such as those to HDMI, DisplayPort, audio, and Lightning to female USB Type-A (so you can plug a USB device into an iPad or iPhone).

There are rumors that Apple may do away with the Lightning connector in a future iPhone release and instead use USB- C. After all, Apple has added USB-C ports to laptops and iPads, and USB-C is the port of the future. The same rumors have persisted since the iPhone 8 was released in 2017, and it seems that Apple has little reason to move away from its proprietary connector.

### Thunderbolt

Where there’s lightning, there’s thunder, right? Bad joke attempts aside, in computer circles Lightning connectors don’t have anything to do with Thunder(bolt). Thunderbolt, created in collaboration between Intel and Apple and released in 2011, combines PCI Express 2.0 x4 with the DisplayPort 1.x technology. While it’s primarily used for video (to replace DisplayPort), the connection itself can support multiple types of peripherals, much like USB does. 

#### Thunderbolt Standards

For most of their histories, Thunderbolt and USB have been competing standards. Thunderbolt was designed more for video applications and USB was the slower “jack of all trades” port, but in reality, they could be used for almost the exact same list of peripherals. It just depended on what your computer supported. But as we pointed out in the USB section, the new USB4 version is based on Thunderbolt 3, providing the same speed and using the same connectors. Table 3.3 shows the four Thunderbolt versions and some key characteristics.

- **Table 3.3** Thunderbolt standards

| Version       | Year | Maximum throughput | Connector        | Other new features                                          |
| ------------- | ---- | ------------------ | ---------------- | ----------------------------------------------------------- |
| Thunderbolt 1 | 2011 | 10 Gbps            | Mini DisplayPort |                                                             |
| Thunderbolt 2 | 2013 | 20 Gbps            | Mini DisplayPort | DisplayPort 1.2 (can send video to a 4k display)            |
| Thunderbolt 3 | 2015 | 40 Gbps            | USB-C            | 10 Gbps Ethernet support                                    |
| Thunderbolt 4 | 2020 | 40 Gbps            | USB-C            | Can support two 4k displays or one 8k display; 32 Gbps PCIe | 

Thunderbolt 3 was released in 2015 and doubled the bandwidth to 40 Gbps. It supports PCIe 3.0 and DisplayPort 1.2, meaning that it can support dual 4K displays at 60 Hz or a single 4K display at 120 Hz. It also provides up to 100 watts of power to a device.

Thunderbolt 4 is the current standard, released in 2020. Perhaps the most interesting thing about the new release is what it doesn’t do, which is increase data transfer rates versus Thunderbolt 3. It still has a maximum bandwidth of 40 Gbps. And the maximum of 100 watts of power to attached devices didn’t change either. The big advantages Thunderbolt 4 has include support for two 4k displays or one 8k display and the requirement to support 32 Gbps data transfers via PCIe, up from 16 Gbps in version 3.

#### Thunderbolt Cables and Connectors

The most common Thunderbolt cable is a copper, powered active cable extending as far as 3 meters, which was designed to be less expensive than an active version of a DisplayPort cable of the same length. There are also optical cables in the specification that can reach as far as 60 meters. Copper cables can provide power to attached devices, but optical cables can’t.

Additionally, and as is the case with USB, Thunderbolt devices can be daisy-chained and connected via hubs. Daisy chains can extend six levels deep for each controller interface, and each interface can optionally drive a separate monitor, which should be placed alone on the controller’s interface or at the end of a chain of components attached to the interface.

As noted in Table 3.3, Thunderbolt changed connectors between versions 2 and 3. Figure 3.19 shows two Thunderbolt 2 interfaces next to a USB port on an Apple MacBook Pro. Note the standard lightning- bolt insignia by the port. Despite its diminutive size, the Thunderbolt port has 20 pins around its connector bar, like its larger DisplayPort cousin. Of course, the functions of all the pins do not directly correspond between the two interface types, because Thunderbolt adds PCIe functionality.

- **Figure 1.98** Two Thunderbolt 2 interfaces
![[Image 1.98.png]]

Starting with Thunderbolt 3, the connector was changed to standard USB-C connectors, as shown in Figure 1.99. Notice that the lightning bolt icon remained the same.

- **Figure 1.99** Two Thunderbolt 3 interfaces
![[Image 1.99.png]]

Converters are available that connect Thunderbolt connectors to VGA, HDMI, and DVI monitors. Active converters that contain chips to perform the conversion are necessary in situations such as when the technology is not directly pin-compatible with Thunderbolt—as with VGA and DVI-A analog monitor inputs, for example. Active converters are only slightly more expensive than their passive counterparts but still only a fraction of the cost of Thunderbolt hubs. One other advantage of active connectors is that they can support resolutions of 4k (3840 × 2160) and higher.

### Serial Ports

Before USB came along in 1998, serial ports were considered slow and inferior to parallel ports. Still, serial enjoyed use among peripherals that didn’t need to transfer information at high speeds, such as mice, modems, network management devices, and even printers. Figure 2.01 shows a 9-pin serial port. It’s the one marked “Serial,” and it’s also the only male connector on the back of the PC.

- **Figure 2.00** Several peripheral ports
![[Image 2.00.png]]

As you might expect, a serial cable attaches to the serial port. Figure 2.02 shows a female DB-9 serial connector. To make things more confusing, sometimes you will hear people refer to the image in Figure 2.02 as an RS-232 cable or connector. Even though the terms are often used interchangeably, there is a technical difference.

- **Figure 2.01** DB- 9 serial connector
![[Image 2.01.png]]

DB-9 refers to a specific type of D-sub connector that has 9 pins. RS-232, on the other hand, is a communications standard for serial transmission. In other words, systems may communicate with each other using RS-232 over a DB-9 connection. But RS-32 can be used on other types of serial cables as well, such as DB-15 or DB- 5. Generally speaking, if someone asks for an RS-232 serial cable, they mean a DB-9 cable with female connectors. But it’s always best to confirm.

RS-232 did have a few advantages over USB—namely, longer cable length (15 meters vs. 3–5 meters) and a better resistance to electromagnetic interference (EMI). Still, USB has made old-school serial ports nearly obsolete. About the only time they are used today is for management devices that connect to servers or network routers with no keyboard and monitor installed.

> [!info] Other Keyboard and Mouse Connectors
> At one time, the most popular connectors for keyboards and mice were round connectors called Personal System/2 (PS/2) connectors. The PS/2 connector (there are two on the left in Figure 3.21) is a smaller 6-pin mini- DIN connector. Many PCs included a PS/2 keyboard connector as well as a PS/2 mouse connector right above it on the motherboard. The keyboard connector was colored purple, and the mouse one green. The ends of the keyboard and mouse cables would be purple and green as well. Today, the PS/2-style connector has been replaced by the USB port.
> >
>
> If you do run into a keyboard or mouse with a PS/2 connector, or a motherboard with a PS/2 port, you can buy a PS/2-to-USB adapter to make them work with more current hardware.

## Video Cables and Connectors 

Computer displays are ubiquitous—they’re easily the most widely used peripheral. Different standards exist to connect displays to the computer, and you need to be familiar with five of them for the exam: VGA, DVI (and variants), HDMI, and DisplayPort. We will start with the older technologies and work toward the present.

### Video Graphics Array Connector

The Video Graphics Array (VGA) connector was the de facto video standard for computers for years and is still in use today. First introduced in 1987 by IBM, it was quickly adopted by other PC manufacturers. The term VGA is often used interchangeably to refer to generic analog video, the 15-pin video connector, or a 640 × 480 screen resolution (even though the VGA standard can support much higher resolutions). Figure 2.02 shows a VGA port, as well as the male connector that plugs into the port. Nearly all VGA connectors are blue.

- **Figure 2.02** VGA connector and port
![[Image 2.02.png]]

> [!info] Understanding D-Sub Ports and Connectors
> >
> 
> The VGA connector is an example of a D-subminiature connector, also known as a D-sub connector. For a number of years, D-sub was the most common style of connector found on computers. Their names are typically designated with DX-n, where the letter X is replaced by a letter from A to E, which refers to the size of the connector, and the letter n is replaced by the number of pins or sockets in the connector.
> >
>
> D-sub connectors are usually shaped like a trapezoid and have at least two rows of pins with no other keying structure or landmark. Several were shown in Figure 3.21. At the bottom center in Figure 3.21 is a DE-15F 15-pin display-connector port, which may also be referred to as an HD-15 or DB-15 port. The top one is a classic DB- 25 parallel port, and the bottom left is a DB-9 serial port. The IEEE 1394 (FireWire) and two dusty USB ports are shown for a size comparison.
> >
> 
> The “D” shape ensures that only one orientation is possible. If you try to connect them upside down or try to connect a male connector to another male connector, they just won’t go together and the connection can’t be made. By the way, male interfaces have pins, while female interfaces have sockets. Be on the lookout for the casual use of DB to represent any D-sub connector. This is very common and is accepted as an unwritten de facto standard, even if some are technically DE- or DA- connectors. Also note that you will see them written without the hyphen or with a space, such as DB15 or DB 15.

VGA technology is the only one on the objectives list that is purely analog. It has been superseded by newer digital standards, such as DVI, HDMI, and DisplayPort, and it was supposed to be phased out starting in 2013. A technology this widely used will be around for quite a while, though, and you’ll still see it occasionally in the wild (or still in use).

### Digital Visual Interface

The analog VGA standard ruled the roost for well over a decade but it had a lot of shortcomings. Digital video can be transmitted farther and at higher quality than analog, so development of digital video standards kicked off in earnest. The first commercially available one was a series of connectors known collectively as Digital Visual Interface (DVI) and was released in 1999. 

At first glance, the DVI connector might look like a standard D-sub connector. On closer inspection, however, it begins to look somewhat different. For one thing, it has quite a few pins, and for another, the pins it has are asymmetrical in their placement on the connector. The DVI connector is usually white and about an inch long. Figure 2.03 shows what the connector looks like coming from the monitor. 

- **Figure 2.03** DVI connector
![[Image 2.03.png]]

There are three main categories of DVI connectors:

- **DVI-A:** DVI-A is an analog-only connector. The source must produce analog output, and the monitor must understand analog input.
- **DVI-D:** DVI-D is a digital-only connector. The source must produce digital output, and the monitor must understand digital input.
- **DVI-I:** DVI-I is a combination analog/digital connector. The source and monitor must both support the same technology, but this cable works with either a digital or an analog signal.

The DVI-D and DVI-I connectors come in two varieties: single-link and dual-link. The dual- link options have more conductors—taking into account the six center conductors—than their single- link counterparts; therefore, the dual- link connectors accommodate higher speed and signal quality. The additional link can be used to increase screen resolution for devices that support it. Figure 2.04 illustrates the five types of connectors that the DVI standard specifies.

- **Figure 2.04** Types of DVI connectors
![[Image 2.04.png]]

DVI-A and DVI-I analog quality is superior to that of VGA, but it’s still analog, meaning that it is more susceptible to noise. However, the DVI analog signal will travel farther than the VGA signal before degrading beyond usability. Nevertheless, the DVI-A and VGA interfaces are pin-compatible, meaning that a simple passive DVI-to-VGA adapter, as shown in Figure 2.05, is all that is necessary to convert between the two. As you can see, the analog portion of the connector, if it exists, comprises the four separate color and sync pins and the horizontal blade that they surround, which happens to be the analog ground lead that acts as a ground and physical support mechanism even for DVI-D connectors.

- **Figure 2.05** DVI-to-VGA adapter
![[Image 2.05.png]]

It’s important to note that DVI-I cables and interfaces are designed to interconnect two analog or two digital devices; they cannot convert between analog and digital. DVI cables must support a signal of at least 4.5 meters, but better cable assemblies, stronger transmitters, and active boosters result in signals extending over longer distances.

### High-Definition Multimedia Interface

High-Definition Multimedia Interface (HDMI) is an all-digital technology that advances the work of DVI to include the same dual- link resolutions using a standard HDMI cable but with higher motion-picture frame rates and digital audio right on the same connector. HDMI was introduced in 2002, which makes it seem kind of old in technology years, but it’s a great, fast, reliable connector that will probably be around for several years to come. HDMI cabling also supports an optional Consumer Electronics Control (CEC) feature that allows transmission of signals from a remote- control unit to control multiple devices without separate cabling to carry infrared signals.

HDMI cables, known as Standard and High Speed, exist today in the consumer space. Standard cables are rated for 720p resolution as well as 1080i, but not 1080p. High Speed cables are capable of supporting not only 1080p, but also the newer 4k and 8k technologies. Figure 2.06 shows an HDMI cable and port.

- **Figure 2.06** HDMI cable and port
![[Image 2.06.png]]

In June 2006, revision 1.3 of the HDMI specification was released to support the bit rates necessary for HD DVD and Blu-ray Disc. This version also introduced support for “deep color,” or color depths of at least one billion colors, including 30-, 36-, and 48-bit color. However, not until version 1.4, which was released in May 2009, was the High Speed HDMI cable initially required.

With version 1.4 came HDMI capability for the controlling system—the television, for instance—to relay Ethernet frames between its connected components and the Internet, alleviating the need for each and every component to find its own access to the LAN for Internet access. Both Standard and High Speed cables are available with this Ethernet channel. Each device connected by such a cable must also support the HDMI Ethernet Channel specification, however.

Additional advances that were first seen in version 1.4 were 3D support, 4K resolution (but only at a 30 Hz refresh rate), an increased 120 Hz refresh rate for the 1080 resolutions, and an Audio Return Channel (ARC) for televisions with built-in tuners to send audio back to an A/V receiver without using a separate output cable. Version 1.4 also introduced the anti- vibration Type-E locking connector for the automotive-video industry and cables that can also withstand vibration as well as the hot/cold extremes that are common in the automotive world.

Version 2.0 of HDMI (2013) introduced no new cable requirements. In other words, the existing High Speed HDMI cable is fully capable of supporting all new version 2 enhancements. These enhancements include increasing the 4K refresh rate to 60 Hz, a 21:9 theatrical widescreen aspect ratio, and 32-channel audio. Note that 7.1 surround sound comprises only eight channels, supporting the more lifelike Rec. 2020 color space and multiple video and audio streams to the same output device for multiple users. Version 2.0a, released in 2015, primarily added high dynamic range (HDR) video, but it does not require any new cables or connectors.

The most recent version (as of this writing) is HDMI 2.1, released in November 2017. Version 2.1 specifies a new cable type called 48G, which provides for 48 Gbps bandwidth. 48G cables are backward compatible with older HDMI versions. You can also use older cables with 48G-capable devices, but you just won’t get the full 48 Gbps bandwidth. HDMI 2.1 also provides for 120 Hz refresh rates for 4k, 8k, and 10k video, and it supports enhanced Audio Return Channel (eARC), which is needed for object-based audio formats, such as DTS:X and Dolby Atmos.

Even though the HDMI connector is not the same as the one used for DVI, the two technologies are electrically compatible. HDMI is compatible with DVI-D and DVI-I interfaces through proper adapters, but HDMI’s audio and remote- control pass- through features are lost. Additionally, 3D video sources work only with HDMI. Figure 2.08 shows a DVI-to-HDMI adapter between DVI- D and the Type- A 19-pin HDMI interface. Compare the DVI-D interface in Figure 2.07 to the DVI-I interface in Figure 2.06, and note that the ground blade on the DVI-D connector is narrower than that of the DVI- A and DVI-I connectors. The DVI-D receptacle does not accept the other two plugs for this reason, as well as because the four analog pins around the blade have no sockets in the DVI-D receptacle.

- **Figure 2.07** DVI-to-HDMI adapter
![[Image 2.07.png]]

Unlike DVI-D—and, by extension DVI-I—DVI-A and VGA devices cannot be driven passively by HDMI ports directly. An HDMI-to-VGA adapter must be active in nature, powered either externally or through the HDMI interface itself.

HDMI cables should meet the signal requirements of the latest specification. As a result, and as with DVI, the maximum cable length is somewhat variable. For HDMI, cable length depends heavily on the materials used to construct the cable. Passive cables tend to extend no farther than 15 meters, while adding electronics within the cable to create an active version results in lengths as long as 30 meters.

> [!info] Smaller HDMI connectors
> Multiple versions of HDMI connectors are available in the marketplace. The standard connector that you’re probably used to seeing, and the one shown in Figure 3.27 and Figure 3.28, is the 19-pin Type-A connector. The Type-A connector and the 29-pin Type- B connector were specified in HDMI version 1.0 and haven’t changed much since then. Type-B connectors were intended for higher- resolution products but are not used in the market today.
> >
> 
> HDMI version 1.3 specified a smaller 19-pin Type-C connector for portable devices. The Type-C connector, also referred to as a mini- HDMI connector, is compatible with the Type-A connector, but it still requires an adapter due to its smaller size. HDMI version 1.4 specified two more interfaces: Type-D and Type-E. If Type-C is a mini-HDMI interface, then you might refer to the Type-D connector as micro-HDMI. Figure 2.08 shows all five HDMI connectors. Also compatible with Type-A interfaces because they have the same 19 pins, Type-D interfaces require just a simple adapter for conversion.
> - **Figure 2.08** HDMI connector types
> ![[Image 2.08.png]]
> 
> The mini-HDMI and micro-HDMI connectors are most often used on smaller portable devices, such as tablets, smartphones, and digital cameras. As mentioned previously, the Type-E connector has a locking mechanism and is intended for use in automobiles or other environments that are susceptible to vibration, which could cause a connector and cable to become disconnected.

### DisplayPort

DisplayPort is a royalty-free digital display interface from the Video Electronics Standards Association (VESA) that uses less power than other digital interfaces and VGA. Introduced in 2008, it’s designed to replace VGA and DVI. To help ease the transition, it’s backward compatible with both standards, using an adapter. In addition, an adapter allows HDMI and DVI voltages to be lowered to those required by DisplayPort because it is functionally similar to HDMI and DVI. DisplayPort cables can extend 3 meters, unless an active cable powers the run, in which case the cable can extend to 33 meters. DisplayPort is intended primarily for video, but, like HDMI, it can transmit audio and video simultaneously. 

Figure 2.09 shows a DisplayPort port on a laptop as well as a connector. The DisplayPort connector latches itself to the receptacle with two tiny hooks. A push-button mechanism serves to release the hooks for removal of the connector from the receptacle. Note the beveled keying at the bottom-left corner of the port.

- **Figure 2.09** A DisplayPort port and cable
![[Image 2.09.png]]

The DisplayPort standard also specifies a smaller connector, known as the Mini DisplayPort (MDP) connector. The MDP is electrically equivalent to the full-size DP connector and features a beveled keying structure, but it lacks the latching mechanism present in the DP connector. The MDP connector looks identical to a Thunderbolt 2 connector, which we covered in [[Cables and Connectors#Peripheral Cables and Connectors|Peripheral Cables and Connectors]].

## Hard Drive Cables and Connectors

Remember that all drives need some form of connection to the motherboard so that the computer can “talk” to the disk drive. Regardless of whether the connection is built into the motherboard (onboard) or on an adapter card (off- board), internal or external, the standard for the attachment is based on the drive’s requirements. These connections are known as drive interfaces. The interfaces consist of circuitry and a port, or header.

### Serial Advanced Technology Attachment

The most common hard drive connector used today is Serial Advanced Technology Attachment (SATA). Figure 2.10 shows SATA headers, which you have seen before, and a SATA cable. Note that the SATA cable is flat, and the connector is keyed to fit into the motherboard header in only one way. SATA data cables have a 7-pin connector. SATA power cables have 15 pins and are wider than the data connector.

- **Figure 2.10** SATA connectors and cable
![[Image 2.10.png]]

The SATA we’ve discussed so far is internal, but there’s an external version as well, appropriately named external SATA (eSATA). It uses the same technology, only in an external connection. The port at the bottom center of Figure 2.11 is eSATA. It entered the market in 2003, is mostly intended for hard drive use, and can support up to 15 devices on a single bus. 

- **Figure 2.11** eSATA
![[Image 2.11.png]]

Table 3.4 shows some of the eSATA specifications.

- **Table 3.4** eSATA specifications

| Version      | Year | Speed    | Names                 |
| ------------ | ---- | -------- | --------------------- |
| Revision 1.0 | 2003 | 1.5 Gbps | SATA I, SATA 1.5 Gb/s |
| Revision 2.0 | 2005 | 3.0 Gbps | SATA II, SATA 3 Gb/s  |
| Revision 3.0 | 2009 | 6.0 Gbps | SATA III, SATA 6 Gb/s |

You will commonly see the third generation of eSATA (and SATA) referred to as SATA 6 or SATA 6 Gb/s. This is because if they called it SATA 3, there would be confusion with the second generation, which had transfer speeds of 3.0 Gbps.

An interesting fact about eSATA is that the interface does not provide power, which is a big negative compared to its contemporary high-speed serial counterparts. To overcome this limitation, there is another eSATA port that you might see, called Power over eSATA, eSATA+, eSATAp, or eSATA/USB. It’s essentially a combination eSATA and USB port. Since the port is a combination of two others, neither sanctioning body officially recognizes it (which is probably why there are so many names—other companies call it what they want to). Figure 2.12 shows this port. 

- **Figure 2.12** USB over eSATA
![[Image 2.12.png]]

You can see that this port is slightly different from the one in Figure 3.32, and it’s also marked with a USB icon next to the eSATA one. On the market, you can purchase cables that go from this port to an eSATA device and provide it with power via the eSATAp port.

> [!info] Note
> You might have noticed that the most recent eSATA specification was released over a decade ago. eSATA is basically dead, because newer standards such as USB4 and Thunderbolt 3 (and 4) provide not only power but faster data transmission speeds as well.

### Parallel Advanced Technology Attachment

Prior to SATA, the most popular hard drive connector was Integrated Drive Electronics (IDE), which has now been renamed Parallel Advanced Technology Attachment (PATA). There is no difference between PATA and IDE, other than the name. Figure 2.13 shows PATA connectors on a motherboard next to a PATA cable. Refer to Figure 2.9, to see a direct comparison of SATA and PATA connectors on a hard drive. 

- **Figure 2.13** PATA connectors and cable
![[Image 2.13.png]]

PATA drives use a 40-pin flat data cable, and there are a few things to note about it. First, there is an off-colored stripe (often red, pink, or blue) along one edge of the cable to designate where pin 1 is. On a PATA drive, pin 1 is always on the edge nearest the power connector. The second thing to note is that there are three connectors—one for the motherboard and two for drives. PATA technology specifies that there can be two drives per cable, in a primary and secondary configuration. The primary drive will be attached to the other end of the cable, and the secondary, if connected, will use the middle connector. In addition, the drive itself may need to be configured for primary or secondary by using the jumper block on the drive. Most PATA drives will auto-configure their status based on their position on the cable, but if there is a conflict, they can be manually configured.

Power is supplied by a 4-pin power connector known as a Molex connector, shown in Figure 2.14. If you have a PATA drive and a SATA- supporting power supply (or vice versa), you can buy an adapter to convert the power to what you need. The same holds true for data connectors as well. 

- **Figure 2.14** Molex power connector
![[Image 2.14.png]]

### Small Computer System Interface

A fourth type of hard drive connector is called Small Computer System Interface (SCSI). The acronym is pronounced “scuzzy,” even though the original designer intended for it to be called “sexy.” The most common usage is for storage devices, but the SCSI standard can be used for other peripherals as well. You won’t see many SCSI interfaces in home computers—it’s more often found in servers, dedicated storage solutions, and high-end workstations.

Early versions of SCSI used a parallel bus interface called SCSI Parallel Interface (SPI). Starting in 2005, SPI was replaced by Serial Attached SCSI (SAS), which, as you may guess, is a serial bus. If you compare SCSI to other popular drive interfaces at the time, SCSI was generally faster but more expensive than its counterparts, such as IDE.

#### SCSI Parallel Interface

Although it’s essentially obsolete now, you might find some details of SPI interesting. The first standard, ratified in 1986, was an 8- bit bus that provided for data transfers of 5 Mbps.

Because it was an 8-bit bus, it could support up to seven devices. (The motherboard or expansion card header was the eighth.) Each device needed a unique ID from 0 to 7, and devices were attached in a daisy-chain fashion. A terminator (essentially a big resistor) needed to be attached to the end of the chain; otherwise, the devices wouldn’t function.

In 1994, the 8-bit version was replaced by a 16-bit version that supported up to 15 devices and had a transfer speed of 320 Mbps. Compared to the 100 Mbps supported by IDE at the time, you can see why people wanted SCSI!

SPI had different connectors, depending on the standard; 50-pin, 68-pin, and 80-pin connectors were commonly used. Figure 2.15 shows two 50-pin Centronics connectors, which were common for many years. Figure 2.16 shows a terminator, with the top cover removed so that you can see the electronics.

- **Figure 2.15** Two 50-pin SCSI connectors
![[Image 2.15.png]]

- **Figure 2.16** A SCSI terminator
![[Image 2.16.png]]

#### Serial Attached SCSI

Of the newer SCSI implementations, the one you will most likely encounter is SAS. For example, as we mentioned in Chapter 2, most 15,000 rpm hard drives are SAS drives. From an architectural standpoint, SAS differs greatly from SPI, starting with the fact that it’s serial, not parallel. What they do share is the use of the SCSI command architecture, which is a group of commands that can be sent from the controller to the device to make it do something, such as write or retrieve data. 

A SAS system of hard drives works much like the SATA and PATA systems you’ve already
learned about. There’s the controller, the drive, and the cable that connects it. SAS uses its
own terminology, though, and adds a component called an expander. Here are the four components of a SAS system:

- **Initiator:** Think of this as the controller. It sends commands to target devices and receives data back from them. These can be integrated or an add-on card. Each initiator can have a direct connection to 128 devices. 
- **Target:** This is the device, typically a hard drive. It can also be multiple hard drives functioning in a RAID array. 
- **Service Delivery Subsystem:** The service delivery subsystem transmits information between an initiator and a target. Often this is a cable, but it can also be a server backplane (where multiple devices connect).
- **Expander:** An expander is a device that allows for multiple initiators to be combined into one service delivery subsystem. Through the use of expanders, one initiator can support up to 16,256 devices.

Figure 2.17 shows a SAS cable and connector. It’s slightly wider than a SATA power and data connector together. The other end of a cable such as this might have an identical SAS connector or a mini-SAS connector, or it might pigtail into four SATA or mini-SAS connectors. 

- **Figure 2.17** A SAS connector
![[Image 2.17.png]]

Table 3.5 lists SAS standards and maximum throughput.

- **Table 3.5** SAS standards and speeds

| Standard | Year | Throughput |
| -------- | ---- | ---------- |
| SAS-1    | 2005 | 3 Gbps     |
| SAS-2    | 2009 | 6 Gbps     |
| SAS-3    | 2013 | 12 Gbps    |
| SAS-4    | 2017 | 22.5 Gbps  | 

SAS offers the following advantages over SPI:

- No terminator is required.
- Up to 16,256 devices can be connected to a single system.
- Each SAS device has its own link to the controller, so there are no issues with contention (when multiple devices try to use the same link at the same time, causing interference).
- SAS provides faster data transfer speeds than SPI.
- SAS devices are compatible with SATA 2.0 and higher—SATA drives can be connected to SAS controllers.

With the invention of super-fast M.2 and NVMe hard drives, which you learned about , it’s hard to say what the future of SAS is. For example, SAS-5 (45 Gbps) has been under development since around 2018, but there is no official release date and there seems to be no impetus to get it to market. Most likely, SAS will continue to have a place in corporate environments with large-scale storage solutions, while the others will provide leading-edge speed for the workstation environment, particularly among laptops and smaller devices.

