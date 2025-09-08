
# Memory (RAM)

[[🏷️PC hardware]]

"More memory, more memory, I don’t have enough memory!" Adding memory is one of the most popular, easy, and inexpensive ways to upgrade a computer. As the computer’s CPU works, it stores data and instructions in the computer’s memory. Contrary to what you might expect from an inexpensive solution, memory upgrades tend to afford the greatest performance increase as well, up to a point. Motherboards have memory limits; operating systems have memory limits; CPUs have memory limits.

To identify memory visually within a computer, look for several thin rows of small circuit boards sitting vertically, potentially packed tightly together near the processor. In situations where only one memory stick is installed, it will be that stick and a few empty slots that are tightly packed together. Figure 1.30 shows where memory is located in a system—in this case, all four banks are full.

- **Figure 1.30** Location of memory within a system
![[Image 1.30.png]]

## Important Memory Terms 

There are a few technical terms and phrases that you need to understand with regard to memory and its function:

- Parity checking
- Error-correction code (ECC)
- Single- and double-sided memory
- Single-, dual-, triple-, and quad-channel memory

> [!info] Note
> ECC, or error correcting code, will sometimes be referred to by its full name as error correcting code as well. As with other acronyms in computing that might have multiple expansions, focus less on what it stands for and more on what it does.

### Parity Checking and Memory Banks

Parity checking is a rudimentary error checking scheme that offers no error correction. Parity checking works most often on a byte, or 8 bits, of data. A ninth bit is added at the transmitting end and removed at the receiving end so that it does not affect the actual data transmitted. If the receiving end does not agree with the parity that is set in a particular byte, a parity error results. The four most common parity schemes affecting this extra bit are known as even, odd, mark, and space. Even and odd parity are used in systems that actually compute parity. Mark (a term for a digital pulse, or 1 bit) and space (a term for the lack of a pulse, or a 0 bit) parity are used in systems that do not compute parity but expect to see a fixed bit value stored in the parity location. Systems that do not support or reserve the location required for the parity bit are said to implement non-parity memory.

The most basic model for implementing memory in a computer system uses eight memory chips to form a set. Each memory chip holds millions or billions of bits of information, each in its own cell. For every byte in memory, one bit is stored in each of the eight chips. A ninth chip is added to the set to support the parity bit in systems that require it. One or more of these sets, implemented as individual chips or as chips mounted on a memory module, form a memory bank. 

A bank of memory is required for the computer system to recognize electrically that the minimum number of memory components or the proper number of additional memory components has been installed. The width of the system data bus, the external bus of the processor, dictates how many memory chips or modules are required to satisfy a bank. For example, one 32-bit, 72-pin SIMM (single in-line memory module) satisfies a bank for an old 32-bit CPU, such as a i386 or i486 processor. Two such modules are required to satisfy a bank for a 64-bit processor— a Pentium, for instance. However, only a single 64-bit, 168-pin DIMM is required to satisfy the same Pentium processor. For those modules that have fewer than eight or nine chips mounted on them, more than 1 bit for every byte is being handled by some of the chips. For example, if you see three chips mounted, the two larger chips customarily handle 4 bits, a nibble, from each byte stored, and the third, smaller chip handles the single parity bit for each byte.

Even and odd parity schemes operate on each byte in the set of memory chips. In each case, the number of bits set to a value of 1 is counted up. If there is an even number of 1 bits in the byte (0, 2, 4, 6, or 8), even parity stores a 0 in the ninth bit, the parity bit; otherwise, it stores a 1 to even up the count. Odd parity does just the opposite, storing a 1 in the parity bit to make an even number of 1s odd and a 0 to keep an odd number of 1s odd. You can see that this is effective only for determining if there was a blatant error in the set of bits received, but there is no indication as to where the error is and how to fix it. Furthermore, the total 1-bit count is not important, only whether it’s even or odd. Therefore, in either the even or odd scheme, if an even number of bits is altered in the same byte during transmission, the error goes undetected because flipping 2, 4, 6, or all 8 bits results in an even number of 1s remaining even and an odd number of 1s remaining odd.

