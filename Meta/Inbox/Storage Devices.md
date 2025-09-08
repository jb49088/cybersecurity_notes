
# Storage Devices

What good is a computer without a place to put everything? Storage media hold the files that the operating system needs to operate and the data that users need to save. What about saving to the cloud? The computers that make up the cloud, rather than the local computer, hold the storage media. The many different types of storage media differ in terms of their capacity (how much they can store), access time (how fast the computer can access the information), and the physical type of media used. 

## Hard Disk Drive Systems

Hard disk drive (HDD) systems (or hard drives for short) are used for permanent storage and quick access. Hard drives typically reside inside the computer, where they are 
semi-permanently mounted with no external access (although there are external and removable hard drives) and can hold more information than other forms of storage. Hard drives use a magnetic storage medium, and they are known as conventional drives to differentiate them from newer solid-state storage media.

The hard disk drive system contains the following three critical components:

- **Controller:** This component controls the drive. The controller chip controls how the drive operates and how the data is encoded onto the platters. It controls how the data sends signals to the various motors in the drive and receives signals from the sensors inside the drive. Nearly all hard disk drive technologies incorporate the controller and drive into one assembly. Today, the most common and well known of these technologies is Serial Advanced Technology Attachment (SATA).
- **Hard Disk:** This is the physical storage medium. Hard disk drive systems store information on small discs (from under 1 inch to 5 inches in diameter), also called platters, stacked together and placed in an enclosure. 
- **Host Bus Adapter:** The host bus adapter (HBA) is the translator, converting signals from the controller to signals that the computer can understand. Most motherboards today incorporate the host adapter into the motherboard’s circuitry, offering headers for drive- cable connections. Legacy host adapters and certain modern adapters house the hard drive controller circuitry. 

Figure 1.48 shows a hard disk drive and host adapter. The hard drive controller is integrated into the drive in this case, but it could reside on the host adapter in other hard drive technologies. This particular example shows a hard drive plugging into an expansion card. Today’s drives almost always connect straight to the motherboard, again with the HBA being integrated with the drive itself.
 
- **Figure 1.48** A hard disk drive system
![[Image 1.48.png]]

Hard drives, regardless of whether they are magnetic or solid- state, most often connect to the motherboard’s SATA or Parallel Advanced Technology Attachment (PATA) interfaces. You learned about SATA and PATA in Chapter 1, but Figure 1.49 provides a reminder of what the interfaces look like; SATA is on the top.

The back of the hard drive will have data and power connectors. Figure 2.9 shows the data and power connectors for a PATA drive and a SATA drive.

- **Figure 1.49** Four SATA and two PATA ports
![[Image 1.49.png]]

Today, IDE (PATA) hard drives are essentially obsolete. Most of that is due to the limitations in transfer speeds. Most PATA hard drives follow the ATA/100 standard, which has a maximum transfer speed of 100 MBps. There are faster ATA standards, such as ATA/133 and ATA/167, but drives using those standards are rare. SATA III (also known as SATA 6 Gb/s), on the other hand, has a maximum transfer speed of 600 MBps.

> [!info] Note 
> There’s another hard drive connector type called SAS, or Serial Attached SCSI. (SCSI is pronounced “scuzzy” and stands for Small Computer System Interface—aren’t acronyms within acronyms great?) SAS tends to be a bit faster than SATA, and it’s used mostly in enterprise computing applications. You won’t see many SAS ports on conventional desktop or laptop motherboards. SAS is not on the A+ exam objectives, but it is on the A+ acronym list.

- **Figure 1.50** PATA (top) and SATA (bottom) hard drive data and power connectors
![[Image 1.50.png]] 

### Anatomy of a Hard Drive

A hard drive is constructed in a cleanroom to avoid the introduction of contaminants into the hermetically sealed drive casing. Once the casing is sealed, most manufacturers seal one or more of the screws with a sticker warning that removal of or damage to the seal will result in voiding the drive’s warranty. Even some of the smallest contaminants can damage the precision components if allowed inside the hard drive’s external shell. The following is a list of the terms used to describe these components in the following paragraphs:

- Platters
- Read/write heads
- Tracks
- Sectors
- Cylinders
- Clusters (allocation units)

Inside the sealed case of the hard drive lie one or more platters, where the actual data is stored by the read/write heads. The heads are mounted on a mechanism that moves them in tandem across both surfaces of all platters. Older drives used a stepper motor to position the heads at discrete points along the surface of the platters, which spin at thousands of revolutions per minute on a spindle mounted to a hub. Newer drives use voice coils for a more analog movement, resulting in reduced data loss because the circuitry can sense where the data is located through a servo scheme, even if the data shifts due to changes in physical disc geometry. Figure 1.51 shows the internal components of a conventional hard drive.

- **Figure 1.51** Anatomy of a hard drive
![[Image 1.51.png]]

Before a hard drive can store data, it must be prepared. Factory preparation for newer drives, or low-level formatting in the field for legacy drives, maps the inherent flaws of the platters so that the drive controllers know not to place data in these compromised locations. Additionally, this phase in drive preparation creates concentric rings, or tracks, which are drawn magnetically around the surface of the platters. Sectors are then delineated within each of the tracks. Sectors are the magnetic domains that represent the smallest units of storage on the disk’s platters. This is illustrated in Figure 1.52. Magnetic- drive sectors commonly store only 512 bytes (½ KB) of data each. 

- **Figure 1.52** Cylinders, tracks, and sectors
![[Image 1.52.png]]

The capacity of a hard drive is a function of the number of sectors it contains. The controller for the hard drive knows exactly how the sectors are laid out within the disk assembly. It takes direction from the BIOS when writing information to and reading information from the drive. The BIOS, however, does not always understand the actual geometry of the drive. For example, the BIOS does not support more than 63 sectors per track. Nevertheless, almost all hard drives today have tracks that contain many more than 63 sectors per track. As a result, a translation must occur from where the BIOS believes it is directing information to be written to where the information is actually written by the controller. When the BIOS detects the geometry of the drive, it is because the controller reports dimensions that the BIOS can understand. The same sort of trickery occurs when the BIOS reports to the operating system a linear address space for the operating system to use when requesting that data be written to or read from the drive through the BIOS.

