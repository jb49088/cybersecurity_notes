
# Motherboard

[[🏷️PC hardware]]

The spine of the computer is the motherboard, otherwise known as the system board or mainboard. This is the printed circuit board (PCB), which is a conductive series of pathways laminated to a nonconductive substrate that lines the bottom of the computer and is often of a uniform color, such as green, brown, blue, black, or red. It is the most important component in the computer because it connects all the other components together. Figure 1.01 shows a typical PC system board, as seen from above. All other components are attached to this circuit board. On the system board, you will find the central processing unit (CPU) slot or integrated CPU, underlying circuitry, expansion slots, video components, random access memory (RAM) slots, and a variety of other chips.

## Motherboard Form Factors

There are hundreds, if not thousands, of different motherboards in the market today. It can be overwhelming trying to figure out which one is needed. To help, think of mother-boards in terms of which type they are, based on a standard classification. System boards are classified by their form factor (design), such as ATX and ITX. Exercise care and vigilance when acquiring a motherboard and components separately. Motherboards will have different expansion slots, support certain processors and memory, and fit into some cases but not others. Be sure that the other parts are physically compatible with the motherboard you choose.

### Advanced Technology Extended

Intel developed the Advanced Technology eXtended (ATX) motherboard in the mid-1990s to improve upon the classic AT-style motherboard architecture that had ruled the PC world for many years. The ATX motherboard has the processor and memory slots at right angles
to the expansion cards, like the one in Figure 1.00. This arrangement puts the processor and memory in line with the fan output of the power supply, allowing the processor to run
cooler. And because those components are not in line with the expansion cards, you can
install full- length expansion cards—adapters that extend the full length of the inside of a
standard computer case—in an ATX motherboard machine. ATX (and its derivatives, such as micro-ATX) is the primary PC motherboard form factor in use today. Standard ATX motherboards measure 12″ × 9.6″ (305 mm × 244 mm).

- **Image 1.00** A typical motherboard 
![[Image 1.00.png]]

### Information Technology eXtended

The Information Technology eXtended (ITX) line of motherboard form factors was developed by VIA Technologies in the early 2000s as a low- power, small form factor (SFF) board for specialty uses, including home- theater systems, compact desktop systems, gaming systems, and embedded components. ITX itself is not an actual form factor but a family of formfactors. The family consists of the following form factors:

- Mini- ITX— 6.7″ × 6.7″ (170 mm × 170 mm)
- Nano- ITX— 4.7″ × 4.7″ (120 mm × 120 mm)
- Pico- ITX— 3.9″ × 2.8″ (100 mm × 72 mm)
- Mobile- ITX— 2.4″ × 2.4″ (60 mm × 60 mm)

The mini- ITX motherboard has four mounting holes that line up with three or four of the holes in the ATX and micro- ATX form factors. In mini- ITX boards, the rear interfaces are placed in the same location as those on the ATX motherboards. These features make mini- ITX boards compatible with ATX cases. This is where the mounting compatibility ends, because despite the PC compatibility of the other ITX form factors, they are used in embedded systems, such as set- top boxes, home entertainment systems, and smart phones, and lack the requisite mounting and interface specifications. Figure 1.01 shows the three larger forms of ITX motherboards, next to two ATX motherboards for comparison.

- **Figure 1.01** ITX motherboards
![[Image 1.01.png]]

## System board components

System board components consist of essential sockets, slots, and chips that enable hardware integration and communication within a computer system. 

### Bus architecture  

In a PC, data is sent from one component to another via a bus, which is a common collection of signal pathways. In the early days, PCs used serial buses, which sent 1 bit at a time which were painfully slow. Engineers later came up with a way to send 8 bits at a time (over synchronized separate lines), this was known as a parallel bus. 

The downside of parallel communications is the loss of circuit length (how long the circuit could be) and throughput (how much date could move at one time). The signal could travel only a short distance, and the amount of data was limited due to the careful synchronization needed between separate lines, the speed of which must be controlled to limit skewing the arrival of the individual signals at the receiving end.

Later, engineers discovered methods to make serial transmissions work at data rates that are many times faster than parallel signals. Therefore, nearly everything you see today uses a serial bus. The only limitation of serial circuits is in the capability of the transceivers, which tends to grow over time at a refreshing rate due to technical advancements. Some key specs that have made serial communication popular include Serial Advanced Technology Attachment (Serial ATA, or SATA), Universal Serial Bus (USB), IEEE 1394/FireWire , and Peripheral Component Interconnect Express (PCIe).

> [!info] Note
> The term bus is also used in any parallel or bit- serial wiring implementation where multiple devices can be attached at the same time in parallel or in series (daisy- chained). Examples include Small Computer System Interface (SCSI), USB, and Ethernet.

On a motherboard, several different buses are used. Expansion slots of various architectures, such as PCIe, are included to allow for the insertion of external devices, or adapters. Other types of buses exist within the system to allow communication between the CPU, RAM, and other components with which data must be exchanged. 

The various buses throughout a given computer system can be rated by their bus speeds. The higher the bus speed, the higher its performance. In some cases, various buses must be synchronized for proper performance, such as the system bus and any expansion buses that run at the front-side bus speed. Other times, one bus will reference another for its own speed. The internal bus speed of a CPU is derived from the front-side bus clock, for instance. 

### Chipsets 

A chipset is a collection of chips or circuits that perform interface peripheral functions for the processor. This collection of chips is usually the circuitry that provides interfaces for memory, expansion cards, and onboard peripherals, and it generally dictates how a motherboard will communicate with the installed peripherals. 

Chipsets are usually given a name and model number by the original manufacturer. For example, B550 and X570 are chipsets that support AMD processors, and Z490 and H410 are Intel motherboard chipsets. Typically, the manufacturer and model tell you that your particular chipset has a certain set of features (for example, type of CPU and RAM supported, type and brand of onboard video, and so on).

Chipsets can be made up of one or several integrated circuit chips. Intel-based motherboards, for example, typically use two chips. To know for sure, you must check the manufacturer's documentation, especially because cooling mechanisms frequently obscure today's chipset chips, sometimes hindering visual brand and model identification. 

Chipsets can be divided into 2 major functional groups, called Northbridge and Southbridge. 

> [!info] Note
> AMD and Intel have integrated the features of Northbridge and South-bridge into most of their CPUs. Therefore, the CPU provides Northbridge and Southbridge functionality as opposed to separate chipsets.