Mark and space parity are used in systems that want to see 9 bits for every byte transmitted but don’t compute the parity bit’s value based on the bits in the byte. Mark parity always uses a 1 in the parity bit, and space parity always uses a 0. These schemes offer less error detection capability than the even and odd schemes because only changes in the parity bit can be detected. Again, parity checking is not error correction; it’s error detection only, and not the best form of error detection at that. Nevertheless, an error can lock up the entire system and display a memory parity error. Enough of these errors and you need to replace the memory. Therefore, parity checking remains from the early days of computing as an effective indicator of large-scale memory and data-transmission failure, such as with serial interfaces attached to analog modems or networking console interfaces, but not so much for detecting random errors.

In the early days of personal computing, almost all memory was parity-based. As quality has increased over the years, parity checking in the RAM subsystem has become more uncommon. As noted earlier, if parity checking is not supported, there will generally be fewer chips per module, usually one less per column of RAM.

### Error Checking and Correction

The next step in the evolution of memory error detection is known as error-correction code (ECC). If memory supports ECC, check bits are generated and stored with the data. An algorithm is performed on the data and its check bits whenever the memory is accessed. If the result of the algorithm is all zeros, then the data is deemed valid and processing continues. ECC can detect single- and double-bit errors and actually correct single-bit errors. In other words, if a particular byte—group of 8 bits—contains errors in 2 of the 8 bits, ECC can recognize the error. If only 1 of the 8 bits is in error, ECC can correct the error.

### Single- and Double-Sided Memory

Commonly speaking, the terms single-sided memory and double-sided memory refer to how some memory modules have chips on one side and others have chips on both sides. Double-sided memory is essentially treated by the system as two separate memory modules. Motherboards that support such memory have memory controllers that must switch between the two "sides" of the modules and, at any particular moment, can access only the side to which they have switched. Double-sided memory allows more memory to be inserted into a computer, using half the physical space of single-sided memory, which requires no switching by the memory controller.

### Single-, Dual-, Triple-, and Quad-Channel Memory

Standard memory controllers manage access to memory in chunks of the same size as the system bus’s data width. This is considered communicating over a single channel. Most modern processors have a 64-bit system data bus. This means that a standard memory controller can transfer exactly 64 bits of information at a time. Communicating over a single channel is a bottleneck in an environment where the CPU and memory can both operate
faster than the conduit between them. Up to a point, every channel added in parallel between the CPU and RAM serves to ease this constriction.

Memory controllers that support dual- channel and greater memory implementation were developed in an effort to alleviate the bottleneck between the CPU and RAM. Dual-channel memory is the memory controller’s coordination of two memory banks to work as a synchronized set during communication with the CPU, doubling the specified system bus width from the memory’s perspective. Triple-channel memory, then, demands the coordination of three memory modules at a time. Quad-channel memory is the coordination of four memory modules at once. Collectively, they are known as multichannel memory implementations.

Because today’s processors largely have 64-bit external data buses, and because one stick of memory satisfies this bus width, there is a 1:1 ratio between banks and modules. This means that implementing multichannel memory in today’s most popular computer systems requires that two, three, or four memory modules be installed at a time. Note, however, that it’s the motherboard, not the memory, that implements multichannel memory (more on this in a moment). Single-channel memory, in contrast, is the classic memory model that dictates only that a complete bank be satisfied whenever memory is initially installed or added. One bank supplies only half the width of the effective bus created by dual- channel support, for instance, which by definition pairs two banks at a time.

In almost all cases, multichannel implementations support single-channel installation, but poorer performance should be expected. Multichannel motherboards often include slots of different colors, usually one of each color per set of slots. To use only a single channel, you populate slots of the same color, skipping neighboring slots to do so. Filling neighboring slots in a dual-channel motherboard takes advantage of its dual-channel capability.

Because of the special tricks that are played with memory subsystems to improve overall system performance, care must be taken during the installation of disparate memory modules. In the worst case, the computer will cease to function when modules of different speeds, different capacities, or different numbers of sides are placed together in slots of the same channel. If all of these parameters are identical, there should be no problem with pairing modules. Nevertheless, problems could still occur when modules from two different manufacturers or certain unsupported manufacturers are installed, all other parameters being the same. Technical support or documentation from the manufacturer of your motherboard should be able to help with such issues.