After initial drive preparation, the drive is formatted with a file system, by the operating system, and then it’s ready to store data. Filesystems laid down on the tracks and their sec- tors routinely group a configurable number of sectors into equal or larger sets called clusters or allocation units. This concept exists because operating system designers have to settle on a finite number of addressable units of storage and a fixed number of bits to address them uniquely.

No two files are allowed to occupy the same sector, so the opportunity exists for a waste of space if small files occupy only part of a sector. Clusters exacerbate the problem by having a similar foible: the operating system does not allow any two files to occupy the same cluster. Thus, the larger the cluster size, the larger the potential waste. So although you can increase the cluster size (generally to as large as 64 KB, which corresponds to 128 sectors), you should keep in mind that unless you are storing a notable number of very large files, the waste will escalate astoundingly, perhaps negating or reversing your perceived 
storage-capacity increase.  

### HDD Speeds

As the electronics within the HBA and controller get faster, they are capable of requesting data at higher and higher rates. If the platters are spinning at a constant rate, however, the information can be accessed only as fast as a given fixed rate. To make information available to the electronics more quickly, manufacturers increase the speed at which the platters spin from one generation of drives to the next, with multiple speeds coexisting in the marketplace for an unpredictable period, at least until the demand dies down for one or more speeds.

The following spin rates have been used in the industry for the platters in conventional
magnetic hard disk drives:

- 5,400 rpm
- 7,200 rpm
- 10,000 rpm
- 12,000 rpm
- 15,000 rpm

While it is true that a higher revolutions per minute (rpm) rating results in the ability to move data more quickly, there are many applications that do not benefit from increased 
disk-access speeds. As a result, you should choose only faster drives, which are also usually more expensive per byte of capacity, when you have an application for this type of performance, such as for housing the partition where the operating system resides or for very disk- intensive programs. For comparison, a 7,200 rpm SATA hard drive can sustain data read speeds of about 100 MBps, which is about the same as a PATA ATA/100 7,200 rpm drive. A 10,000 rpm (also known as 10k) SATA drive can top out around 200 MBps.

> [!info] Note
> All 15,000 rpm drives are SAS drives, not SATA or PATA drives.

Higher speeds also consume more energy and produce more heat. The lower speeds can be ideal in laptops, where heat production and battery usage can be issues with 
higher-speed drives. Even the fastest conventional hard drives are slower than solid-state drives are at transferring data. 

### HDD Form Factors

Physically, the most common hard drive form factors (sizes) are 3.5" and 2.5". Desktops traditionally use 3.5" drives, whereas the 2.5" drives are made for laptops— although most laptops today avoid using conventional HDDs. Converter kits are available to mount a 2.5" drive into a 3.5" desktop hard drive bay. Figure 1.53 shows the two drives together. As you can see, the 2.5" drive is significantly smaller in all three dimensions, but it does have the same connectors as its bigger cousin.

- **Figure 1.53** A 3.5" and 2.5" hard drive
![[Image 1.53.png]]

## Solid-State Drives

Unlike conventional hard drives, solid-state drives (SSDs) have no moving 
parts—they use the same solid-state memory technology found in the other forms of flash memory. You can think of them as big versions of the flash drives that are so common.

Because they have no moving parts, SSDs are capable of transferring data much more quickly than HDDs could ever dream of doing. Recall from the “HDD Speeds” section that a 10k SATA HDD tops out at about 200 MBps. Even the slowest SSDs will run circles around that. The true speed of an SSD will be determined, of course, by the drive itself, but also the interface to which it’s attached.

And because there’s no need for spinning platters and read/write heads, SSDs can be made much smaller than HDDs, making them better for laptops and portable devices. SSDs have several other advantages over their mechanical counterparts as well, including the following:

- Faster start-up and read times
- Less power consumption and heat produced
- Silent operation
- Generally more reliable because of a lack of moving parts
- Less susceptible to damage from physical shock and heat production
- Higher data density per square centimeter

The disadvantages of SSDs are as follows:

- The technology to build an SSD is more expensive per byte.
- All solid-state memory is limited to a finite number of write (including erase) operations. Lack of longevity could be an issue. As the technology matures, this is becoming less and less of a problem.

You will find that SSDs in the market generally have lower overall capacity than HDDs. For example, it’s not uncommon to find HDDs over 8 TB in size, with 18 TB drives pacing the market. Conversely, the biggest commercially available SSD (as of this writing) is 8 TB.

As for cost, HDDs run about 3 cents per GB and low-end SATA SSDs are about three times as expensive. Faster SSDs such as NVMe drives (which we’ll get to in a minute) can be from four to ten times as expensive. Of course, prices are subject to (and it’s guaranteed they will) change!

When used as a replacement for traditional HDDs, SSDs are expected to behave in a similar fashion, mainly by retaining contents across a power cycle. With SSD, you can also expect to maintain or exceed the speed of the HDD. SSDs can be made faster still by including a small amount of DRAM as a cache.

SSDs come in various shapes and sizes and have a few different interfaces and form factors. 

### Hybrid Drives

A cost-saving alternative to a standard SSD that can still provide a significant increase in performance over conventional HDDs is the hybrid drive. Hybrid drives can be implemented in two ways: a solid-state hybrid drive and a dual-drive storage solution. Both forms of hybrid drives can take advantage of solutions such as Intel’s Smart Response Technology (SRT), which informs the drive system of the most used and highest-value data. The drive can then load a copy of such data into the SSD portion of the hybrid drive for faster read access.

