# Cooling Systems

It’s a basic concept of physics: electronic components turn electricity into work and heat. The excess heat must be dissipated or it will shorten the life of the components. In some cases (like with the CPU), the component will produce so much heat that it can destroy itself in a matter of seconds if there is not some way to remove this extra heat.

Air-cooling methods are used to cool the internal components of most PCs. With air cooling, the movement of air removes the heat from the component. Sometimes, large blocks of metal called heat sinks are attached to a heat-producing component in order to dissipate the heat more rapidly.

## Fans 

When you turn on a computer, you will often hear lots of whirring. Contrary to popular
opinion, the majority of the noise isn’t coming from the hard disk (unless it’s about to go
bad). Most of this noise is coming from the various fans inside the computer. Fans provide
airflow within the computer. Most PCs have a combination of the following seven fans:

- **Front Intake Fan:** This fan is used to bring fresh, cool air into the computer for
cooling purposes.

- **Rear Exhaust Fan:** This fan is used to take hot air out of the case.

- **Power Supply Exhaust Fan:** This fan is usually found at the back of the power supply,
and it is used to cool the power supply. In addition, this fan draws air from inside the
case into vents in the power supply. This pulls hot air through the power supply so that
it can be blown out of the case. The front intake fan assists with this airflow. The rear
exhaust fan supplements the power supply fan to achieve the same result outside of the
power supply.

- **CPU Fan:** This fan is used to cool the processor. Typically, this fan is attached to a large heat sink, which is in turn attached directly to the processor.

- **Chipset Fan:** Some motherboard manufacturers replaced the heat sink on their onboard chipset with a heat sink and fan combination as the chipset became more advanced. This fan aids in the cooling of the onboard chipset (especially useful when overclocking—setting the system clock frequency higher than the default).

- **Video Card Chipset Fan:** As video cards get more complex and have higher performance, more video cards have cooling fans directly attached. Despite their name, these fans don’t attach to a chipset in the same sense as to a chipset on a motherboard. The chipset here is the set of chips mounted on the adapter, including the GPU and graphics memory. On many late- model graphics adapters, the equivalent of a second slot is dedicated to cooling the adapter. The cooling half of the adapter has vents in the backplane bracket to exhaust the heated air.

- **Memory Module Fan:** The more capable memory becomes of keeping up with the CPU, the hotter the memory runs. As an extra measure of safety, regardless of the presence of heat spreaders on the modules, an optional fan setup for your memory might be in order. 

> [!info] Motherboard Fan Power Connectors
> It’s important to be aware of the two main types of fan connections found on today’s motherboards. One of these connectors has only three connections, while the other has four. The fan connectors and motherboard headers are interchangeable between the two pinouts, but if a chassis fan has four conductors, it’s a sign that it’s calling for connectivity to an extra +5VDC (volts direct current) connection that the most common 3-pin header doesn’t offer. A more rare 3-pin chassis-fan connector features a +12VDC power connection for heavier- duty fans and a rotation pin used as an input to the motherboard for sensing the speed of the fan.
> 
> >
> 
> 4-pin CPU connections place the ground and power connections in pins 1 and 2, respectively, so that 2-pin connectors can be used to power older fans. The 4-pin header also offers a tachometer input signal from the fan on pin 3 so that the speed of the fan can be monitored by the BIOS and other utilities. Look for markings such as CPU FAN IN to identify this function. Pin 4 might be labeled CPU FAN PWM to denote the pulse-width modulation that can be used to send a signal to the fan to control its speed. This is the function lost when a 3-pin connector is placed in the correct position on a 4-pin header. Four-pin chassis-fan connectors can share the tachometer function but replace the speed control function with the extra 5V mentioned earlier.
> 
> >
> 
> Other power connections and types will be covered in Chapter 2, including the Molex connector, which can be used to power chassis and CPU fans using an adapter or the built-in connector on mostly older fans manufactured before the motherboard connectors were standardized. Figure 1.35 shows two 3-pin chassis-fan headers on a motherboard.
> - **Figure 1.35** 3-pin chassis-fan headers
> ![[Image 1.35.png]]
> 
> Figure 1.36 shows a 4-pin CPU fan header with an approaching 3-pin connector from the fan. Note that the keying tab is lined up with the same three pins it’s lined up with in the 3-pin connectors.
> - **Figure 1.36** A 4-pin CPU fan header
> ![[Image 1.36.png]]
> 
> This physical aspect and the similar pin functions are what make these connectors interchangeable, provided that the header’s function matches the role of the fan being connected. Figure 1.37 shows the resulting unused pin on the 4-pin header. Again, controlling the fan’s speed is not supported in this configuration.
> - **Figure 1.37** Position of a 3-pin connector on a 4-pin header 
> ![[Image 1.37.png]] 