Although it’s not the make- up of the memory that leads to multichannel support but instead the technology on which the motherboard is based, some memory manufacturers still package and sell pairs and triplets of memory modules in an effort to give you peace of mind when you’re buying memory for a system that implements multichannel memory architecture. Keep in mind, the motherboard memory slots have the distinctive color- coding, not the memory modules.

> [!info] I Can't Fill All My Memory Slots
> As a reminder, most motherboard manufacturers document the quantity and types of modules that their equipment supports. Consult your documentation when you have questions about supported memory. Most manufacturers require that slower memory be inserted in lower-numbered memory slots. This is because such a system adapts to the first module it sees, looking at the lower-numbered slots first. Counterintuitively, however, it might be required that you install modules of larger capacity rather than smaller modules in lower-numbered slots.
> 
> >
> 
> Additionally, memory technology continues to advance after each generation of motherboard chipsets is announced. Don’t be surprised when you attempt to install a single module of the highest available capacity in your motherboard and the system doesn’t recognize the module, either by itself or with others. That capacity of module might not have been in existence when the motherboard’s chipset was released. Sometimes, flashing the BIOS is all that is required. Other times it just won’t work. Consult the motherboard’s documentation.
> 
> >
> 
> One common point of confusion, not related to capacity, when memory is installed is the lack of recognition of four modules when two or three modules work fine, for example. In such a case, let’s say your motherboard’s memory controller supports a total of four modules. Recall that a double-sided module acts like two separate modules. If you are using double-sided memory, your motherboard might limit you to two such modules comprising four sides (essentially four virtual modules), even though you have four slots on the board. If instead you start with three single-sided modules, when you attempt to install a double-sided module in the fourth slot, you are essentially asking the motherboard to accept five modules, which it cannot.
> 
> > 
> 
> Finally, know that dual- and quad- channel memory support is common today, but triple-channel is less so. As with anything else, check the motherboard’s documentation to see what it supports.

## Types of Memory

Memory comes in many formats. Each one has a particular set of features and characteristics, making it best suited for a particular application. Some decisions about the application of the memory type are based on suitability; others are based on affordability to consumers or marketability to computer manufacturers. The following list gives you an idea of the vast array of memory types and subtypes:

- DRAM (dynamic random access memory)
	- ADRAM (asynchronous DRAM)
	- FPM DRAM (fast page mode DRAM)
	- EDO DRAM (extended data out DRAM)
	- BEDO DRAM (burst EDO DRAM)
	- SDRAM (synchronous DRAM)
	- SDR SDRAM (single data rate SDRAM)
	- DDR SDRAM (double data rate SDRAM)
	- DDR2 SDRAM (double data rate, version two, SDRAM)
	- DDR3 SDRAM (double data rate, version three, SDRAM)
	- DDR4 SDRAM (double data rate, version four, SDRAM)
	- DDR5 SDRAM (double data rate, version five, SDRAM)
- SRAM (static random access memory)
- ROM (read- only memory)

Pay particular attention to all synchronous DRAM types as that’s the most common type in use. Note that the type of memory does not dictate the packaging of the memory. Conversely, however, you might notice one particular memory packaging holding the same type of memory every time you come across it. Nevertheless, there is no requirement to this end. Let’s detail the intricacies of some of these memory types.

### DRAM

DRAM is dynamic random access memory. This is what most people are talking about when they mention RAM. When you expand the memory in a computer, you are adding DRAM chips. You use DRAM to expand the memory in the computer because it’s a cheaper type of memory. Dynamic RAM chips are cheaper to manufacture than most other types because
they are less complex. Dynamic refers to the memory chips’ need for a constant update signal (also called a refresh signal) in order to keep the information that is written there. If this signal is not received every so often, the information will bleed off and cease to exist. Currently, the most popular implementations of DRAM are based on synchronous DRAM and include DDR3 and DDR4. Occasionally you will see some DDR2, and DDR5 is new so
it hasn’t been widely adopted yet. Before discussing these technologies, let’s take a quick look at the legacy asynchronous memory types.