It should be noted that systems on which data is accessed randomly do not benefit from hybrid drive technology. Any data that is accessed for the first time will also not be accessed from flash memory, and it will take as long to access it as if it were accessed from a traditional hard drive. Repeated use, however, will result in the monitoring software’s flagging of the data for caching in the SSD.

#### Solid-State Hybrid Drive

The solid-state hybrid drive (SSHD) is a conventional HDD manufactured with a substantial amount of flash memory–like solid-state storage aboard. The SSHD is known to the operating system as a single drive, and individual access to the separate components is unavailable to the user.

#### Dual-Drive Solutions

Dual-drive storage solutions can also benefit from technologies such as Intel’s SRT. However, because they are implemented as two separate drives (one conventional HDD and one SSD), each with its own separate file system and drive letter, the user can also manually choose the data to move to the SSD for faster read access. Users can choose to implement dual-drive systems with SSDs of the same size as the HDD, resulting in a fuller caching scenario.

### SSD Communication Interfaces

It’s been said that the advent of the SSD was a major advancement for the computer industry. Solid-state drives are basically made from the same circuitry that RAM is, and they are really, really fast. When they were first on the market, the limitation in the system was the SATA controller that most hard drives were plugged into. So as enterprising computer engineers are known to do, some started looking into ways to overcome this barrier. The result is that there have been more interfaces designed for storage devices, with much faster speeds.

The CompTIA A+ exam objectives list three technologies as SSD communications interfaces: SATA, PCIe, and NVMe. We will cover them now.

#### SATA

At this point, SATA is a technology you should be somewhat familiar with. We covered it in Chapter 1, and the interface is shown earlier in this chapter in Figure 2.8. SATA is a bit unique among the other subjects in this SSD section because it can support mechanical hard drives as well as SSDs.

SSDs came onto the market in the mid-1990s before SATA was even a thing, but they were limited in popularity because of the major bottleneck—the PATA communications interface. Once SATA came along in the early 2000s, the two technologies felt like glorious companions. SATA 1.x could transfer data at 150 MBps, which was a lot faster than the conventional hard drives at the time (the most common conventional standard was ATA/100, which maxed out at 100 MBps). Then, of course, came SATA 2.x (300 MBps) and eventually SATA 3.x (600 MBps). Comparatively, conventional hard drives appear to be painfully slow. And they are.

Keep in mind that of all the SSD technologies we discuss in this chapter, the SATA interface is the slowest of them. So while SATA SSDs are about 6x faster than conventional HDDs, there is a lot of performance upside. SATA SSDs are still popular today because they are plentiful and cheap (compared to other SSDs), and motherboards usually have more SATA connectors than any other type of hard drive connector.

#### PCIe

Peripheral Component Interconnect Express (PCIe) is another technology that was covered in Chapter 1 and is used for SSDs. PCIe was first introduced in 2002, technically a year before SATA, and both technologies took a little while to get widely adopted. Like SATA, PCIe has gone through several revisions, with each version being faster than the previous one. Table 2.1 shows the throughput of PCIe versions.

![[Table 1.07|no-link no-title clean]]

> [!info] Note
> PCIe 6.0 is under development and is either coming soon or already released, depending on when you read this book. It doubles the transfer rate to 64.0 GT/s and improves encoding and error correction, helping total throughput. It is backward compatible with older PCIe standards.

Looking at Table 2.1, something might immediately jump out at you. The transfer rate is specified in gigatransfers per second (GTps). This unit of measure isn’t very commonly used, and most people talk about PCIe in terms of its data throughput. Before moving on, though, let’s take a quick look at what GTps means. (It’s highly unlikely you will be tested on this, but you might be curious.)

PCIe is a serial bus that embeds clock data into the data stream to help the sender and receiver keep track of the order of transmissions. Two clock bits are used for every eight bits of data. Therefore, PCIe uses what’s called “8b/10b” encoding—8 bits of data are sent in a 10-bit bundle, which is decoded at the receiving end. Gigatransfers per second (GTps) refers to the total number of bits sent, whereas the throughput data you might be more used to seeing refers to data only and not the clock.

> [!info] Note
> A little math using PCIe 1.0 might help illustrate the transfer rate versus data throughput. PCIe 1.0 has a transfer rate of 2.5 billion (giga) bits per second. Because it uses 8b/10b encoding, you then multiply by 0.8 (8/10) to get to bits of data, which is 2 trillion. But that’s bits. Divide that by 8 to turn it into bytes, and you are left with 250 million bytes, or 250 MBps. Again, don’t expect to see this on the test, but we know that some of you like these technical details!

Also remember that PCIe cards can have different numbers of channels—x1, x2, x4, x8, and x16. So, for example, a PCIe 3.0 x4 card will have total data throughput of 8 GBps (1 GBps for one lane in one direction, times two for bidirectional, times four for the four channels).

What does all of this mean for SSDs? First, take a look at a picture of a PCIe SSD in Figure 1.54. This is a PCIe 2.0 x4 Kingston HyperX Predator. These drives came in capacities up to 960 GB and supported data reads of up to 2.64 GBps and maximum write speeds of 1.56 GBps. The drive is a little dated by today’s standards, but it still serves as a great example. First, it’s the most common PCIe SSD size, which is x4. PCIe x2 drives are also common, with x8 and x16 drives being relatively rare. Second, notice the transfer speeds. Based on Table 2.1, PCIe 2.0 x4 has a maximum throughput of 4 GBps. This drive doesn’t get to that level, especially on write speeds. This is the difference between theoretical maximums of standards versus practical realities of creating hardware. Even so, you can see that this PCIe SSD is significantly faster than a SATA SSD.

- **Figure 1.54** Kingston PCIe x4 SSD
![[Image 1.55.png]]

> [!info] Note
> Remember that, unlike SATA, which is designed for storage devices such as hard drives and optical drives, PCIe is more of a universal connector. Video cards, sound cards, network cards, and many other devices use PCIe slots as well. Before attempting to install a PCIe hard drive into a computer, make sure that there’s an open PCIe slot of the appropriate type first! 