Ideally, the airflow inside a computer should resemble what is shown in Figure 1.38, where the back of the chassis is shown on the left in the image. 

- **Figure 1.38** System unit airflow
![[Image 1.38.png]]

Note that you must pay attention to the orientation of the power supply’s airflow. If the power supply fan is an exhaust fan, as assumed in this discussion, the front and rear fans will match their earlier descriptions: front, intake; rear, exhaust. If you run across a power supply that has an intake fan, the orientation of the supplemental chassis fans should be reversed as well. The rear chassis fan(s) should always be installed in the same orientation the power supply fan runs to avoid creating a small airflow circuit that circumvents the cross-flow of air throughout the case. The front chassis fan and the rear fans should always be installed in reverse orientation to avoid having them fight against each other and thereby reduce the internal airflow. Reversing supplemental chassis fans is usually no harder than removing four screws and flipping the fan. Sometimes, the fan might just snap out, flip, and then snap back in, depending on the way it is rigged up. 

## Memory Cooling

If you are going to start overclocking your computer, you will want to do everything in your power to cool all of its components, and that includes the memory.

There are two methods of cooling memory: passive and active. The passive memory cooling method just uses the ambient case airflow to cool the memory through the use of enhanced heat dissipation. For this, you can buy either heat sinks or, as mentioned earlier, special “for memory chips only” devices known as heat spreaders. Recall that these are special aluminum or copper housings that wrap around memory chips and conduct the heat away from them.

Active cooling, on the other hand, usually involves forcing some kind of cooling medium (air or water) around the RAM chips themselves or around their heat sinks. Most often, active cooling methods are just high-speed fans directing air right over a set of heat spreaders.

## Hard Drive Cooling

You might be thinking, “Hey, my hard drive is doing work all the time. Is there anything I can do to cool it off?” There are both active and passive cooling devices for hard drives. Most common, however, is the active cooling bay. You install a hard drive in a special device that fits into a 5¼″ expansion bay. This device contains fans that draw in cool air over the hard drive, thus cooling it. Figure 1.39 shows an example of one of these active hard drive coolers. As you might suspect, you can also get heat sinks for hard drives.

- **Figure 1.39** An active hard disk cooler
![[Image 1.39.png]]

## Chipset cooling

Every motherboard has a chip or chipset that controls how the computer operates. Like other chips in the computer, the chipset is normally cooled by the ambient air movement in the case. However, when you overclock a computer, the chipset may need to be cooled more because it is working harder than it normally would be. Therefore, it is often desirable to replace the onboard chipset cooler with a more efficient one. Refer back to Figure 1.4 for a look at a modern chipset cooling solution. 

## CPU Cooling

Probably the greatest challenge in cooling is the computer’s CPU. It is the component that generates the most heat in a computer (aside from some pretty insane GPUs out there). As a matter of fact, if a modern processor isn’t actively cooled all of the time, it will generate enough heat to burn itself up in seconds. That’s why most motherboards have an internal CPU heat sensor and a CPU_FAN sensor. If no cooling fan is active, these devices will shut down the computer before damage occurs.

There are multiple CPU cooling methods, but the two most common are air cooling and liquid cooling.

### Air Cooling

The parts inside most computers are cooled by air moving through the case. The CPU is no exception. However, because of the large amount of heat produced, the CPU must have (proportionately) the largest surface area exposed to the moving air in the case. Therefore, the heat sinks on the CPU are the largest of any inside the computer.

The CPU fan often blows air down through the body of the heat sink to force the heat into the ambient internal air where it can join the airflow circuit for removal from the case. However, in some cases, you might find that the heat sink extends up farther, using 
radiator-type fins, and the fan is placed at a right angle and to the side of the heat sink. This design moves the heat away from the heat sink immediately instead of pushing the air down through the heat sink. CPU fans can be purchased that have an adjustable rheostat to allow you to dial in as little airflow as you need, aiding in noise reduction but potentially leading to accidental overheating.

It should be noted that the highest- performing CPU coolers use copper plates in direct contact with the CPU. They also use high-speed and high- CFM cooling fans to dissipate the heat produced by the processor. CFM is short for cubic feet per minute, an airflow measurement of the volume of air that passes by a stationary object per minute. Figure 1.40 shows a newer, large heat sink with a fan in the center. In the picture it can be tough to gauge size—this unit is about six inches across! (And to be fair, this heat sink should have a second fan on one of the sides, but with the second fan the heatsink wouldn’t fit into the author’s case—the RAM was in the way.)

- **Figure 1.40** Large heat sink and fan
![[Image 1.40.png]]