#### Asynchronous DRAM

Asynchronous DRAM (ADRAM) is characterized by its independence from the CPU's external clock. Asynchronous DRAM chips have codes on them that end in a numerical value that is related to (often 1/10 of the actual value of) the access time of the memory. Access time is essentially the difference between the time when the information is requested from memory and the time when the data is returned. Common access times attributed to
asynchronous DRAM were in the 40- to 120-nanosecond (ns) vicinity. A lower access time is obviously better for overall performance.

Because ADRAM is not synchronized to the front-side bus, you would often have to insert wait states through the BIOS setup for a faster CPU to be able to use the same memory as a slower CPU. These wait states represented intervals in which the CPU had to mark time and do nothing while waiting for the memory subsystem to become ready again for subsequent access.

Common asynchronous DRAM technologies included fast page mode (FPM), extended data out (EDO), and burst EDO (BEDO). Feel free to investigate the details of these particular technologies, but a thorough discussion of these memory types is not necessary here. The A+ technician should be concerned with synchronous forms of RAM, which are the only types of memory being installed in mainstream computer systems today.

#### Synchronous DRAM 

Synchronous DRAM (SDRAM) shares a common clock signal with the computer’s system-bus clock, which provides the common signal that all local-bus components use for each step that they perform. This characteristic ties SDRAM to the speed of the FSB and hence the processor, eliminating the need to configure the CPU to wait for the memory to catch up.

Originally, SDRAM was the term used to refer to the only form of synchronous DRAM on the market. As the technology progressed, and more was being done with each clock signal on the FSB, various forms of SDRAM were developed. What was once called simply SDRAM needed a new name retroactively. Today, we use the term single data rate SDRAM (SDR SDRAM) to refer to this original type of SDRAM.

**SDR SDRAM:** SDR SDRAM is a legacy RAM technology, and it is presented here only to provide a basis for the upcoming discussion of DDR and other more advanced RAM. With SDR SDRAM, every time the system clock ticks, 1 bit of data can be transmitted per data pin, limiting the bit rate per pin of SDRAM to the corresponding numerical value of the clock’s frequency. With today’s processors interfacing with memory using a parallel data- bus width of 8 bytes (hence the term 64- bit processor), a 100 MHz clock signal produces 800 MBps. That’s mega bytes per second, not mega bits. Such memory modules are referred to as PC100, named for the true FSB clock rate upon which they rely. PC100 was preceded by PC66 and succeeded by PC133, which used a 133 MHz clock to produce 1,066 MBps of throughput.

Note that throughput in megabytes per second is easily computed as eight times the rating in the name. This trick works for the more advanced forms of SDRAM as well. The common thread is the 8-byte system data bus. Incidentally, you can double throughput results when implementing dual-channel memory.

**DDR SDRAM:** Double data rate (DDR) SDRAM earns its name by doubling the transfer rate of ordinary SDRAM; it does so by double-pumping the data, which means transferring a bit per pin on both the rising and falling edges of the clock signal. This obtains twice the transfer rate at the same FSB clock frequency. It’s the increasing clock frequency that generates heating issues with newer components, so keeping the clock the same is an advantage. The same 100 MHz clock gives a DDR SDRAM system the impression of a 200 MHz clock compared to an SDR SDRAM system. For marketing purposes, and to aid in the comparison of disparate products (DDR vs. SDR, for example), the industry has settled on the practice of using this effective clock rate as the speed of the FSB.

> [!info] Module Throughput Related to FSB Speed
> There is always an 8:1 module-to-chip (or module-to-FSB speed) numbering ratio because of the 8 bytes that are transferred at a time with 64-bit processors (not because of the ratio of 8 bits per byte). The formula in Figure 1.31 explains how this relationship works.
> - **Figure 1.31** The 64-bit memory throughput formula
![[Image 1.31.png]]