#### Northbridge 

The Northbridge subset of a motherboard's chipset is the set of circuitry or chips that performs one very important function: management of high speed peripheral communications. The Northbridge is responsible primarily for communications with integrated video using PCIe, for instance, and processor-to-memory communications. Therefore, it can be said that much of the true performance of a PC relies on the specifications of the Northbridge component and its communications capability with the peripherals it controls. 

> [!info] Note
> When we use the term Northbridge, we are referring to a functional subset of a motherboard’s chipset. There isn’t actually a Northbridge brand of chipset.

The communications between the CPU and the memory occur over what is known as the front-side bus (FSB), which is just a set of signal pathways connecting the CPU and main memory, for instance. The clock signal that drives the FSB is used to drive communications by certain other devices, such as PCIe slots, making them local-bus technologies. The back-side bus (BSB), if present, is a set of signal pathways between the CPU and external cache memory. The BSB uses the same clock signal that drives the FSB. If no back-side bus exists, cache is placed on the front-side bus with CPU and main memory.

The Northbridge is directly connected to the Southbridge. It controls the Southbridge and helps to manage the communications between the Southbridge and the rest of the computer.

#### Southbridge

The Southbridge subset of the chipset is responsible for providing support to the slower onboard peripherals (USB, Serial and Parallel ATA, parallel ports, serial ports, and so on), managing their communications with the rest of the computer and the resources given to them. These components do not need to keep up with the external clock of the CPU and do not represent a bottleneck in the overall performance of the system. Any component that would impose such a restriction on the system should eventually be developed for FSB attachment.

In other words, if you're considering any component other than the CPU, memory and cache, or PCIe slots, the Southbridge is in charge. Most motherboards today have integrated USB, network, and analog and digital audio ports for the Southbridge to manage, for example. The Southbridge is also responsible for managing communications with the slower expansion buses, such as PCI, and legacy buses.

Figure 1.02 is a photo of the chipset of a motherboard, with the heat sink of the Northbridge at the top left, connected to the heat-spreading cover of the Southbridge at the bottom right.

- **Figure 1.02** A modern computer chipset
![[Image 1.02.png]]

Figure 1.03 shows a schematic of a typical motherboard chipset (both Northbridge and Southbridge) and the components with which they interface. Notice which components interface with which parts of the chipset.

- **Figure 1.03** A schematic of a typical motherboard chipset 
![[Image 1.03.png]]

### Expansion Slots 

The most visible parts of any motherboard are the expansion slots. These are small plastic slots, usually from 1 to 6 inches long and approximately 0.5 inches wide. As their name suggests, these slots are used to install various devices in the computer to expand its capabilities. Some expansion devices that might be installed in these slots include video, network, sound, and disk interface cards.

If you look at the motherboard in your computer, you will more than likely see one of the
main types of expansion slots used in computers today, which are PCI and PCIe.

#### PCI Expansion slots

It's now considered an old technology, but many motherboards in use today still contain 32-bit Peripheral Component Interconnect (PCI) slots. They are easily recognizable because they are only 3 inches long and classically white, although modern boards take liberties with the color. PCI slots became extremely popular with the advent of Pentium-class processors in the mid-1990s. Although popularity has shifted from PCI to PCIe, the PCI slot's service to the industry cannot be ignored; it has been an incredibly prolific architecture for many years.

PCI expansion buses operate at 33 MHz or 66 MHz (version 2.1) over a 32-bit (4-byte) channel, resulting in data rates of 133 MBps and 266 MBps, respectively, with 133 MBps being the most common, server architectures excluded. PCI is a shared-bus topology, however, so mixing 33 MHz and 66 MHz adapters in a 66 MHz system will slow all adapters to 33 MHz. Older servers might have featured 64-bit PCI slots as well, since version 1.0, which double the 32-bit data rates. 

> [!info] Arriving at the Exact Answer
> To get the math exactly right when dealing with frequencies and data rates ending in 33 and 66, you have to realize that every 33 has an associated one-third (1/3), and every 66 has an associated two-thirds (2/3). The extra quantities are left off of the final result but must be added back on to get the math exactly right. The good news is that omitting these small values from the equation still gets you close, and a bit of experience with the numbers leads to being able to make the connection on the fly.
 
PCI slots and adapters are manufactured in 3.3V and 5V versions. Universal adapters are keyed to fit in slots based on either of the two voltages. The notch in the card edge of the common 5V slots and adapters is oriented toward the front of the motherboard, and the notch in the 3.3V adapters toward the rear. Figure 1.04 shows several PCI expansion slots. Note the 5V
32-bit slot in the foreground and the 3.3V 64-bit slots. Also notice that a universal 32-bit card, which has notches in both positions, is inserted into and operates fine in the 64-bit 3.3V slot in the background.

- **Figure 1.04** PCI expansion slots
![[Image 1.04.png]]

#### PCIe Expansion Slots

The most common expansion slot architecture that is being used by motherboards is PCI Express (PCIe). It was designed to be a replacement for PCI, as well as an older video card standard called accelerated graphics port (AGP). PCIe has the advantage of being faster than AGP while maintaining the flexibility of PCI. PCIe has no plug compatibility with either AGP or PCI. Some modern PCIe motherboards can be found with regular PCI slots for backward compatibility, but AGP slots have not been included for many years.

PCIe is causally referred to as a bus architecture to simplify its comparison with other bus technologies. True expansion buses share total bandwidth among all slots, each of which taps into different points along the common bus lines. In contrast, PCIe uses a switching component with point-to-point connections to slots, giving each component full use of the corresponding bandwidth and producing more of a star topology versus a bus. Furthermore, unlike other expansion buses, which have parallel architectures, PCIe is a serial technology, striping data packets across multiple serial paths to achieve higher data rates.

PCIe uses the concept of lanes, which are the switched point-to-point signal paths between any 2 PCIe components. Each lane that the switch interconnects between any two intercommunicating devices comprises a separate pair of wires for both directions of traffic. Each PCIe pairing between cards requires a negotiation for the highest mutually supported number of lanes. The single lane or combined collection of lanes that the switch interconnects between devices is referred to as a link.