#### NVMe

Created by a consortium of manufacturers, including Intel, Samsung, Dell, SanDisk, and Seagate, and released in 2011, Non-Volatile Memory Express (NVMe) is an open standard designed to optimize the speed of data transfers. Unlike SATA and PCIe, NVMe isn’t related to a specific type of connector. Said another way, there is no NVMe connector—think of it as a nonvolatile memory chip that can be used in SATA, PCIe, or M.2 (which we will cover in the next section) slots. Figure 1.55 shows a 1 TB Western Digital NVMe SSD. 

- **Figure 1.55** M.2 NVMe SSD
![[Image 1.55.png]]

NVMe drives are frighteningly fast—current NVMe SSDs can support data reads of up to 3.5 GBps, provided that the interface they are plugged into supports it as well, of course. An NVMe SATA 3 SSD will still be limited to 600 MBps; older PCIe versions in theory might have limitations, but you’re not going to find any PCIe 1.0 or 2.0 NVMe SSDs, so it’s not a problem.

One potential issue you might see with NVMe hard drives is that in order to be a boot drive, the motherboard must support it. If the motherboard has a built-in M.2 slot, odds are that the BIOS will support booting from an NVMe drive. If you are adding it using a PCIe port, the BIOS might not be able to boot from that drive. Always check the motherboard documentation to ensure it supports what you’re trying to do.

### SSD Form Factors

Whereas a communications interface is the method the device uses to communicate with other components, a form factor describes the shape and size of a device. The two SSD form factors you need to know for the A+ exam are mSATA and M.2.

#### mSATA

The Serial ATA International Organization has developed several specifications—you’ve already been introduced to SATA and eSATA. Next on the list is a form factor specifically designed for portable devices such as laptops and smaller—mini-Serial ATA (mSATA). mSATA was announced in 2009 as part of SATA version 3.1 and hit the market in 2010. mSATA uses the same physical layout as the Mini PCI Express (mPCIe) standard, and both have a 30 mm-wide 52-pin connector. The wiring and communications interfaces between the two standards are different though. mSATA uses SATA technology, whereas mPCIe uses PCIe. In addition, mPCIe card types are as varied as their larger PCIe cousins are, including video, network, cellular, and other devices. mSATA, on the other hand, is dedicated to storage devices based on SATA bus standards. mSATA cards come in 30 mm × 50.95 mm full-size and 30 mm × 26.8 mm half-size cards. Figure 1.56 shows a full-sized mSATA SSD on top of a 2.5" SATA SSD.

- **Figure 1.56** mSATA SSD and a 2.5" SATA SSD
![[Image 1.56.png]]

The wiring differences between mSATA and mPCIe can pose some interesting challenges. Both types of cards will fit into the same slot, but it depends on the motherboard as to which is supported. You might have heard us say this before, but as always, check the motherboard’s documentation to be sure. 

#### M.2

Originally developed under the name Next Generation Form Factor (NGFF), M.2 (pronounced “M dot 2”) was born from the desire to standardize small form factor SSD hard drives. We touched briefly on M.2 in Chapter 1, and we mentioned that although M.2 is primarily used for hard drives, it supports other types of cards such as Wi-Fi, Bluetooth, Global Positioning System (GPS), and near-field communication (NFC) connectivity, as well as PCIe and SATA connections. It’s a form factor designed to replace the mSATA standard for ultra-small expansion components in laptops and smaller devices. Whereas mSATA uses a 30mm 52-pin connector, M.2 uses a narrower 22mm 66-pin connector.

One interesting connectivity feature of M.2 is that the slots and cards are keyed such that only a specific type of card can fit into a certain slot. The keys are given letter names to distinguish them from each other, starting with the letter A and moving up the alphabet as the location of the key moves across the expansion card. Table 2.2 explains the slot names, some interface types supported, and common uses.

![[Table 1.09|no-link no-title clean]]

Let’s look at some examples. Figure 2.16 shows four different M.2 cards. From left to right, they are an A- and E-keyed Wi-Fi card, two B- and M-keyed SSDs, and an M-keyed SSD. Of the four, only the M-keyed SSD can achieve the fastest speeds (up to 1.8 GBps) because it supports PCIe x4. SSDs on the market are keyed B, M, or B+M. A B-keyed or M-keyed SSD won’t fit in a B+M socket. However, a B+M keyed drive will fit into a B socket or an M socket.

Another interesting feature of the cards is that they are also named based on their size. For example, you will see card designations such as 1630, 2242, 2280, 22110, or 3042. The first two numbers refer to the width, and the rest to the length (in millimeters) of the card. In Figure 1.58, you see a 1630, a 2242, and two 2280 cards.

Figure 1.58 shows a motherboard with two M.2 slots. The one on the left is E-keyed, and the one on the right is B-keyed. The left slot is designed for an E-keyed Wi-Fi NIC, and the right one for a B-keyed SSD.

- **Figure 1.57** Four M.2 cards
![[Image 1.57.png]]

- **Figure 1.58** M.2 E- keyed and B- keyed slots
![[Image 1.58.png]]

Many motherboards today come with protective covers over the M.2 slots, which provide a bit of safety within the case. An example is shown in Figure 1.59. The bottom M.2 slot is covered, and the top slot (just above the PCIe x4 connector) has the cover removed. Notice the screw holes to support 42 mm, 60 mm, 80 mm, and 110 mm length devices.

- **Figure 1.59** M.2 connectors covered and uncovered
![[Image 1.59.png]]

As mentioned earlier, M.2 is a form factor, not a bus standard. M.2 supports SATA, USB, and PCIe buses. What does that mean for M.2 hard drives? It means that if you purchase an M.2 SATA hard drive, it will have the same speed limitation as SATA III, or about 600 MBps. That’s not terrible, but it means that the primary advantage of an M.2 SATA drive versus a conventional SATA SSD is size. An M.2 PCIe hard drive is an entirely different story. PCIe, you will recall, is much faster than SATA. A PCIe 2.0 x1 bus supports one-way data transfers of 500 MBps. That is close to SATA III speed, and it’s only a single lane for an older standard. NVMe M.2 drives kick up the speed even further. If you want the gold standard for hard drive speed, NVMe M.2 is the way to go.