Because the actual system clock speed is rarely mentioned in marketing literature, on packaging, or on store shelves for DDR and higher, you can use this advertised FSB frequency in your computations for DDR throughput. For example, with a 100 MHz clock and two operations per cycle, motherboard makers will market their boards as having an FSB of 200 MHz. Multiplying this effective rate by 8 bytes transferred per cycle, the data rate is 1,600 MBps. Because DDR made throughput a bit trickier to compute, the industry began using this final throughput figure to name the memory modules instead of the actual frequency, which was used when naming SDR modules. This makes the result seem many times better (and much more marketable), while it’s really only twice (or so) as good, or close to it. 

In this example, the module is referred to as PC1600, based on a throughput of 1,600 MBps. The chips that go into making PC1600 modules are named DDR200 for the effective FSB frequency of 200 MHz. Stated differently, the industry uses DDR200 memory chips to manufacture PC1600 memory modules.

Let’s make sure that you grasp the relationship between the speed of the FSB and the name for the related chips as well as the relationship between the name of the chips (or the speed of the FSB) and the name of the modules. Consider an FSB of 400 MHz, meaning an actual clock signal of 200 MHz, by the way—the FSB is double the actual clock for DDR, remember. It should be clear that this motherboard requires modules populated with DDR400 chips and that you’ll find such modules marketed and sold as PC3200. 

Let’s try another. What do you need for a motherboard that features a 333 MHz FSB (actual clock is 166 MHz)? Well, just using the 8:1 rule mentioned earlier, you might be on the lookout for a PC2667 module. Note, however, that sometimes the numbers have to be played with a bit to come up with the industry’s marketing terms. You’ll have an easier time finding PC2700 modules that are designed specifically for a motherboard like yours, with an FSB of 333 MHz. The label isn’t always technically accurate, but round numbers sell better, perhaps. The important concept here is that if you find PC2700 modules and PC2667 modules, there’s absolutely no difference; they both have a 2667 MBps throughput rate. Go for the best deal; just make sure that the memory manufacturer is reputable.

**DDR2 SDRAM:** Think of the 2 in DDR2 as yet another multiplier of 2 in the SDRAM technology, using a lower peak voltage to keep power consumption down (1.8V vs. the 2.5V of DDR). Still double-pumping, DDR2, like DDR, uses both sweeps of the clock signal for data transfer. Internally, DDR2 further splits each clock pulse in two, doubling the number of operations it can perform per FSB clock cycle. Through enhancements in the electrical interface and buffers, as well as through adding off-chip drivers, DDR2 nominally produces four times the throughput that SDR is capable of producing. 

Continuing the DDR example, DDR2, using a 100 MHz actual clock, transfers data in four operations per cycle (effective 400 MHz FSB) and still 8 bytes per operation, for a total of 3,200 MBps. Just as with DDR, chips for DDR2 are named based on the perceived frequency. In this case, you would be using DDR2-400 chips. DDR2 carries on the effective FSB frequency method for naming modules but cannot simply call them PC3200 modules because those already exist in the DDR world. DDR2 calls these modules PC2-3200. (Note the dash to keep the numeric components separate.)

As another example, it should make sense that PC2-5300 modules are populated with DDR2-667 chips. Recall that you might have to play with the numbers a bit. If you multiply the well-known FSB speed of 667 MHz by 8 to figure out what modules you need, you might go searching for PC2- 5333 modules. You might find someone advertising such modules, but most compatible modules will be labeled PC2-5300 for the same marketability mentioned earlier. They both support 5,333 MBps of throughput.

**DDR3 SDRAM:** The next generation of memory devices was designed to roughly double the performance of DDR2 products. Based on the functionality and characteristics of DDR2’s proposed successor, most informed consumers and some members of the industry surely assumed the forthcoming name would be DDR4. This was not to be, however, and DDR3 was born. This naming convention proved that the 2 in DDR2 was not meant to be a multiplier but instead a revision mark of sorts. Well, if DDR2 was the second version of DDR, then DDR3 is the third. DDR3 is a memory type, designed to be twice as fast as the DDR2 memory, that operates with the same system clock speed. Just as DDR2 was required to lower power consumption to make up for higher frequencies, DDR3 must do the same. In fact, the peak voltage for DDR3 is only 1.5V.