Most new CPU heat sinks use tubing to transfer heat away from the CPU. With any cooling system, the more surface area exposed to the cooling method, the better the cooling. Plus, the heat pipes can be used to transfer heat to a location away from the heat source before cooling. This is especially useful in cases where the form factor is small and with laptops, where open space is limited.

With advanced heat sinks and CPU cooling methods like this, it is important to improve the thermal transfer efficiency as much as possible. To that end, cooling engineers came up with a glue-like compound that helps to bridge the extremely small gaps between the CPU and the heat sink, which avoids superheated pockets of air that can lead to focal damage of the CPU. This product is known as thermal transfer compound, or simply thermal compound (alternatively, thermal grease or thermal paste), and it can be bought in small tubes. 
Single-use tubes are also available and alleviate the guesswork involved with how much you should apply. Watch out, though; this stuff makes quite a mess and doesn’t want to come off your fingers very easily. An alternative to the paste is a small thermal pad, which provides heat conductivity between the processor and the heat sink.

Apply the compound by placing a bead in the center of the heat sink, not on the CPU, because some heat sinks don’t cover the entire CPU package. That might sound like a problem, but some CPUs don’t have heat-producing components all the way out to the edges. Some CPUs even have a raised area directly over the silicon die within the packaging, resulting in a smaller contact area between the components. You should apply less than you think you need because the pressure of attaching the heat sink to the CPU will spread the compound across the entire surface in a very thin layer. It’s advisable to use a clean, lint-free applicator of your choosing to spread the compound around a bit as well, just to get the spreading started. You don’t need to concern yourself with spreading it too thoroughly or too neatly because the pressure applied during attachment will equalize the compound quite well. During attachment, watch for oozing compound around the edges, clean it off immediately, and use less next time.

> [!info] Improving and Maintaining CPU Cooling
> In addition to using thermal compound, you can enhance the cooling efficiency of a CPU heat sink by lapping the heat sink, which smoothens the mating surface using a very fine sanding element, about 1000 grit in the finishing stage. Some vendors of the more expensive heat sinks will offer this service as an add-on.
> 
> >
> 
> If your CPU has been in service for an extended period of time, perhaps three years or more, it is a smart idea to remove the heat sink and old thermal compound and then apply fresh thermal compound and reattach the heat sink. Be careful, though; if your thermal paste has already turned into thermal “glue,” you can wrench the processor right out of the socket, even with the release mechanism locked in place. Invariably, this damages the pins on the chip. Try running the computer for a couple of minutes to warm the paste and then try removing the heat sink again. 
> 
> >
> 
> Counterintuitively perhaps, you can remove a sealed heat sink from the processor by gently rotating the heat sink to break the paste’s seal. Again, this can be made easier with heat. If the CPU has risen in the socket already, however, rotating the heat sink would be an extremely bad idea. Sometimes, after you realize that the CPU has risen a bit and that you need to release the mechanism holding it in to reseat it, you find that the release arm is not accessible with the heat sink in place. This is an unfortunate predicament that will present plenty of opportunity to learn.

### Liquid Cooling

Liquid cooling is a technology whereby a special water block is used to conduct heat away from the processor (as well as from the chipset). Water is circulated through this block to a radiator, where it is cooled.

The theory is that you could achieve better cooling performance through the use of liquid cooling. For the most part, this is true. However, with traditional cooling methods (which use air and water), the lowest temperature you can achieve is room temperature. Plus, with liquid cooling, the pump is submerged in the coolant (generally speaking), so as it works, it produces heat, which adds to the overall liquid temperature.

The main benefit to liquid cooling is silence. Only one fan is needed: the fan on the radiator to cool the water. So, a liquid- cooled system can run extremely quietly.

There are two major classifications of liquid cooling systems in use with PCs today: all- in- one (AIO) coolers and custom loop systems. AIO systems are relatively easy to install—they require about as much effort as a heat sink and fan—and comparably priced to similarly effective air systems. Figure 1.41 shows an example from Corsair, with the pump in front and the fans behind it, attached to the radiator.

- **Figure 1.41** AIO liquid cooling system
![[Image 1.41.png]]

AIO systems come in three common sizes: 120 mm (with one fan, and the most common), 240 mm (two fans, for overclocked components), and 360 mm (three fans, for high- end multicore overclocked components). Options with RGB lighting are readily available if that’s the style you want. Custom loop systems can quickly become complex and expensive, but many hardcore gamers swear by their performance. The components are essentially the same as those in an AIO system—there’s a radiator, pump, fans, some tubes, and liquid. However, each part is purchased separately, and some assembly is required.

> [!info] Tip 
> Water cooling systems often require more room inside the case than heat sinks, as well as special headers on the motherboard (or in the case) to support the fans. As always, check your documentation to be sure that your other hardware is compatible!