To wrap up this section on SSDs, let’s look at one more picture showing the difference in sizes between a few options, all from the manufacturer Micron. Figure 2.19 has a 2.5" SSD on top, with (from left to right) a full-sized mSATA drive, an M.2 22110 drive, and an M.2 2280 drive. All are SSDs that can offer the same capacity, but the form factors differ quite a bit from each other.

## RAID

Multiple hard drives can work together as one system, often providing increased performance (faster disk reads and writes) or fault tolerance (protection against one disk failing). Such systems are called Redundant Array of Independent (or Inexpensive) Disks (RAID). RAID can be implemented in software, such as through the operating system, or in hardware, such as through the motherboard BIOS or a RAID hardware enclosure. Hardware RAID is more efficient and offers higher performance but at an increased cost.

- **Figure 1.60** Four different SSDs
![[Image 1.60.png]]

There are several types of RAID. The following are the most commonly used RAID levels:

- **RAID 0:** RAID 0 is also known as disk striping, where a striped set of equal space from at least two drives creates a larger volume. This is in contrast to unequal space on multiple disks being used to create a simple volume set, which is not RAID 0. RAID 0 doesn’t provide the fault tolerance implied by the redundant component of the name. Data is written across multiple drives, so one drive can be reading or writing while another drive’s read- write head is moving. This makes for faster data access. If any one of the drives fails, however, all content is lost. Some form of redundancy or fault tolerance should be used in concert with RAID 0.
- **RAID 1:** Also known as disk mirroring, RAID 1 is a method of producing fault tolerance by writing all data simultaneously to two separate drives. If one drive fails, the other contains all of the data, and it will become the primary drive. Disk mirroring doesn’t help access speed, however, and the cost is double that of a single drive. If a separate host adapter is used for the second drive, the term duplexing is attributed to RAID 1. Only two drives can be used in a RAID 1 array.
- **RAID 5:** RAID 5 combines the benefits of both RAID 0 and RAID 1, creating a redundant striped volume set. Sometimes you will hear it called a stripe set with parity. Unlike RAID 1, however, RAID 5 does not employ mirroring for redundancy. Each stripe places data on n- 1 disks, and parity computed from the data is placed on the remaining disk. The parity is interleaved across all the drives in the array so that neighboring stripes have parity on different disks. If one drive fails, the parity information for the stripes that lost data can be used with the remaining data from the working drives to derive what was on the failed drive and to rebuild the set once the drive is replaced. The same process is used to continue to serve client requests until the drive can be replaced. This process can result in a noticeable performance decrease, one that is predictable because all drives contain the same amount of data and parity. Furthermore, the loss of an additional drive results in a catastrophic loss of all data in the array. Note that while live requests are served before the array is rebuilt, nothing needs to be computed for stripes that lost their parity. Recomputing parity for these stripes is required only when rebuilding the array. A minimum of three drives is required for RAID 5. The equivalent space of one drive is lost for redundancy. The more drives in the array, the less of a percentage this single disk represents.

- **RAID 10:** Also known as RAID 1+0, RAID 10 adds fault tolerance to RAID 0 through the RAID 1 mirroring of each disk in the RAID 0 striped set. Its inverse, known as RAID 0+1, mirrors a complete striped set to another striped set just like it. Both of these implementations require a minimum of four drives and, because of the RAID 1 component, use half of your purchased storage space for mirroring. 

Figure 1.61 illustrates RAID 1 and RAID 5.

- **Figure 1.61** RAID 1 and RAID 5
![[Image 1.61.png]]

There are other implementations of RAID that are not included in the CompTIA A+ exam objectives. Examples include RAID 3 and RAID 4, which place all parity on a single drive, resulting in varying performance changes upon drive loss. RAID 6 is essentially RAID 5 with the ability to lose two disks and still function. RAID 6 uses the equivalent of two parity disks as it stripes its data and distributed parity blocks across all disks in a fashion similar to that of RAID 5. A minimum of four disks is required to make a RAID 6 array.

## Removable Storage and Media

Thus far we’ve focused on storage media that is internal to a PC, but external and removable storage options exist as well. Among the other types of storage available are flash drives, memory cards, optical drives, and external hard drives. The following sections present the details about removable storage solutions.

### Flash Memory

Once used exclusively for primary memory, the same components found on your motherboard as RAM are now utilized in various physical sizes and configurations in today’s solid-state storage solutions. These include older removable and non-removable flash memory mechanisms, Secure Digital (SD) and other memory cards, and USB flash drives. Each of these technologies offers the ability to reliably store vast amounts of information in a compact form factor. Manufacturers have introduced innovative packaging options for these products, such as keychain attachments, to enhance portability.

Additionally, consider the SSD alternatives to traditional magnetic hard drives mentioned earlier in this chapter. Flash memory modules have long provided storage options ranging from low to medium capacities for various devices. The term "flash memory" originates from its ability to quickly modify stored data using electricity. Original flash memory is still widely used in devices requiring nonvolatile storage for critical data and code, such as routers and switches.

For instance, Cisco Systems employs flash memory in various forms to store its Internetwork Operating System (IOS). During boot-up and operational uptime, IOS is accessed directly from flash memory, and in some cases, throughout administrator configuration sessions. In lower-end models, IOS is stored in compressed form within the flash memory device and then decompressed into RAM for use during configuration and operation. After boot-up, flash memory is typically only accessed again if its contents need modification, such as during an IOS upgrade. Certain devices utilize externally removable PC Card technology for similar purposes.

The following sections will delve into today’s most popular forms of flash memory: USB flash drives and memory cards.

