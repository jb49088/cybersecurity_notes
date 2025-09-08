
# Central Processing Unit (CPU)

[[🏷️PC hardware]]

The role of the CPU, or central processing unit, is to control and direct all the activities of the computer using both external and internal buses. From a technical perspective, the job of the CPU is to process, or do math, on large strings of binary numbers—0s and 1s. It is a processor chip consisting of an array of millions of transistors. Intel and Advanced Micro Devices, Inc. (AMD) are the two largest PC-compatible CPU manufacturers. Their chips were featured in Table 1.1 during the discussion of the sockets into which they fit.

Today’s AMD and Intel CPUs should be compatible with every PC-based operating system and application in the market. It’s possible that you could run into an app that doesn’t work quite right on an AMD chip, but those cases are exceedingly rare. From a compatibility standpoint, the most important thing to remember is that the motherboard and processor need to be made for each other. The rest of the hardware plugs into the motherboard and will be CPU brand agnostic.

> [!info] Note
> The term chip has grown to describe the entire package that a technician might install in a socket. However, the word originally denoted the silicon wafer that is generally hidden within the carrier that you actually see. The external pins that you see are structures that can withstand insertion into a socket and are carefully threaded from the wafer’s minuscule contacts. Just imagine how fragile the structures must be that you don’t see.

Older CPUs are generally square, with contacts arranged in a pin grid array (PGA). Prior to 1981, chips were found in a rectangle with two rows of 20 pins known as a dual in-line package (DIP)—see Figure 1.26. There are still integrated circuits that use the DIP form factor; however, the DIP form factor is no longer used for PC CPUs. Most modern CPUs use the LGA form factor. Figure 1.10, earlier in this chapter, shows an LGA socket next to a PGA socket. Additionally, the ATX motherboard in Figure 1.2 has a PGA socket, whereas the micro ATX motherboard has an LGA.

- **Figure 1.26** DIP and PGA
![[Image 1.26.png]]

Intel and AMD both make extensive use of an inverted socket/processor combination of sorts. As mentioned earlier, the LGA packaging calls for the pins to be placed on the motherboard, while the mates for these pins are on the processor packaging. As with PGA, LGA is named for the landmarks on the processor, not the ones on the motherboard. As a result, the grid of metallic contact points, called lands, on the bottom of the CPU gives this format its name.

You can easily identify which component inside the computer is the CPU because it is a large square lying flat on the motherboard with a very large heat sink and fan (refer to Figure 1.10). The CPU is almost always located very close to the RAM to improve system speed, as shown in Figure 1.1, Figure 1.2, and Figure 1.8.

## CPU Architecture

As noted in the previous section, the functional job of the processor is to do math on very large strings of 0s and 1s. How the CPU goes about doing that depends upon its architecture. For commonly used processors, there are two major categories—those based on Complex Instruction Set Computing (CISC) and those based on Reduced Instruction Set Computer (RISC).

### x64/x86

CISC (pronounced like disk, but with a “c”) and RISC (pronounced risk) are examples of an instruction set architecture (ISA). Essentially, it’s the set of commands that the processor can execute. Both types of chips, when combined with software, can ultimately perform all the same tasks. They just go about it differently. When programmers develop code, they develop it for a CISC or a RISC platform.

As the CISC name implies, instructions sent to the computer are relatively complex (as compared to RISC), and as such they can do multiple mathematical tasks with one instruction, and each instruction can take several clock cycles to complete. We’ll talk more about CPU speeds in the “CPU Characteristics” section later, but for now, know that if a CPU is advertised as having 3.8 GHz speed, that means it can complete roughly 3.8 billion cycles in one second. The core of a processor can only do one thing at a time—it just does them very, very quickly so it looks like it’s multitasking.

CISC was the original ISA for microprocessors, and the most well-known example of CISC technology is the x64/x86 platform popularized by Intel. AMD processors are CISC chips as well. So where did the terms x64 and x86 come from? First, just a bit more theory. There is a set of data lines between the CPU and the primary memory of the system—remember the bus? The most common bus today is 64 bits wide, although there are still some 32-bit buses kicking around out there. In older days, buses could theoretically be as narrow as 2 bits, and 8-bit and 16-bit buses were popular for CPUs for several years. The wider the bus, the more data that can be processed per unit of time, and hence, more work can be performed. Internal registers in the CPU might be only 32 bits wide, but with a 64-bit system bus, two separate pipelines can receive information simultaneously. For true 64-bit CPUs, which have 64-bit internal registers and can run x64 versions of Microsoft operating systems, the external system data bus will always be 64 bits wide or some larger multiple thereof.