There are seven different link widths supported by PCIe, designated x1 (pronounced "by 1"), x2, x4, x8, x12, x16, and x32, with x1, x4, and x16 being the most common. The x8 link width is less common than these but more common than the others. A slot that supports a particular link width is of a physical size related to that width because the width is based on the number of lanes supported, requiring a related number of wires. As a result, an x8 slot is longer than a x1 slot but shorter than a x16 slot. Every PCIe slot has a 22-pin portion in common toward the rear of the motherboard, which you can see in Figure 1.05, in which the rear of the motherboard is to the left. These 22 pins comprise mostly voltage and ground leads. (The PCIe slots are the longer and lighter ones in Figure 1.05).

- **Figure 1.05** PCIe expansion slots
![[Image 1.05.png]]

Four major versions of PCIe are currently available in the market: 1.x, 2.x, 3.0, and 4.0. For the four versions, a single lane, and therefore a x1 slot, operates it each direction (or transmits and receives from either communicating device's perspective), at a data rate of 250 MBps (almost twice the rate of the most common PCI slot), 500 MBps, approximately 1 GBps, and roughly 2 GBps, respectively.

> [!info] Note
> PCIe 5.0 was formally ratified by the PCI Special Interest Group (PCI- SIG) in 2019, and motherboards supporting the architecture started hitting the market in late 2021. Much like its predecessors, it doubles the speed of the previous version. Therefore, a PCIe 5.0 x1 adapter operates at about 4 MBps in each direction. The slots are forward and backward compatible. For example, you can put a PCIe 4.0 video card into a motherboard with a PCIe 5.0 slot, but you won’t get the full performance that PCIe 5.0 is capable of. The inverse is true as well— a PCIe 5.0 card will work in a 4.0 slot but at the 4.0 standard’s speed. PCIe 6.0 is expected around 2023.

An associated bidirectional link has a nominal throughput of double these rates. Use the doubled rate when comparing PCIe to other expansion buses because those other rates are for bidirectional communication. This means that the 500 MBps bidirectional link of a 1x slot in the first version of PCIe was comparable to PCI's best, a 64-bit slot running at 66 MHz and producing a throughput of 533 MBps. 

> [!info] Note
Bidirectional means that data flows in both directions, often simultaneously. Unidirectional means data flows in only 1 direction

Combining lanes simply results in a linear multiplication of these rates. For example, a PCIe 1.1 x16 slot is capable of 4 GBps of throughput in each direction, 16 times the 250 MBps x1 rate. Bidirectionally, this fairly common slot produces a throughput of 8 GBps. Each subsequent PCIe specification doubles this throughput. The aforementioned PCIe 5.0 will produce bidirectional throughput of approximately 128 GBps, which is faster than some DDR4 standards (which is really fast).

> [!info] Using Shorter Cards in Longer Slots
>Up-plugging is defined in the PCIe specification as the ability to use a higher-capability slot for a lesser adapter. In other words, you can use a shorter (fewer-lane) card in a longer slot. For example, you can insert an x8 card into an x16 slot. The x8 card won’t completely fill the slot, but it will work at x8 speeds if up-plugging is supported by the motherboard. Otherwise, the specification requires up-plugged devices to operate at only the x1 rate. This is something you should be aware of and investigate in advance. Down-plugging is possible only on open- ended slots, although not specifically allowed in the official specification. Even if you find or make (by cutting a groove in the end) an open-ended slot that accepts a longer card edge, the inserted adapter cannot operate faster than the slot’s maximum rated capability because the required physical wiring to the PCIe switch in the Northbridge is not present.

Because of its high date rate, PCIe is the current choice of gaming aficionados. Additionally, technologies similar to NVIDIA's Scalable Link Interface (SLI) allow such users to combine preferably identical graphics adapters in appropriately spaced PCIe x16 slots with a hardware bridge to form a single virtual graphics adapter. The job of the bridge is to provide non-chipset communication among the adapters. The bridge is not a requirement for SLI to work, but performance suffers without it. SLI-ready motherboards allow two, three, or four PCIe graphics adapters to pool their graphics processing units (GPUs) and memory to feed graphics output to a single monitor attached to the adapter acting as the primary SLI device. SLI implementation results in increased graphics performance over single-PCIe and non-PCIe implementations.

Refer back to Figure 1.6, which is a photo of an SLI-ready motherboard with three PCIe x16 slots (every other slot, starting with the top one), one PCIe x1 slot (second slot from the top), and two PCI slots (first and third slots from the bottom). Notice the latch and tab that secures the x16 adapters in place by their hooks. Any movement of these high-performance devices can result in temporary failure or poor performance.

> [!info] Using Riser Cards
> Most PC expansion cards plug directly into the motherboard. A special type of expansion card, called a riser card, provides additional slots that other expansion cards plug into. The other expansion cards are then parallel to the motherboard, as opposed to perpendicular. Figure 1.06 shows an example of a riser card. It's an older example, but it illustrates the concept well. 
> - **Figure 1.06** Riser card in a motherboard
> ![[Image 1.06.png]] 
>
> Riser cards aren't often found in desktop PCs today but do still find some use in rack-mounted servers with low-profile cases. The motherboard must be designed to accept a riser card, and the case needs to be built for it as well, for the external portion of the expansion card to be accessible. 

### Memory Slots and Cache

Memory, or random access memory (RAM), slots are the next most notable slots on a motherboard. These slots are designed for the modules that hold memory chips that make up primary memory, which is used to store currently used data and instructions for the CPU. Many types of memory are available for PCs today. 

For the most part, PCs today use memory chips arranged on a small circuit board. A dual in-line memory module (DIMM) is one type of circuit board. Today's DIMMs differ in the number of conductors, or pins, that each particular physical form factor uses. Some common examples include 168-, 184-, 240-, and 288-pin configurations. In addition, laptop memory comes in smaller form factors known as small outline DIMMs (SODIMMs) and Micro-DIMMs. 

Memory slots are easy to identify on a motherboard. Classic DIMM slots were usually black and, like all memory slots, were placed very close together. DIMM slots with color-coding are more common these days, however. The color-coding of the slots acts as a guide to the installer of the memory. Consult the motherboard's documentation to determine the specific modules allowed as well as their required orientation. The number of memory slots varies from motherboard to motherboard, but the structure of the different slots is similar. Metal pins in the bottom make contact with the metallic pins on each memory module. Small metal or plastic tabs on each side of the slot keep the memory module securely in its slot. Figure 1.07 shows 4 memory slots, with the CPU socket included for reference.

- **Figure 1.07** Double Data Rate (DDR) memory slots
![[Image 1.07.png]]

Sometimes, the amount of primary memory installed is inadequate to service additional requests for memory resources from newly launched applications. When this condition occurs, the user may receive an "out of memory" error message and an application may fail to launch. One solution for this is to use the hard drive as additional RAM. This space on the hard drive is known as the paging file. The technology in general is known as virtual memory or virtual RAM. The paging file is called PAGEFILE.SYS in modern Windows operating systems. It is an optimized space that can deliver information to RAM at the request of the memory controller faster than if it came from the general storage pool of the drive. It's located at c:\pagefile.sys by default. Note that virtual memory cannot be used directly from the hard drive; is must be paged into RAM as the oldest contents of RAM are paged out to the hard drive to make room. The memory controller, by the way, is the chip that manages access to RAM as well as adapters that have had a few hardware memory addresses reserved for their communication with the processor.

Nevertheless, relying too much on virtual memory results in the entire system slowing down considerably. An inexpensive and highly effective solution is to add physical memory to the system, thus reducing its reliance on virtual memory. 

Another type of memory common in PCs is cache memory, which is small and fast and logically sits between the CPU and RAM. Cache is a very fast form of memory forged from static RAM. Cache improves system performance by predicting what the CPU will ask for next and prefetching this information before being asked. This paradigm allows the cache to be smaller in size than the RAM itself. Only the most recent used data and code or that which is expected to be used next is stored in the cache.

You'll see three different cache designations: 

**Level 1 Cache:** L1 cache is the smallest and fastest, and it's on the processor die itself. In other words, it's an integrated part of the manufacturing pattern that's used to stamp the processor pathways into the silicon chip. You can't get any closer to the processor than that.

Though the definition of L1 cache has not changed much over the years, the same is not true for other cache levels. L2 and L3 cache used to be on the motherboard but now have moved on-die in most processors as well. The biggest differences are the speed and whether they are shared.

**Level 2 Cache:** L2 cache is larger but a little slower than L1 cache. For processors with multiple cores, each core will generally have its own dedicated L1 and L2 caches. A few processors share a common L2 cache among the cores.

**Level 3 Cache:** L3 cache is larger and slower than L1 or L2, and is usually shared among all processor cores.

The typical increasing order of capacity and distance from the processor die is L1 cache, L2 cache, L3 cache, RAM, and HDD/SSD (hard disk drive and solid-state drive). This is also the typical decreasing order of speed. The following list includes representative capacities of these memory types. The cache capacities are for each core of the 10th generation Intel Core i7 processor. The other capacities are simply modern examples. 

- L1 cache—80 KB (32 KB for instructions and 48 KB for data) 
- L2 cache—512 KB 
- L3 cache—8–16 MB 
- RAM—16–256 GB 
- HDD/SSD—100s of GB to several TB

One way to find out how much cache your system has is to use a utility such as CPU-Z, as shown in Figure 1.08. CPU-Z is freeware that can show you the amount of cache, processor name and number, motherboard and chipset, and memory specifications. 

- **Figure 1.08** Cache in a system
![[Image 1.08.png]]

> [!info] Note 
> Figure 1.09 shows L1D and L1I caches. Many CPUs will split L1 cache into cache for data (L1D) or instructions (L1I). It’s highly unlikely you’ll be tested on this, but it’s interesting to know.

### Central Processing Unit and Processor Socket

The "brain" of any computer is the central processing unit (CPU). There's no computer without a CPU. There are many different types of processors for computers. 

Typically, in today's computers, the processor is the easiest component to identify on the motherboard. It is usually the component that has either a fan of a heat sink (usually both) attached to it (as shown in Figure 1.09). These devices are used to draw away and disperse the heat that a processor generates. This is done because heat is the enemy of microelectronics. Today's processors generate enough heat that, without heat dispersal, they would permanently damage themselves and the motherboard in a matter of minutes, if not seconds.

- **Figure 1.09** Two heat sinks, one with a fan
![[Image 1.09.png]]

CPU sockets are almost as varied as the processors that they hold. Sockets are basically flat and have several columns and rows of holes or pins arranged in a square, as shown in Figure 1.10. The left socket is known as Socket AM4, made for AMD processors such as the Ryzen, and has holes to receive the pins on the CPU. This is known as a pin grid array (PGA) arrangement for a CPU socket. The holes and pins are in a row/column orientation, an array of pins. The right socket is known as LGA 1200, and there are spring-loaded pins in the socket and a grid of lands on the CPU. The land grid array (LGA) is a newer technology that places the delicate pins (yet more sturdy than those on chips) on the cheaper motherboard instead of on the more expensive CPU, opposite to the way that the aging PGA does. The device with the pins has to be replaced if the pins become too damaged to function.

- **Figure 1.10** CPU socket examples
![[Image 1.10.png]]

Modern CPU sockets have a mechanism in place that reduces the need to apply considerable force to the CPU to install a processor, which was necessary in the early days of personal computing. Given the extra surface area on today's processors, excessive pressure applied in the wrong manner could damage the CPU packaging, its pins, or the motherboard itself. For CPUs based on the PGA concept, zero insertion force (ZIF) sockets are exceedingly popular. ZIF sockets use a plastic or metal lever on one of the two lateral edges to lock or release the mechanism that secures the CPU's pins in the socket. The CPU rides on the mobile top portion of the socket, and the socket's contacts that mate with the CPU's pins are in the fixed bottom portion of the socket. The image of Socket AM4 shown on the left in Figure 1.11 illustrates the ZIF locking mechanism at the right edge of the socket.

For processors based on the LGA concept, a socket with a different locking mechanism is used. Because there are no receptacles in either the motherboard or the CPU, there is no opportunity sockets, as they're called despite the misnomer, have a lid that closes over the CPU and is locked in place by an L-shaped arm that borders two of the socket's edges. The nonlocking leg of the arm has a bend in the middle that latches the lid closed when the other leg of the arm is secured. The right image in 1.11 shows an LGA socket with no CPU installed and the locking arm secured over the lid's tab, along the bottom edge. 

Listing out all the desktop PC socket types you might encounter would take a long time. Instead, we'll give you a sampling of some that you might see. The first thing you might notice is that sockets are made for Intel or AMD processors, but not both. Keep that compatibility in mind when replacing a motherboard or a processor. Make sure that the processor and motherboard were designed for each other (even within the Intel or AMD families); otherwise, they won't fit each other and wont work. Table 1.1 lists some common desktop socket/CPU relationships. Servers and laptops/tablets generally have different sockets altogether, although some CPU sockets will support processors designed for desktops or servers. 

![[Table 1.02]]


> [!info] Note
> Some legacy sockets, such as Socket 5 and Socket 7, supported both AMD and Intel platforms, but it’s unlikely that you will see one in the wild, as they are over 25 years old now.

#### Multisocket and Server Motherboards

When it comes to motherboard compatibility, the two biggest things to keep in mind are the processor type and the case. If either of those are misaligned with what the motherboard supports, you're going to have problems.

Thus far, as we've talked about desktop motherboards and their CPU sockets, we have shown examples of boards that have just one socket. There are motherboards that have more than one CPU socket and conveniently, they are called multisocket (typically written as 2 words) motherboards. Figure 1.11 shows a 2 socket motherboard made by GIGABYTE. The 2 CPU sockets are easily identifiable and note that each CPU socket has 8 dedicated memory slots.

- **Figure 1.11** GIGABYTE multisocket motherboard
![[Image 1.11.png]]

Trying to categorize server motherboards can be a bit challenging. Servers are expected to do a lot more work than the average PC, so it makes sense that servers need more powerful hardware. Servers can, and quite often do, make do with a single processor on a "normal" PC motherboard. At the same time, there are motherboards designed specifically for servers that support multiple processors (2 and 4 sockets are common) and have expanded memory and networking capabilities as well. Further, while server motherboards are often ATX-sized, many server manufacturers create custom boards to fit inside their chassis. Regardless, multisocket and server motherboards will generally use the same CPU sockets that other motherboards use.

#### Mobile Motherboards

In small mobile devices, space is at a premium. Some manufacturers will use standard small-factor motherboards, but most create their own boards to fit inside specific cases. An example of an oddly shaped Dell laptop motherboard is shown in Figure 1.12. When replacing a laptop motherboard, you almost always need to use one from the exact same model, otherwise it won't fit inside the case.

- **Figure 1.12** Dell laptop motherboard
![[Image 1.12.png]]

Nearly all laptop processors are soldered onto the motherboard, so you don't have to worry about CPU socket compatibility. If the CPU dies,  you replace the entire motherboard. 

### Power Connectors

In addition to these sockets and slots on the motherboard, a special connector (the 24-pin white block connector shown in Figure 1.14) allows the motherboard to be connected to the power supply to receive power. This connector is where the ATX power connector plugs in.

- **Figure 1.13** An ATX power connector on a motherboard
![[Image 1.13.png]]

#### Onboard Nonvolatile Storage Connectors

Nearly all users store data, and the most widely used data storage device is a hard drive. Hard drives are great because they store data even when the device is powered off, which explains why they are sometimes referred to as nonvolatile storage. There are multiple types of hard drives, and of course, those drives need to connect to the motherboard, and that's what we'll cover here.

##### Integrated Drive Electronics/Parallel ATA

At one time, integrated drive electronics (IDE) drives were the most common type of hard drive found in computers. Though often thought of in relation to hard drives, IDE was much more than a hard drive interface; it was also a popular interface for many other drive types, including optical drives and tape drives. Today, we call it IDE Parallel ATA (PATA) and consider it to be a legacy technology. Figure 1.14 shows two PATA interfaces; you can see that one pin in the center is missing (as a key) to ensure that the cable gets attached properly. The industry now favors Serial ATA instead.

- **Figure 1.14** Two PATA hard drive connectors
![[Image 1.14.png]]

##### Serial ATA

Serial ATA (SATA) began as an enhancement to the original ATA specifications, also known as IDE and, today, PATA. Technology is proving that the orderly progression of data in a single-file path is superior to placing multiple bits of data in parallel and trying to synchronize their transmission to the point that all of the bits arrive simultaneously. In other words, if you can build faster transceivers, serial transmissions are simpler to adapt to the faster rates than are parallel transmissions.

The first version of SATA, known as SATA 1.5 Gbps (and also by the less-preferred terms SATA I and SATA 150), used an 8b/10b-encoding scheme that requires 2 non-data overhead bits for every 8 data bits. The result is a loss of 20% of the rated bandwidth. The silver lining, however, is that the math becomes quite easy. Normally, you have to divide by 8 to convert bits to bytes. With 8b/10b encoding, you divide by 10. Therefore, the 150 MBps throughput for which this version of SATA was nicknamed is easily derived as 1/10 of the 1.5 Gbps transfer rate. The original SATA specification also provided for hot swapping at the discretion of the motherboard and drive manufactures.  

Similar math works for SATA 3 Gbps, tagged as SATA II and SATA 300, and SATA 6 Gbps, which you might hear called SATA III or SATA 600. Note that each subsequent version doubles the throughput of the previous version. Figure 1.16 shows 4 SATA headers on a motherboard that will receive the data cable. Note that identifiers silkscreened onto motherboards often enumerate such headers. The resulting numbers are not related to the SATA version that the header supports. Instead, such numbers serve to differentiate headers from one another and to map to firmware identifiers, often visible within the BIOS configuration utility.

Another version of SATA that you will see is external SATA (eSATA). As you might expect based upon the name, this technology was developed for devices that reside outside of the case, not inside it. Many motherboards have an eSATA connector built in. If not, you can buy an expansion card that has eSATA ports and plugs into internal SATA connectors. Figure 1.16 shows an example of how the two ports are different. Finally, SATA and eSATA standards are compatible. In other words, SATA 6 Gbps equals eSATA 6 Gbps.

- **Figure 1.15** Four SATS headers
![[Image 1.15.png]]

- **Figure 1.16** SATA (left) and eSATA (right) cables and ports 
![[Image 1.16.png]]

> [!info] Note
> SATA and eSATA ports do not provide power, like USB does. Therefore, when connecting SATA and eSATA drives, a separate power connection is required in addition to the data cable.

##### M.2

The most recent development in expansion connectors is M.2 (pronounced "M dot 2"). So far it's primarily used for hard drives, but other types of devices, such as Wi-Fi, Bluetooth, Global Positioning System (GPS), and near-field communication (NFC) adapters are built for M.2 as well. 

It's important to call out that M.2 is a form factor, not a bus standard. The form factor supports existing SATA, USB, and PCIe buses. This means that if you hook up a SATA device to an M.2 slot (with the appropriate connector), the device speed will be regulated by SATA standards. Figure 1.17 shows 2 M.2 connectors on a motherboard.

- **Figure 1.17** Two M.2 slots
![[Image 1.17.png]]

> [!info] Note
> M.2 is closely associated with hard drives, and the M.2 form factor is also in CompTIA A+ exam objective 3.3, “Given a scenario, select and install storage devices.” Because of that, we will go into more depth about M.2 and hard drive data transfer speeds in Chapter 2 when we discuss solid-state drives (SSDs).

### Motherboard Headers

From the time of the very first personal computer, there has been a minimum expectation as to the buttons and LEDs that should be easily accessible to the user. At first, they generally appeared on the front of the case. In today's cases, buttons and LEDs have been added and placed on the top of the case of on a beveled edge between the top and the front. They have also been left on the front or have been used in a combination of these locations. These buttons and lights, as well as other external connectors, plug into the motherboard through a series of pins known as headers. Examples of items that are connected using a header include:

- Power button
- Power light
- Reset button
- Drive activity lights
- Audio jacks
- USB ports

Headers for different connections are often spread throughout different locations on the motherboard—finding the right on can sometimes be a frustrating treasure hunt. Other headers are grouped together. For example, most of the headers for the items on the front or top panel of the case are often co-located. The purpose for the header will be printed on the motherboard, and while that may tell you what should connect there, it often lacks detail in how it should be connected. The motherboard manufacturer's website is a good place to go if you need a detailed diagram or instructions. Figure 1.18 shows several headers on a motherboard. On the left is a USB header, then a system fan header in the center, and a block of front panel headers on the right, including the hard drive light, reset button, chassis intrusion detector, and power light.

- **Figure 1.18** Motherboard headers
![[Image 1.18.png]]

#### Power Button and Light

Users expect a power button to turn the computer on. (These were on the side or back of very early PCs.) The soft power feature available through the front power button, which is no more than a relay, allows access to multiple effects through the contact on the motherboard, based on how long the button is pressed. These effects can be changed through the BIOS or operating system. Users also expect a power light, often a green LED, to assure them that the button did its job.

#### Reset Button 

The reset button appeared as a way to reboot the computer from a cold startup point without removing power from the components. Keeping the machine powered tends to prolong the life of the electronics affected by power cycling. Pressing the reset button also gets around software lockups because the connection to the motherboard allows the system to restart from the hardware level. One disadvantage to power cycling is that certain circuits, such as memory chips, might need time to drain their charge for the reboot to be completely successful. This is why there is always a way to turn the computer off as well.

#### Drive Activity Light

In the early days of personal computing, the hard disk drive's LED had to be driven by the drive itself. Before long, the motherboard was equipped with drive headers, so adding pins so drive the drive activity light was no issue. These days, all motherboards supply this connectivity. The benefit of having one LED for all internal drives is that all the drives are represented on the front panel when only one LED is provided. The disadvantage might be that you cannot tell which drive is currently active. This tends to be a minor concern because you often know which drive you've accessed. If you haven't intentionally accessed any drive, it's likely the drive that holds the operating system or virtual-memory swap file is being accessed by the system itself. In contrast, external drives with removable media, such as optical drives, supply their own activity light on their faceplate.

#### Audio Jacks

Early generations of optical drives had to have a special cable attached to the rear of the drive, which was then attached to the sound card if audio CDs were to be heard through the speakers attached to the sound card. Sound emanating from a CD-ROM running an application, such as a game, did not have to take the same route and could travel through the same path from the drive as general data. The first enhancement to this arrangement came in the form of a front 3.5 mm jack on the drive's faceplate that was intended for headphones but could also have speakers connected to it. The audio that normally ran across the special cable was rerouted to the front jack when something was plugged into it.

Many of today's motherboards have 10-position pin headers designed to connect to standardized front-panel audio modules. Some of these modules have legacy AC'97 analog ports on them, whereas others have high-definition (HD) audio connections. Motherboards that accommodate both have a BIOS setting that enables you to choose which header you want to activate, with the HD setting most often being the default.

#### USB Ports

So many temporarily attached devices feature USB connectivity, such as USB keys (flash drives) and cameras, that front-panel connectivity is a must. Finding your way to the back of the system unit for a brief connection is hardly worth the effort in some cases. For many years, motherboards have supplied one or more 10-position headers for internal connectivity of front-panel USB ports. Because this header size is popular for many connectors, only 9 positions tend to have pins protruding, while the 10th position acts as a key, showing up in different spots for each connector type to discourage the connection of the wrong cable. Figure 1.19 shows USB headers on a motherboard. The labels "USB56" and "USB78" indicate that one block serves ports 5 and 6, while the other serves ports 7 and 8, all of which are arbitrary, based on the manufacturer's numbering convention. In each, the upper left pin is "missing" which is the key.

- **Figure 1.19** Two motherboard USB headers
![[Image 1.19.png]]

### BIOS/UEFI and the POST Routine

Firmware is the name given to any software that is encoded in hardware, usually a read-only memory (ROM) chip, and it can be run without extra instructions from the operating system. Most computers, large printers, and devices with no operating system use firmware in some sense. The best example of firmware is a computer's Basic Input/Output System (BIOS), which is burned into a chip. Also, some expansion cards, such as SCSI cards and graphics adapters, use their own firmware utilities for setting up peripherals.

The BIOS chip, also referred to as the ROM BIOS chip, is one of the most important chips on the motherboard. This special memory chip contains the BIOS system software that boots the system and allows the operating system to interact with certain hardware in the computer in lieu of requiring a more complex device driver to do so. The BIOS chip is easily identified: If you have a brand-name computer, this chip might have on it the name of the manufacturer and usually the word BIOS. For clones, the chip usually has a sticker or printing on it from one of the major BIOS manufacturers (AMI, Phoenix, Award, Winbond, and others). On later motherboards, the BIOS might be difficult to identify or it might even be integrated into the Southbridge, but the functionality remains regardless of how it's implemented.

The successor to the BIOS is the Unified Extensible Firmware Interface (UEFI). The extensible features of the UEFI allow for the support of a vast array of systems and platforms by allowing the UEFI access to system resources for storage of additional modules that can be added at any time. Technologies such as Secure Boot would not be possible with the classic BIOS. It is the extensibility of the UEFI that makes such technology feasible.

Figure 1.20 gives you an idea of what a modern BIOS/UEFI chip might look like on a motherboard. Despite the 1998 copyright on the label, which refers only to the oldest code present on the chip, this particular chip can be found on motherboards produced as late as 2009. Notice also the Reset CMOS jumper at the lower left and its configuration silkscreen at the upper left. You might use this jumper to clear the CMOS memory, when an unknown password, for example, is keeping you out of the BIOS/UEFI configuration utility. The jumper in the photo is in clear position, not the normal operating position. System bootup is typically not possible in this state.

- **Figure 1.20** A BIOS chip on a motherboard
![[Image 1.20.png]]

At a basic level, the BIOS/UEFI controls system boot options such as the sequence of drives from which it will look for operating system boot files. The boot sequence menu from a BIOS/UEFI is shown in Figure 1.21. Other interface configuration options will be available too, such as enabling or disabling integrated ports of and integrated video card. A popular option on corporate computers is to disable USB ports, which can increase security and decrease the risk of contracting a virus.

- **Figure 1.21** BIOS boot sequence
![[Image 1.21.png]]

Most BIOS/UEFI setup utilities have more to offer than a simple interface for making selections and saving the results. For example, these utilities often offer diagnostic routines that you can use to have the BIOS/UEFI analyze the state and quality of the same components that it inspects during bootup, but at a much deeper level.

Consider the scenario where a computer is making noise and overheating. You can use the BIOS/UEFI configuration utility to access built-in diagnostics to check the rotational speed of the motherboard fans. If the fans running slower than expected, the noise could be related to the bearings of one or more fans, causing them to lose speed and, thus,
cooling capacity.

There is often also a page within the utility that gives you access to such bits of information as current live readings of the temperature of the CPU and the ambient temperature of the interior of the system unit. On such a page, you can set the temperature at which the BIOS/UEFI sounds a warning tone and the temperature at which the BIOS/UEFI shuts down the system to protect it. You can also monitor the instantaneous fan speeds, bus speeds, and voltage levels of the CPU and other vital landmarks to make sure that they are all within acceptable ranges. You might also be able to set a lower fan speed threshold at which the system warns you. In many cases, some of these levels can be altered to achieve such phenomena as overclocking, which is using the BIOS/UEFI to set the system clock higher than what the CPU is rated for, or undervolting, which is lowering the voltage of the CPU and RAM, which reduces power consumption and heat production.

### BIOS/UEFI Security and Encryption 

The BIOS/UEFI has always played a role in system security. Since the early days of the personal computer, the BIOS allowed the setting of 2 passwords—the user (or boot) password and the supervisor/administrator, or access, password. The boot password is required to leave the initial power-on screens and begin the process of booting an operating system. The administrator password is required before entering the BIOS/UEFI configuration utility. It is always a good idea to set the administrator password, but the boot password should not be set on public systems that need to boot on their own, in case of an unforeseen power cycle.

In more recent years, the role of the BIOS/UEFI in system security has grown substantially. BIOS/UEFI security has been extended to a point where the operating system is ready to take it over. The BIOS/UEFI was a perfect candidate to supervise security and integrity in a platform-independent way. Coupled with the Trusted Platform Module (TPM), a dedicated security coprocessor, or cryptoprocessor, the BIOS can be configured to boot the system only after authenticating the boot device. This authentication confirms that the hardware being booted to has been tied to the system containing the BIOS/UEFI and TPM, a process known as sealing. Sealing the devices to the system also prohibits the devices from being used after removing them from the system. For further security, the keys created can be combined with a PIN or password that unlocks their use or with a USB flash drive that must be inserted before booting.

Microsoft's BitLocker uses the TPM to encrypt the entire drive. Normally, only user data can be encrypted, but BitLocker encrypts operating system files, the Registry, the hibernation file, and so on, in addition to those files and folders that file-level encryption secures. If any changes have occurred to the Windows installation, the TPM does not release the keys required to decrypt and boot to the secured volume. TPM is configured in Windows under Start > Settings > Update & Security > Windows Security > Device Security, as shown in Figure 1.22.

Most motherboards come with a TPM chip installed, but if they don't, it's not possible to add one. In those situations, you can enable the same functionality by using a hardware security module (HSM). An HSM is a security device that can manage, create, and securely store encryption keys—it enables users to safely encrypt and decrypt data. An HSM cat take a few different forms. The simplest is a USB or PCIe device that plugs into a system. It could be set up for file encryption and decryption, required for the computer to boot, or both. For large scale-solutions, HSM-enabled servers can provide crypto services to an entire network.

When a certain level of UEFI is used, the system firmware can also check digital signatures for each boot file is uses to confirm that it is the approved version and has not been tampered with. This technology is known as Secure Boot. An example of a BIOS/UEFI's boot security screen is shown in Figure 1.23. The boot files checked include option ROMs, the boot loader, and other operating-system boot files. Only if the signatures are valid will the firmware load and execute the associated software.

- **Figure 1.22** Windows TPM configuration screen
![[Image 1.22.png]]

- **Figure 1.23** Secure boot in UEFI
![[Image 1.23.png]]

The problem can now arise that a particular operating system might not be supported by the database of known-good signatures stored in the firmware. In such a situation, the system manufacturer can supply an extension that the UEFI can use to support that operating system—a task not possible with traditional BIOS-based firmware.

>[!info] Note
> LoJack for Laptops is a UEFI-enabled security system developed by Absolute Software. It performs similarly to other UEFI security methods already discussed, such as drive encryption, but adds a few features. For example, LoJack can remotely track stolen laptops as well as lock and delete certain files. 

Some BIOS firmware can monitor the status of a contact on the motherboard for intrusion detection. If the feature in the BIOS is enabled and the sensor on the chassis is connected to the contact on the motherboard, the removal of the cover will be detected and logged by the BIOS. This can occur even if the system is off, thanks to the CMOS battery. At the next bootup, the BIOS will notify you of the intrusion. No notification occurs over subsequent boots unless the additional intrusion is detected.

### POST

A major function of the BIOS/UEFI is to perform a process known as a power-on self-test (POST). POST is a series of system checks performed by the system BIOS/UEFI and other high- end components, such as the SCSI BIOS and the video BIOS, known collectively as option ROMs. Among other things, the POST routine verifies the integrity of the BIOS/UEFI itself. It also verifies and confirms the size of primary memory. During POST, the BIOS also analyzes and catalogs other forms of hardware, such as buses and boot devices, as well as manages the passing of control to the specialized BIOS/UEFI routines mentioned earlier. The BIOS/UEFI is responsible for offering the user a key sequence to enter the configuration routine as POST is beginning. Finally, once POST has completed successfully, the BIOS/UEFI selects the boot device highest in the configured boot order and executes the master boot record (MBR) or similar construct on that device so that the MBR can call its associated operating system’s boot loader and continue booting up.

The POST process can end with a beep code or displayed code that indicates the issue discovered. Each BIOS/UEFI publisher has its own series of codes that can be generated. Figure 1.24 shows a simplified POST display during the initial boot sequence of a computer.

- **Figure 1.24** An example of a system POST screen
![[Image 1.24.png]]

>[!info] Flashing the System BIOS/UEFI
> If ever you find that a hardware upgrade to your system is not recognized, even after the latest and correct drivers have been installed, perhaps a BIOS/UEFI upgrade, also known as flashing the BIOS, is in order. Only certain hardware benefits from a BIOS/UEFI upgrade, such as drives and a change of CPU or RAM types. Very often, this hardware is recognized immediately by the BIOS/UEFI and has no associated driver that you must install. So, if your system doesn’t recognize the new device, and there’s no driver to install, the BIOS/ UEFI is a logical target.
>
> >
>
> Let’s be clear about the fact that we are not talking about entering the BIOS/UEFI setup utility and making changes to settings and subsequently saving your changes before exiting and rebooting. What we are referring to here is a replacement of the burned- in code within the BIOS itself. You might even notice after the upgrade that the BIOS setup utility looks different or has different pages and entries than before.
>
>>
>
> On older systems and certain newer ones, a loss of power during the upgrade results in catastrophe. The system becomes inoperable until you replace the BIOS/UEFI chip, if possible, or the motherboard itself. Most new systems, however, have a fail-safe or two. This could be a portion of the BIOS/UEFI that does not get flashed and has just enough code to boot the system and access the upgrade image. It could be a passive section to which the upgrade is installed and switched to only if the upgrade is successful. Sometimes this is controlled on screen. At other times, there may be a mechanism, such as a jumper, involved in the recovery of the BIOS/UEFI after a power event occurs. The safest bet is to make sure that your laptop has plenty of battery power and is connected to AC power or your desktop is connected to an uninterruptible power supply (UPS).
>
>>
>
> In all cases, if you think you need a BIOS/UEFI upgrade, do not consult the BIOS/UEFI manufacturer. Instead, go to the motherboard or system manufacturer and check its website. The motherboard or system manufacturer vendors have personalized their BIOS/UEFI code after licensing it from the BIOS/UEFI publisher. The vendor will give you access to the latest code as well as the appropriate flashing utility for its implementation.

### CMOS and CMOS Battery

Your PC has to keep certain settings when it’s turned off and its power cord is unplugged: 

- Date
- Time
- Hard drive/optical drive configuration
- Memory
- CPU settings, such as overclocking
- Integrated ports (settings as well as enable/disable)
- Boot sequence
- Power management
- Virtualization support
- Security (passwords, Trusted Platform Module settings, LoJack)

Consider a situation where you added a new graphics adapter to your desktop computer, but the built-in display port continues to remain active, prohibiting the new interface from working. The solution might be to alter your BIOS/UEFI configuration to disable the internal graphics adapter, so that the new one will take over. Similar reconfiguration of your BIOS/UEFI settings might be necessary when overclocking—or changing the system clock speed—is desired, or when you want to set BIOS/UEFI-based passwords or establish TPM- based whole-drive encryption, as with Microsoft’s BitLocker. While not so much utilized today, the system date and time can be altered in the BIOS/UEFI configuration utility of your system; once, in the early days of personal computing, the date and time actually might have needed to be changed this way.

Your PC keeps these settings in a special memory chip called the complementary metal oxide semiconductor (CMOS) memory chip. Actually, CMOS (usually pronounced see- moss) is a manufacturing technology for integrated circuits. The first commonly used chip made from CMOS technology was a type of memory chip, the memory for the BIOS/UEFI. As a result, the term CMOS stuck and is the accepted name for this memory chip.

The BIOS/UEFI starts with its own default information and then reads information from the CMOS, such as which hard drive types are configured for this computer to use, which drive(s) it should search for boot sectors, and so on. Any overlapping information read from the CMOS overrides the default information from the BIOS/UEFI. A lack of corresponding information in the CMOS does not delete information that the BIOS knows natively. This process is a merge, not a write-over. CMOS memory is usually not upgradable in terms of its capacity and might be integrated into the BIOS/UEFI chip or the Southbridge.

>[!info] Note
> Although there are technical differences, in the real world the terms BIOS/UEFI and CMOS (and BIOS/UEFI chip and CMOS chip) are used interchangeably. You will hear someone say, Did you check the BIOS/UEFI? or, Did you check CMOS settings? and they’re referring to the same thing. Even though it’s an oversimplification, most people feel comfortable with thinking about the BIOS/UEFI as the firmware that controls the boot process, whereas CMOS is the chip itself. It’s incredibly unlikely that the A+ exam or any person is going to ask you to differentiate between the two, unless you get a job focusing specifically on those technologies.

To keep its settings, integrated circuit-based memory must have power constantly. When you shut off a computer, anything that is left in this type of memory is lost forever. The CMOS manufacturing technology produces chips with very low power requirements. As a result, today’s electronic circuitry is more susceptible to damage from electrostatic discharge (ESD). Another ramification is that it doesn’t take much of a power source to keep CMOS chips from losing their contents.

To prevent CMOS from losing its rather important information, motherboard manufacturers include a small battery called the CMOS battery to power the CMOS memory, shown in the bottom-left corner of Figure 1.25. The batteries come in different shapes and sizes, but they all perform the same function. Most CMOS batteries look like large watch batteries or small cylindrical batteries. Today’s CMOS batteries are most often of a long-life, non-rechargeable lithium chemistry.

- **Figure 1.25** CMOS battery
![[Image 1.25.png]]

> [!info] Note
> There’s a lot to know about motherboards—they are complex devices that connect everything together inside the computer! For the A+ exam, remember that you will need to be familiar with the following concepts:
> - Form factors, such as ATX and ITX
> - Connector types including PCI, PCIe, power, SATA, eSATA, M.2, and headers
> - Compatibility concerns such as AMD and Intel CPU sockets and different board types such as server, multisocket, desktop, and mobile
> - BIOS/UEFI boot options, USB permissions, TPM, fan configurations, secure boot, boot passwords
> - Security and encryption using TPM and HSM