#### USB Flash Drives

USB flash drives are incredibly versatile and convenient devices that allow you to store large quantities of information in a very compact form factor. Many of these devices are designed as mere extensions of the host’s USB connector, protruding minimally from the interface and adding little to its width. This design makes USB flash drives easy to transport, whether in a pocket or a laptop bag. Figure 1.63 illustrates an example of such a component and its relative size.

- **Figure 1.62** A USB flash drive
![[Image 1.62.png]]

USB flash drives capitalize on the versatility of the USB interface, taking advantage of Windows’ Plug and Play, AutoPlay, and Safely Remove Hardware features and the physical connector strength. Upon insertion, these devices announce themselves to Windows File Explorer as removable drives, and they show up in the Explorer window with a drive letter. This software interface allows for drag- and- drop copying and most of the other Explorer functions performed on standard drives. Note that you might have to use the Disk Management utility to assign a drive letter manually to a USB flash drive if it fails to acquire one itself. This can happen in certain cases, such as when the previous letter assigned to the drive has been taken by another device in the USB flash drive’s absence.

#### SD and Other Memory Cards

Today’s smaller devices require some form of removable solid-state memory that can be used for temporary and permanent storage of digital information. Modern electronics, as well as most contemporary digital still cameras, use some form of removable memory card to store still images permanently or until they can be copied off or printed out. Of these, the Secure Digital (SD) format has emerged as the preeminent leader of the pack, which includes the older MultiMediaCard (MMC) format on which SD is based. Both of these cards measure 32 mm × 24 mm, and slots that receive them are often marked for both. The SD card is slightly thicker than the MMC and has a write- protect notch (and often a switch to open and close the notch), unlike MMC. Even smaller devices, such as mobile phones, have an SD solution for them. One of these products, known as miniSD, is slightly thinner than SD and measures 21.5 mm × 20 mm. The other, microSD, is thinner yet and only 15 mm × 11 mm. Both of these reduced formats have adapters that allow them to be used in standard SD slots. Figure 1.64 shows an SD card and a microSD card next to a ruler based on inches.

- **Figure 1.63** Typical SD cards
![[Image 1.63.png]]

Table 2.3 lists additional memory card formats, the slots for some of which can be seen in the images that follow the table.

![[Table 1.00]]

Figure 1.64 shows the memory-card slots of an HP PhotoSmart printer, which is capable of reading these devices and printing from them directly or creating a drive letter for access to the contents over its USB connection to the computer. Clockwise from the upper left, these slots accommodate CF/Microdrive, SmartMedia, Memory Stick (bottom right), and MMC/ SD. The industry provides almost any adapter or converter to allow the various formats to work together.

- **Figure 1.64** Card slots in a printer
![[Image 1.64.png]]

Nearly all of today’s laptops have built-in memory card slots and many desktops will have readers built into the front or top panel of the case as well. If a computer doesn’t have memory card slots built into the case, it’s easy to add external card readers. Most are connected via USB, such as the one shown in Figure 1.65 (front first, then back), and are widely available in many different configurations.

- **Figure 1.65** A USB-attached card reader
![[Image 1.65.png]]

### Hot- Swappable Devices

Many of the removable storage devices mentioned are hot-swappable. This means that you can insert and remove the device with the system powered on. Most USB attached devices without a filesystem fall into this category. Non-hot-swappable devices, in contrast, either cannot have the system’s power applied when they are inserted or removed or have some sort of additional conditions for their insertion or removal. One subset is occasionally referred to as cold-swappable, the other as warm-swappable. The system power must be off before you can insert or remove cold-swappable devices. An example of a cold-swappable device is anything connected to a SATA connector on the motherboard.

Warm-swappable devices include USB flash drives and external drives that have a filesystem. Windows and other operating systems tend to leave files open while accessing them and write cached changes to them at a later time, based on the algorithm in use by the software. Removing such a device without using the Safely Remove Hardware and Eject Media utility can result in data loss. However, after stopping the device with the utility, you can remove it without powering down the system—hence, the warm component of the category’s name. These are officially hot-swappable devices.

Hardware-based RAID systems benefit from devices and bays with a single connector that contains both power and data connections instead of two separate connectors. This is known as Single Connector Attachment (SCA). SCA interfaces have ground leads that are longer than the power leads so that they make contact first and lose contact last. SATA power connectors are designed in a similar fashion for the same purpose. This arrangement ensures that no power leads make contact without their singular ground leads, which would often result in damage to the drive. Drives based on SCA are hot-swappable. RAID systems that have to be taken offline before drives are changed out, but the system power can remain on, are examples of warm-swappable systems.

### Optical Drives

The final category of storage devices we will look at is optical drives. They get their name because instead of storing data using magnetic fields like conventional HDDs, they read and write data with the use of a laser. The laser scans the surface of a spinning plastic disc, with data encoded as small bits and bumps in the track of the disc.

With the popularity of high-speed Internet access and streaming services, optical drives have lost much of their popularity. For about 20 years they were practically required components, but today they are far less common. The most advanced optical storage technology used is the Blu-ray Disc (BD) drive. It replaced the digital versatile disc (DVD), also called digital video disc drive, which in turn replaced the compact disc (CD) drive. Each type of optical drive can also be expected to support the technology that came before it. Such optical storage devices began earnestly replacing floppy diskette drives in the late 1990s. Although, like HDDs, these discs have greater data capacity and increased performance over floppies, they are not intended to replace hard disk drives. HDDs greatly exceed the capacity and read/write performance of optical drives.

The CDs, DVDs, and BDs used for data storage, which may require multiple data reads and writes, are virtually the same as those used for permanent recorded audio and video. The way that data, audio, and video information is written to consumer-recordable versions makes them virtually indistinguishable from such professionally manufactured discs. Any differences that arise are due to the format used to encode the digital information on the disc. Despite the differences among the professional and consumer formats, newer players have no issue with any type of disc used. Figure 1.66 shows an example of an internal 5¼" DVD-ROM drive, which also accepts CD-ROM discs. Modern optical drives are indistinguishable from older ones, aside from obvious markings concerning their capabilities. External drives that connect via USB are more popular (and portable!) than their internal cousins.