In the last paragraph, we introduced the term x64, which refers to processors designed to handle 64 bits of data at a time. Correspondingly, the operating system must also be designed to work with x64 chips.

Contrast that with processors that can handle only 32 bits of information at once. Those are referred to as x86 processors. You might look at that last sentence and be certain that we made a typo, but we didn’t. For a long time, when 32-bit processors were the fastest on the PC market, Intel was the dominant player. Their CPUs had names like 80386 (aka i386) and 80486 (i486) and were based on the older 16-bit 80286 and 8086. Since the i386 and i486 were the most popular standards, the term x86 sprung up to mean a 32-bit architecture. So even though it may seem counterintuitive due to the numbers, x64 is newer and faster than x86.

### Advanced RISC Machine

Moving into the RISC architecture, the primary type of processor used today is known as an Advanced RISC Machine (ARM) CPU. Depending on who you talk to and which sources you prefer, there are conflicting stories on if that’s actually the right acronym, as ARM is also known as an Acorn RISC Machine. Regardless of what it stands for, ARM is a competing technology to Intel and AMD x64-based CPUs.

Based on the RISC acronym, one might think that the reduced set of instructions the processor can perform makes it inferior somehow, but that’s not the case. Tasks just need to get executed in different ways. To use a human example, let’s say that we tell you to add the number 7 to itself seven times. One way to do that is to use one step of multiplication: 7 × 7 equals 49. But what if we said you can’t use multiplication? You can still get to the answer by using addition. It will just take you seven steps instead of one. Same answer, different process. That’s kind of how RISC compares to CISC.

RISC processors have some advantages over their CISC counterparts. They can be made smaller than CISC chips and they produce less heat, making them ideal for mobile devices. In fact, nearly all smartphones use RISC-based chips, such as Apple’s A15 and Samsung’s Exynos series processors. On the downside, RISC processors use more memory than CISC ones do because it takes more code to complete a task with a RISC chip.

Like x64/x86, ARM processors have evolved over time—64-bit implementations are the most current, and they are designated ARM64; 32-bit versions are known simply as ARM.

### CPU Cores

Older processors were single-core, meaning that there was one set of instruction pathways through the processor. Therefore, they could process one set of tasks at a time. Designers then figured out how to speed up the computer by creating multiple cores within one processor package. Each core effectively operates as its own independent processor, provided that the operating system and applications are able to support multicore technology. (Nearly all do.)

Today, almost all desktop CPUs in the market are multicore. The number of cores you want may determine the processor to get. For example, the 10th-generation Intel Core i7 has eight cores whereas the i5 has six.

> [!info] Note
> As an interesting aside, throughout the 1980s and 1990s, processor clock speeds grew at very fast rates. But they haven’t gotten much faster over the last 10–15 years as designers ran into technical limitations for increasing speeds. Instead, computers have gotten faster because of the introduction of multicore processors, which is basically like having four (or six or eight) separate processors in one computer.

## CPU Characteristics

When looking for a processor, you might have several decisions to make. Do you want an Intel or AMD CPU? Which model? How fast should it be? What features does it need to support? In this section, we will take a look at some characteristics of processor performance.

### Speed

The speed of the processor is generally described in clock frequency. Older chips were rated in megahertz (MHz) and new chips in gigahertz (GHz). Since the dawn of the personal computer industry, motherboards have included oscillators, quartz crystals shaved down to a specific geometry so that engineers know exactly how they will react when a current is run through them. The phenomenon of a quartz crystal vibrating when exposed to a current is known as the piezoelectric effect. The crystal (XTL) known as the system clock keeps the time for the flow of data on the motherboard. How the front-side bus uses the clock leads to an effective clock rate known as the FSB speed. As discussed in the section “Types of Memory” later in this chapter, the FSB speed is computed differently for different types of RAM (DDR3, DDR4, DDR5, and so forth). From here, the CPU multiplies the FSB speed to produce its own internal clock rate, producing the third speed mentioned thus far.