The most commonly found range of actual clock speeds for DDR3 tends to be from 133 MHz at the low end to less than 300 MHz. Because double-pumping continues with DDR3, and because four operations occur at each wave crest (eight operations per cycle), this frequency range translates to common FSB implementations from 1,066 MHz to more than 2,000 MHz in DDR3 systems. These memory devices are named following the conventions established earlier. Therefore, if you buy a motherboard with a 1,600 MHz FSB, you know immediately that you need a memory module populated with DDR3- 1600 chips, because the chips are always named for the FSB speed. Using the 8:1 module-to-chip/FSB naming rule, the modules that you need would be called PC3-12800, supporting a 12,800 MBps throughput.

The earliest DDR3 chips, however, were based on a 100 MHz actual clock signal, so we can build on our earlier example, which was also based on an actual clock rate of 100 MHz. With eight operations per cycle, the FSB on DDR3 motherboards is rated at 800 MHz, quite a lot of efficiency while still not needing to change the original clock with which our examples began. Applying the 8:1 rule again, the resulting RAM modules for this motherboard are called PC3-6400 and support a throughput of 6,400 MBps, carrying chips called DDR3- 800, again named for the FSB speed.

**DDR4 SDRAM:** Continuing the inevitable march of technology, DDR4 is the next
iteration of SDRAM on the market. As you would expect, the speed of DDR4 is
roughly double that of DDR3. DDR3 provided data rates of approximately 800 Mbps
to 2,133 Mbps, whereas DDR4 ranges between 1,600 Mbps and 3,200 Mbps. DDR
also runs at a lower voltage—1.2 volts. Finally, DDR4 can support more memory per
module, up to 512 GB per chip. Realistically, though, no one produces motherboards (or
RAM) that support that quantity. The largest you will see are 64 GB sticks.

**DDR5 SDRAM:** After a long wait, DDR5 finally hit the market at the end of 2021. Intel’s Alder Lake platform was the first to support it; AMD chips could support DDR5 in early 2022 with the Zen 4 release.

DDR5 doubles the speed of DDR4 to 6.4 Gbps, as is expected for a new memory standard. Improved power efficiency means it runs at 1.1 volts. DDR5 is also the first memory module to be available in up to 128 GB modules.

### SRAM

Static random access memory (SRAM) doesn’t require a refresh signal like DRAM does. The chips are more complex and are thus more expensive. However, they are considerably faster. DRAM access times come in at 40 nanoseconds (ns) or more; SRAM has access times faster than 10ns. SRAM is classically used for cache memory.

### ROM

ROM stands for read-only memory. It is called read-only because you could not write to the original form of this memory. Once information had been etched on a silicon chip and manufactured into the ROM package, the information couldn’t be changed. Some form of ROM is normally used to store the computer’s BIOS because this information normally does not change often.

The system ROM in the original IBM PC contained the power-on self-test (POST), BIOS, and cassette BASIC. Later, IBM computers and compatibles included everything but the cassette BASIC. The system ROM enables the computer to “pull itself up by its bootstraps,” or boot (find and start the operating system).

Through the years, different forms of ROM were developed that could be altered, later ones more easily than earlier ones. The first generation was the programmable ROM (PROM), which could be written to for the first time in the field using a special programming device, but then no more. You may liken this to the burning of a DVD-R.

The erasable PROM (EPROM) followed the PROM, and it could be erased using ultra-violet light and subsequently reprogrammed using the original programming device. These days, flash memory is a form of electronically erasable PROM (EEPROM). Of course, it does not require UV light to erase its contents, but rather a slightly higher than normal electrical pulse. 

> [!info] Note
> Although the names of these memory devices are different, they all contain ROM. Therefore, regardless which of these technologies is used to manufacture a BIOS chip, it’s never incorrect to say that the result is a ROM chip.

## Memory Packaging

The memory slots on a motherboard are designed for particular module form factors or styles. RAM historically evolved from form factors no longer seen for such applications, such as dual in-line package (DIP), single in-line memory module (SIMM), and single in-line pin package (SIPP). The most popular form factors for primary memory modules today are as follows:

- DIMM (dual in-line memory module)
- SODIMM (small outline dual in-line memory module)