- **Figure 1.66** A DVD-ROM drive
![[Image 1.66.png]] 
 
#### Optical Disc Capacities

The amount of data that can be stored on the three primary formats of optical disc varies greatly, with each generation of disc exceeding the capacity of all previous generations. We’ll start with the oldest first to show the progression of technologies.

When CDs first were used with computers, they were a huge change from floppy disks. Instead of installing the program of the day using 100 floppy disks, you could use a single CD-ROM, which can hold approximately 650 MB in its original, least-capable format. Although CDs capable of storing 700 MB eventually became and continue to be the most common, discs with 800 MB and 900 MB capacities have been standardized as well.

CDs were rather limited in technology, though. For example, data could only be written to one side, and only one layer of data was permitted on that side. DVDs came along with much higher base capacity, but also the ability to store on both sides and have two layers of data on each side.

The basic DVD disc is still a single-sided disc that has a single layer of encoded information. These discs have a capacity of 4.7 GB, over five times the highest CD capacity. Simple multiplication can sometimes be used to arrive at the capacities of other DVD varieties. For example, when another media surface is added on the side of the disc where the label is often applied, a double-sided disc is created. Such double-sided discs (DVD DS, for double-sided) have a capacity of 9.4 GB, exactly twice that of a single-sided disc.

Practically speaking, the expected 9.4 GB capacity from two independent layers isn’t realized when those layers are placed on the same side of a DVD, resulting in only 8.5 GB of usable space. This technology is known as DVD DL (DL for dual-layer), attained by placing two media surfaces on the same side of the disc, one on top of the other, and using a more sophisticated mechanism for reading and writing. The loss of capacity is due to the space between tracks on both layers being 10 percent wider than normal to facilitate burning one layer without affecting the other. This results in about 90 percent remaining capacity per layer. Add the DL technology to a double-sided disc, and you have a disc capable of holding 17.1 GB of information—again, twice the capacity of the single-sided version.

The current generation of optical storage technology, Blu-ray, was designed for modern high-definition video sources. The equipment used to read the resulting discs employs a violet laser, in contrast to the red laser used with standard DVD and CD technologies. Taking a bit of creative license with the color of the laser, the Blu-ray Disc Association named itself and the technology Blu-ray Disc (BD), after this visibly different characteristic. Blu-ray technology further increases the storage capacity of optical media without changing the form factor. On a 12 cm disc, similar to those used for CDs and DVDs, BD derives a 25 GB storage capacity from the basic disc. When you add a second layer to the same or opposite side of the disc, you attain 50 GB of storage. The Blu-ray laser is of a shorter wavelength (405nm) than that of DVD (650nm) and CD (780nm) technologies. As a result, and through the use of refined optics, the laser can be focused on a much smaller area of the disc. This leads to a higher density of information being stored in the same area.

#### Optical Drive Data Rates

Optical drives are rated in terms of their data transfer speed. The first CD-ROM drives transferred data at the same speed as home audio CD players, 150 KBps, referred to as 1X. Soon after, CD drives rated as 2X drives that would transfer data at 300 KBps appeared. They increased the spin speed in order to increase the data transfer rate. This system of ratings continued up until the 8X speed was reached. At that point, the CDs were spinning so fast that there was a danger of them flying apart inside the drive. So, although future CD drives used the same rating (as in 16X, 32X, and so on), their rating was expressed in terms of theoretical maximum transfer rate; 52X is widely regarded as the highest multiplier for data CDs. Therefore, the drive isn’t necessarily spinning faster, but through electronics and buffering advances, the transfer rates continued to increase.

The standard DVD-ROM 1X transfer rate is 1.4 MBps, already nine times that of the comparably labeled CD-ROM. As a result, to surpass the transfer rate of a 52X CD-ROM drive, a DVD-ROM drive need only be rated 6X. DVD transfer rates of 24X at the upper end of the scale are common.

The 1X transfer rate for Blu-ray is 4.5 MBps, roughly 3¼ times that of the comparable DVD multiplier and close to 30 times that of the 1X CD transfer rate. It takes 2X speeds to play commercial Blu-ray videos properly, and 16X drives are common today.

#### Recordable Discs and Burners

Years after the original factory-made CD-ROM discs and the drives that could read them were developed, the industry, strongly persuaded by consumer demand, developed discs that, through the use of associated drives, could be written to once and then used in the same fashion as the original CD-ROM discs. The firmware with which the drives were equipped could vary the power of the laser to achieve the desired result. At standard power, the laser allowed discs inserted in these drives to be read. Increasing the power of the laser allowed the crystalline media surface to be melted and changed in such a way that light would reflect or refract from the surface in microscopic increments. This characteristic enabled mimicking the way in which the original CD-ROM discs stored data.

Eventually, discs that could be written to, erased, and rewritten were developed. Drives that contained the firmware to recognize these discs and control the laser varied the laser’s power in three levels. The original two levels closely matched those of the writable discs and drives. The third level, somewhere in between, could neutralize the crystalline material without writing new information to the disc. This medium level of power left the disc surface in a state similar to its original, unwritten state. Subsequent high-power laser usage could write new information to the neutralized locations. Drives capable of writing to optical discs are known as burners, because they essentially burn a new image into the disc.

Two different types of writable CD are available. The first type is one that is recordable (-R), and the second is rewritable (-RW). For the first (CD-R), data is written once and then the disc is finalized. With rewritable CDs (CD-RW), data can be rewritten multiple times. Note that over time and with several rewrites, these types of discs can become unstable.