As a result of the foregoing tricks of physics and mathematics, there can be a discrepancy between the front-side bus frequency and the internal frequency that the CPU uses to latch data and instructions through its pipelines. This disagreement between the numbers comes from the fact that the CPU is capable of splitting the clock signal it receives from the external oscillator that drives the front-side bus into multiple regular signals for its own internal use. In fact, you might be able to purchase a number of processors rated for different (internal) speeds that are all compatible with a single motherboard that has a front-side bus rated, for instance, at 1,333 MHz. Furthermore, you might be able to adjust the internal clock rate of the CPU that you purchased through settings in the BIOS.

The speed of a processor can also be tweaked by overclocking, or running the processor at a higher speed than the one at which the manufacturer rated it. Running at a higher speed requires more voltage and also generates more heat, which can shorten the life of the CPU. Manufacturers often discourage the practice (of course, they want you to just buy a faster and more expensive CPU), and it usually voids any warranty. However, some chips are sold today that specifically give you the ability to overclock them. Our official recommendation is to not do it unless the manufacturer says it’s okay. If you’re curious, plenty of information on how to overclock is available online.

### Multithreading and Hyper-Threading

The string of instructions that a CPU runs is known as a thread. Old processors were capable of running only one thread at a time, whereas newer ones can run multiple threads at once. This is called multithreading.

Intel markets their multithreading technology as Hyper-Threading Technology (HTT). HTT is a form of simultaneous multithreading (SMT). SMT takes advantage of a modern CPU’s superscalar architecture. Superscalar processors can have multiple instructions operating on separate data in parallel.

HTT-capable processors appear to the operating system as two processors. As a result, the operating system can schedule two processes at the same time, similar to symmetric multiprocessing (SMP), where two or more processors use the same system resources. In fact, the operating system must support SMP in order to take advantage of HTT. If the current process stalls due to issues like cache or branch prediction, the processor's execution resources can be reallocated to another process that is ready to execute, reducing processor downtime.

HTT manifests itself in the Windows 10 Task Manager by showing graphs for twice as many CPUs as the system has cores. These virtual CPUs are listed as logical processors (see Figure 1.27).

- **Figure 1.27** Logical processors in Windows
![[Image 1.27.png]]

For an in-market example, compare the Intel i5 with the Intel i7. Similar models will have the same number of cores (say, four), but the i7 supports HTT, whereas the i5 does not. This gives the i7 a performance edge over its cousin. The i9 will be even one further step up from the i7. For everyday email and internet use, the differences won’t amount to much. But for someone using resource-intensive applications such as online gaming or virtual reality, especially between i5 and i9 processors, the differences can be important.

> [!info] Real World Scenario
> **Which CPU Do You Have?**
> The surest way to determine which CPU your computer is using is to open the case and view the numbers stamped on the CPU, a process that today requires removal of the active heat sink. However, you may be able to get an idea without opening the case and removing the heat sink and fan because many manufacturers place a very obvious sticker somewhere on the case indicating the processor type. Failing this, you can always go to the manufacturer’s website and look up the information on the model of computer you have.
> 
> >
> 
> An easier way to determine your computer's CPU may be to look in Control Panel ➢ System to access the About screen, as shown in Figure 1.28. For even more detailed information, you can run System Information by clicking Start and entering `msinfo32.exe`. Click on System Information when it appears as the Best Match. Alternatively, third-party utilities such as CPU-Z, which we mentioned earlier, can provide detailed information about your CPU. Another method is to save your work, exit any open programs, and restart the computer. Watch closely during the POST routine (Power-On Self-Test); you should see a notation that tells you what chip you are using.
> 
> - **Figure 1.28** System information an the About screen
> ![[Image 1.28.png]]

### Virtualization Support

Many of today’s CPUs support virtualization in hardware, which eases the burden on the system that software-based virtualization imposes. For more information on virtualization, see Chapter 8, “Virtualization and Cloud Computing.” AMD calls its virtualization technology AMD-V (V for virtualization), whereas Intel calls theirs Virtualization Technology (VT). Most processors made today support virtual technology, but not all. Keep in mind that the BIOS/UEFI and operating system must support it as well for virtualization to work. You may need to manually enable the virtualization support in the BIOS/UEFI before it can be used.

As shown in Figure 1.29, the CPU Technologies tab of this utility tells you if your CPU supports Intel VT.

- **Figure 1.29** Intel Processor Identification Utility
![[Image 1.29.png]]

> [!info] Note
> The CompTIA A+ objectives for CPUs aren’t quite as long as they were for motherboards. For CPUs, be sure to understand the differences between x64/x86/ARM, single- core and multicore, multithreading, and virtualization support.