Desktop computers will use DIMMs. Laptops and smaller devices require SODIMMs or smaller memory packaging. So, in addition to coordinating the speed of the components, their form factor is an issue that must be addressed.

### DIMM

One type of memory package is known as a DIMM, which stands for dual in-line memory module. DIMMs are 64-bit memory modules that are used as a package for the SDRAM family: SDR, DDR, DDR2, DDR3, DDR4, and DDR5. The term dual refers to the fact that, unlike their SIMM predecessors, DIMMs differentiate the functionality of the pins on one side of the module from the corresponding pins on the other side. With 84 pins per side, this makes 168 independent pins on each standard SDR module, as shown with its two keying notches as well as the last pin labeled 84 on the right side in Figure 1.33. SDR SDRAM modules are no longer part of the CompTIA A+ objectives, and they are mentioned here as a foundation only.

- **Figure 1.32** An SDR dual in-line memory module (DIMM)
![[Image 1.32.png]]

The DIMM used for DDR memory has a total of 184 pins and a single keying notch, whereas the DIMM used for DDR2 has a total of 240 pins, one keying notch, and possibly an aluminum cover for both sides, called a heat spreader and designed like a heat sink to dissipate heat away from the memory chips and prevent overheating. The DDR3 DIMM is similar to that of DDR2. It has 240 pins and a single keying notch, but the notch is in a different location to avoid cross-insertion. Not only is the DDR3 DIMM physically incompatible with DDR2 DIMM slots, it’s also electrically incompatible. A DDR4 DIMM is the same length as a DDR3 DIMM, but is about 0.9mm taller and has 288 pins. The key is in a different spot, so you can’t put DDR4 memory into a DDR2 or DDR3 slot. Finally, DDR5 has 288 pins as DDR4 does but is keyed differently so that DDR4 modules won’t fit into DDR5 slots, and vice versa. Table 1.3 summarizes some key differences between the types of DDR we’ve introduced.

![[Table 1.01]]

Figure 1.34 shows, from top to bottom, DDR4, DDR3, and DDR2 DIMMs.

- **Figure 1.33** DDR4, DDR3, and DDR2 DIMMs
![[Image 1.33.png]]

>[!info] Inserting and Removing Memory Modules
> The original single in-line memory modules had to be inserted into their slots at a 45° angle. The installer then had to apply slight pressure as the module was maneuvered upright at a 90° angle to the motherboard, where a locking mechanism would grip the module and prevent it from returning to its 45° position. This procedure created a pressure that reinforced the contact of the module with its slot. Releasing the clips on either end of the module unlocked it and allowed it to return to 45°, where it could be removed.
> DIMM slots, by comparison, have no spring action. DIMMs are inserted straight into the slot with the locking tabs pulled away from the module. The locking tabs are at either end of the module, and they automatically snap into place, securing the module. Pulling the tabs away from the module releases the module from the slot, allowing it to be effortlessly removed.

### SODIMM 

Laptop computers and other computers that require much smaller components don’t use standard RAM packages, such as DIMMs. Instead, they call for a much smaller memory form factor, such as a small outline DIMM (SODIMM). SODIMMs are available in many physical implementations, including the older 32-bit (72-and 100-pin) configuration and newer 
64-bit (144-pin SDR SDRAM, 200-pin DDR/DDR2, 204-pin DDR3, 260-pin DDR4, and 
262-pin DDR5) configurations.

All 64-bit modules have a single keying notch. The 144-pin module’s notch is slightly off center. Note that although the 200-pin SODIMMs for DDR and DDR2 have slightly different keying, it’s not so different that you don’t need to pay close attention to differentiate the two. They are not, however, interchangeable. DDR3, DDR4, and DDR5 are keyed differently from the others as well. Figure 1.34 shows a DDR3 SODIMM compared to DDR3 and DDR2 DIMMs.

- **Figure 1.34** DDR3 SODIMM vs. DDR3 and DDR2 DIMMs
![[Image 1.34.png]]

> [!info] Note
> For the A+ exam, be sure to know the differences between SODIMMs and DIMMs, DDR3, DDR4, and DDR5, ECC RAM, and single-, dual-, triple-, and quad-channel RAM. Also understand what virtual RAM is.