Burnable DVDs use similar nomenclature to CDs, with a notable twist. In addition to DVD-R and DVD-RW, there are “plus” standards of DVD+R and DVD+RW. This is thanks to there being two competing DVD consortiums, each with their own preferred format. The “plus” standards come from the DVD+RW Alliance, whereas the “dash” counterparts are specifications of the DVD Forum. The number of sectors per disc varies between the “plus” and “dash” variants, so older drives might not support both types. The firmware in today’s drives knows to check for all possible variations in encoding and capability. You shouldn’t run into problems today, but it is possible.

Finally, the Blu-ray Disc Association duplicated the use of the -R suffix to denote a disc capable of being recorded only once by the consumer. Instead of the familiar -RW, however, the association settled on -RE, short for re-recordable. As a result, watch for discs labeled BD-R and BD-RE. Dual-layer versions of these discs can be found as well. Table 2.4 draws together the most popular optical-disc formats and lists their respective capacities. Figures in bold in the table are the most common industry-quoted capacities.

![[Table 1.08]]

## Installing, Removing, and Configuring Storage Devices

The removal and installation of storage devices, such as hard drives and optical drives, is pretty straightforward. There really isn’t any deviation in the process of installing or exchanging the hardware. Fortunately, with today’s operating systems, little to no configuration is required for such devices. The Plug and Play BIOS and operating system work together to recognize the devices. However, you still have to partition and format out- of-the-box hard drives before they will allow the installation of the operating system. Nevertheless, today’s operating systems allow for a pain-free partition/format/setup experience by handling the entire process, if you let them.

### Removing Storage Devices

Removing any component is frequently easier than installing the same part. Consider the fact that most people could destroy a house, perhaps not safely enough to ensure their wellbeing, but they don’t have to know the intricacies of construction to start smashing away. On the other hand, very few people are capable of building a house. Similarly, many could figure out how to remove a storage device, as long as they can get into the case to begin with, but only a few could start from scratch and successfully install one without tutelage.

> [!info] Removing an Internal Storage Device
> 1. With the power source removed from the system, ground yourself and the computer to the same source of ground.
> 2. Remove the cover from the system, exposing the internal components.
> 3. Unplug all connections from the storage device you wish to remove. These include data and power connections as well as any others, such as audio connections to the sound card or motherboard (for an optical drive). Always be sure to grip the connector, not the wires.
> 4. Gather the appropriate antistatic packaging for all static-sensitive components that will be reused in the future, including any adapter cards that the storage device plugs into.
> 5. Remove any obstructions that might hinder device removal, such as component cables attached to adapter cards or the adapter cards themselves, storing them in antistatic packaging so that they can be reused. 
> 6. Remove related adapter cards from the motherboard, storing them in antistatic packaging so that they can be reused. 
> 7. Remove the machine screws holding the storage device to the chassis. These could be on the side of the device or on the bottom.
> 8. Some devices, especially hard drives because they have no front access from the case, pull out of the chassis toward the rear of the case, whereas others, such as optical drives, generally pull out from the front. A gentle nudge from the rear of the device starts it on its way out the front. Go ahead and remove the device from the case. If you discover other components that obstruct the storage device’s removal, repeat step 5.

### Installing Storage Devices

An obvious difference among storage devices is their form factor. This is the term used to describe the physical dimensions of a storage device. Form factors commonly have the following characteristics:

- 3¼" wide vs. 5¼" wide
- Half height vs. full height vs. 1" high and more
- Any of the laptop specialty form factors

You will need to determine whether you have an open bay in the chassis to accommodate the form factor of the storage device that you want to install. Adapters exist that allow a device of small size to fit into a larger bay. For obvious reasons, the converse is not also true. 

> [!info] Installing an Internal Storage Device
> 1. With the power source removed from the system, ground yourself and the computer to the same source of ground.
> 2. Remove the cover from the system, exposing the internal components.
> 3. Locate an available bay for your component, paying attention to your device’s need for front access. If you do not see one, look around; some cases provide fastening points near the power supply or other open areas of the case. If you still do not see one, investigate the possibility of sacrificing a rarely or never used device to make room.
> 4. Remove any obstructions that might hinder device installation, such as component cables attached to adapter cards or the adapter cards themselves, storing them in anti-static packaging to be reused.
> 5. Find the proper screws for the storage device, and set any jumpers on the drive while it is in hand. Then insert the device into the bay. Keep in mind that some insert from the rear of the bay and some from the front.
> 6. Line up the screw holes in the device with the holes in the bay. Note that many devices rarely insert as far as they can before lining up with the chassis’ holes, so don’t be surprised when pushing the device all the way into the bay results in misalignment. Other devices that require front access stop themselves flush with the front of the case, and still others require you to secure them while holding them flush.
> 7. Use at least two screws on one side of the device. This keeps the device from sliding in the bay as well as from rotating, which happens when you use only one screw or one screw on each side. If the opposite side is accessible, go ahead and put at least one screw in the other side. Most devices allow for as many as four screws per side, but eight screws are not necessary in the vast majority of situations.
> 8. Connect the data cable from the device to the adapter card or motherboard header.
> 9. Attach a power connector from the power supply to the device. Be sure to insert the connector completely.
> 10. Once the drive is attached, unground yourself, and turn the computer on to verify that the drive is functional. 
> 11. If the drive is working properly, replace the computer cover.

> [!info] Note
> There’s quite a lot to know about storage devices, and there are several objectives to keep in mind as you prepare for the A+ exam. You will need to know the following:
> - Hard drive speeds
> 	- 5,400 rpm, 7,200 rpm, 10,000 rpm, and 15,000 rpm
> - Hard drive form factors
> 	- 2.5 and 3.5
> - SSD communication interfaces
> 	- NVMe, SATA, and PCIe
> - SSD form factors
> 	- M.2 and mSATA
> - Drive configurations such as RAID 0, RAID 1, RAID 5, and RAID 10
> - Removable storage
> 	- Flash drives
> 	- Memory cards
> 	- Optical drives
