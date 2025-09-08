
# Power Supply

[[🏷️PC hardware]]

The computer’s components would not be able to operate without power. The device in the computer that provides this power is the power supply (see Figure 1.67). A power supply converts 110V or 220V AC current into the DC voltages that a computer needs to operate. These are +3.3VDC, +5VDC, –5VDC (on older systems), +12VDC, and –12VDC. The jacket on the leads carrying each type of voltage has a different industry-standard color-coding for faster recognition. Black ground leads offer the reference that gives the voltage leads their respective magnitudes. The +3.3VDC voltage was first offered on ATX motherboards.

- **Figure 1.67** A desktop power supply
![[Image 1.67.png]]

> [!info] Note
> You will see the term PSU in reference to a power supply unit.

Throughout this section, you will see us use the terms watts, volts, and amps. If you’re working with electricity a lot, you might also see the term ohms. To help understand what these terms mean, let’s use an analogy of water flowing through a pipe. Amps would be the amount of water flowing through the pipe; voltage would be the water pressure; and watts would be the power that the water could provide. (Watts mathematically are volts × amps.) If there were a filter or other barrier in the pipe, that would provide resistance, which is measured in ohms. In non-analogous terms, amps are the unit of current flow; volts are the unit of force; watts are the unit for power (watts = volts × amps); and ohms are resistance.

> [!info] Note
> The abbreviation VDC stands for volts DC. DC is short for direct current. Unlike alternating current (AC), DC does not alter the direction in which the electrons flow. AC for standard power distribution does so 50 or 60 times per second (50 or 60 Hz, respectively). Sometimes you will see people abbreviate a current such as positive 5 volts as +5V, and other times as +5VDC. It’s really a matter of preference.

> [!info] Note
> Be aware that DC voltage is not safer than AC voltage, despite its common use in batteries and lower-power components. Direct current is more likely to cause a prolonged clamping of the muscles than AC, which is more likely to fibrillate the heart, resulting in a deadly loss of coordination of the various cardiac muscles. Furthermore, power supplies contain transformers and capacitors that can discharge lethal amounts of current even when disconnected from the wall outlet for long periods. They are not meant to be serviced, especially by untrained personnel. Do not attempt to open them or do any work on them. Simply replace and recycle them when they go bad.

## Power Supply Input

Computer power supplies need to get their power from somewhere, and that is typically a wall outlet. There may be an intermediary battery backup device in-between called an uninterruptible power supply (UPS), which we will talk about later in the “Battery Backup Systems” section, but the point is that the power supply doesn’t just generate its own power. It converts AC power from the wall into DC power that components use.

Countries have differing standards on the voltage provided by wall outlets. In the United States, it’s typically 110V and 220V. The 110V outlets are the “normal” outlets that most electronics, including computers, are plugged into. The 220V outlets are for high-energy devices such as electric ranges and clothes dryers. Fortunately, the two plugs are completely different (as shown in Figure 1.68) to help us avoid plugging the wrong thing into the wrong place and frying the component. As noted, though, other countries have different standards, and power supply manufacturers want to ensure their devices work in different countries.

- **Figure 1.68** 110V (left) and 220V (right) wall outlets
![[Image 1.68.png]]

Therefore, some power supplies have a recessed, two-position slider switch, often a red one, on the rear that is exposed through the case. You can see the one for the power supply shown in Figure 2.26. Dual-voltage options on such power supplies read 110 and 220, 115 and 230, or 120 and 240. This selector switch is used to adjust for the voltage level used in the country where the computer is in service. As noted earlier, in the United States, the power grid supplies anywhere from 110V to 120V. However, in Europe, for instance, the voltage supplied is double, ranging from 220V to 240V.

Although the voltage is the same as what is used in the United States to power high-voltage appliances, the amperage is much lower. The point is, the switch is not there to allow multiple types of outlets to be used in the same country. If the wrong voltage is chosen in the United States, the power supply will expect more voltage than it receives and might not power up at all. If the wrong voltage is selected in Europe, however, the power supply will receive more voltage than it is set for. The result could be disastrous for the entire computer and could result in sparking or starting a fire. Always check the switch before powering up a new or recently relocated computer. In the United States and other countries that use the same voltage, check the setting of this switch if the computer fails to power up.

## Power Supply Output and Ratings

Power supplies all provide the same voltages to a system, such as +3.3V, +5V, and +12V. Each of these can be referred to as a rail because each one comes from a specific tap (or rail) within the power supply. Some power supplies provide multiple 12V rails in an effort to supply more power overall to components that require 12V. For instance, in dual-rail power supplies, one rail might be dedicated to the CPU, while the other is used to supply power to all of the other components that need 12V.

The problem that can arise in high-powered systems is that although the collective power supplied by all rails is greater than that supplied by power supplies with a single rail, each rail provides less power on its own. As a result, it is easier to overdraw one of the multiple rails in such a system, causing a protective shutdown of the power supply. Care must be taken to balance the load on each of the rails if a total amperage greater than any one rail is to be supplied to attached components. Otherwise, if the total power required is less than any single rail can provide, there is no danger in overloading any one rail.

Power supplies are rated in watts. A watt is a unit of power. The higher the number, the more power your computer can draw from the power supply. Think of this rating as the “capacity” of the device to supply power. Most computers require power supplies in the 350- to 500-watt range. Higher wattage power supplies, say 750- to 900-watt, might be required for more advanced systems that employ power-hungry graphics cards or multiple disk drives, for instance. As of this writing, power supplies of up to 2,000 watts were available for desktop machines. It is important to consider the draw that the various components and subcomponents of your computer place on the power supply before choosing one or its replacement.

> [!info] Real World Scenario
> **How much power do you really need?**
> 
>>
>
> Having a power supply that doesn’t provide sufficient wattage to system components will result in brownouts, intermittent reboots, or even the system failing to power up. Having too much power is a little inefficient, but you won’t have to worry about failures such as those. The question is, how much do you really need? 
> 
> >
> 
> Most power- hungry devices (and we’re looking at you, video cards) will give you a minimum power supply requirement. Generally speaking, the video card is the biggest power user, so if you meet these requirements, you should be fine. The manufacturer assumes you have otherwise standard gear in the system and adds a bit of a buffer.
> 
> >
> 
> Another option, if you are building a system, is to use the System Builder feature on a website we love called PCPartPicker.com. As you add components to the system, the site automatically calculates the estimated wattage drawn and displays it on the page. Pick a PSU that supplies more than that amount of power and you should be in the clear.

## Power Connectors

The connectors coming from the power supply are quite varied these days. Some PSUs will have connectors permanently attached, where other PSUs give you the ability to attach and detach power connectors as needed, based on the devices installed in the system. 

### ATX, ATX12V, and EPS12V Connectors

ATX motherboards use a single block connector from the power supply. When ATX boards were first introduced, this connector was enough to power all the motherboard, CPU, memory, and all expansion slots. The original ATX system connector provides the six voltages required, plus it delivers them all through one connector: an easy-to-use single 20-pin connector. Figure 1.69 shows an example of an ATX system connector.

- **Figure 1.69** 20-pin ATX power connector
![[Image 1.69.png]]

When the Pentium 4 processor was introduced, it required much more power than previous CPU models. Power, measured in watts, is a multiplicative function of voltage and current. To keep the voltage low meant that amperage would have to increase, but it wasn’t feasible to supply such current directly from the power supply itself. Instead, the solution was to deliver 12V at lower amperage to a voltage regulator module (VRM) located near the CPU. This approach allowed higher current at a lower voltage over the shorter distance to the CPU.

As a result of this shift, motherboard and power supply manufacturers needed to provide this more varied power to the system board. The ATX12V 1.0 standard was introduced to address this, which added two supplemental connectors. One was a single 6-pin auxiliary connector that supplied additional +3.3V and +5V leads along with their grounds. The other was a 4-pin square mini-version of the ATX connector, known as the P4 connector (named after the processor that first required it). The P4 connector supplied two +12V leads and their grounds.

The EPS12V standard later evolved to use an 8-pin version of the processor power connector, referred to as the processor power connector. This 8-pin connector doubled the functionality of the P4 connector, providing four +12V leads and four grounds. Figure 1.70 illustrates the P4 connector. The 8-pin processor power connector has two rows of 4 pins and is keyed differently from the 8-pin PCIe power connector, which will be discussed shortly.

- **Figure 1.70** ATX12V P4 power connector
![[Image 1.70.png]]

PCIe devices require more power than PCI ones did. So, for ATX motherboards with PCIe slots, the 20-pin system connector proved inadequate. This led to the ATX12V 2.0 standard and the even higher- end EPS12V standard for servers. These specifications call for a 
24-pin connector that adds further positive voltage leads directly to the system connector. The 24-pin connector looks like a larger version of the 20-pin connector. The corresponding pins of the 24-pin motherboard header are actually keyed to accept the 20-pin connector. Adapters are available if you find yourself with the wrong combination of motherboard and power supply. Some power supplies feature a 20- pin connector that snaps together with a separate 4-pin portion for flexibility, called a 20+4 connector, which can be seen in Figure 1.71. Otherwise, it will just have a 24-pin connector. The 6-pin auxiliary connector disappeared with the ATX12V 2.0 specification and was never part of the EPS12V standard. 

- **Figure 1.71** A 24- pin ATX12V 2.x connector, in two parts
![[Image 1.71.png]]

> [!info] Note
> The adapter mentioned in the previous paragraph is called a 20-pin to 24-pin motherboard adapter, which is a specific subobjective of A+ exam 220-1101 objective 3.5: Given a scenario, install or replace the appropriate power supply. 

ATX12V 2.1 introduced a different 6-pin connector, which was shaped a lot like the P4 connector (see Figure 1.72). This 6-pin connector was specifically designed to give additional dedicated power to the PCIe adapters that required it. It provided a 75W power source to such devices. 

- **Figure 1.72** A 6- pin ATX12V 2.1 PCIe connector
![[Image 1.72.png]]

ATX12V 2.2 replaced the 75W 6-pin connector with a 150W 8-pin connector, as shown in Figure 1.73. The plastic bridge between the top two pins on the left side in the photo keeps installers from inserting the connector into the EPS12V processor power header but clears the notched connector of a PCIe adapter. The individual pin keying should avoid this issue, but a heavy-handed installer could defeat that. The bridge also keeps the connector from being inserted into a 6-pin PCIe header, which has identically keyed corresponding pins. 

- **Figure 1.73** An 8- pin ATX12V 2.2 PCIe connector
![[Image 1.73.png]]

### Proprietary Power Connectors

Although the internal peripheral devices have standard power connectors, manufacturers of computer systems sometimes take liberties with the power interface between the motherboard and power supply of their systems. It’s uncommon but not unheard of. In some cases, the same voltages required by a standard ATX power connector are supplied using one or more proprietary connectors. This makes it virtually impossible to replace power supplies and motherboards with other units “off the shelf.” Manufacturers might do this to solve a design issue or simply to ensure repeat business.

### SATA Power Connectors

SATA drives arrived on the market with their own power requirements in addition to their new data interfaces. (Refer back to Figure 2.9 to see the SATA data and power connectors.) You get the 15-pin SATA power connector, a variant of which is shown in Figure 1.74. The fully pinned connector is made up of three +3.3V, three +5V, and three +12V leads interleaved with two sets of three ground leads. Each of the five sets of three common pins is supplied by one of five single conductors coming from the power supply. When the optional 3.3V lead is supplied, it is standard to see it delivered on an orange conductor.

- **Figure 1.74** SATA power connector
![[Image 1.74.png]]

Note that in Figure 1.74, the first three pins are missing. These correspond to the 3.3V pins, which are not supplied by this connector. This configuration works fine and alludes to the SATA drives’ ability to accept Molex connectors or adapters attached to Molex connectors, thus working without the optional 3.3V lead.

> [!info] Note
> Older PATA hard drives and optical drives used a thicker 4-pin power connector called a Molex connector. An example is shown in Figure 1.75. The connector is keyed with two beveled corners, making it nearly impossible to install incorrectly.

- **Figure 1.75** Molex power connector
![[Image 1.75.png]]

## Modular Power Supplies

On older PSUs, all power connectors were hardwired into the power supply itself. This had a number of interesting side effects. One was that no matter how many or how few internal devices were present, there were a fixed number of connectors. Power supply manufacturers generally provided enough so most users wouldn’t run short of connectors. The flip side of this was that there were often four to six unused connectors, but the cables were still taking up space inside the case. Zip ties and thick rubber bands helped maintain the chaos. 

As the variety of internal components became more complex, the need arose to have more flexibility in terms of the connectors provided. Out of this need rose an elegant solution—the modular power supply. From a functional standpoint, it works just as a non- modular power supply does. The difference is that none of the power cables are permanently attached. Only the ones that are needed are connected. Figure 1.76 shows the side of a fully modular power supply. The top row has connectors for the motherboard (left and center) and CPU or PCIe device. On the bottom row, you can see four 6-pin peripheral connectors and three 8-pin ones to power the CPU or PCIe devices.

- **Figure 1.76** Modular power supply
![[Image 1.76.png]]

You will also see semi-modular PSUs on the market. Generally, the motherboard and CPU connectors will be hardwired, whereas the peripheral connectors can be added as needed. There are two potential disadvantages to using a fully modular or semi-modular power supply. First, some PSU manufacturers use proprietary connectors. Always be sure to keep the extra power connectors around (many come with a bag to store unused cables) just in case they are needed. Second, modular PSUs can take up a little more room in the case. Plugging the power connectors into the PSU can take up an extra ¼ or ½ inch. Usually this isn’t an issue, but it can be in smaller cases.

## Redundant Power Supplies

Nearly every computer you will work with has one and only one power supply—is that enough? If the PSU supplies the right amount of wattage to safely power all components, then the answer is nearly always yes. There are some instances, though, where power redundancy is helpful or even critical. Within the realm of power redundancy, there are two paths you can take: redundant power supplies within a system or battery backups. Let’s look at both.

### Multiple PSUs

It’s almost unheard of to see two power supplies installed in a desktop computer. There’s generally no need for such a setup and it would just be a waste of money. And for laptops and mobile devices, it’s simply not an option. For servers, though, having a redundant power supply (RPS), meaning a second PSU installed in the system, might make sense. The sole reason to have two power supplies is in case one fails, the other can take over. The transition between the two is designed to be seamless and service will not be disrupted. 

Based on its name and our description so far, it might seem as though this means installing two full-sized PSUs into a computer case. Given the limited amount inside a case, you can imagine how problematic this could be. Fortunately, though, PSU manufacturers make devices that have two identical PSUs in one enclosure. One such example is shown in Figure 1.77. The total device is designed to fit into ATX cases and is compliant with ATX12V and EPS12V standards. If one fails, the other automatically takes over. They are 
hot-swappable, so the failed unit can be replaced without powering the system down.

- **Figure 1.77** Hot- swappable redundant PSUs
![[Image 1.77.png]]

Although an RPS can help in the event of a PSU failure, it can’t keep the system up and running if there is a power outage.

### Battery Backup Systems

The second type of power redundancy is a battery backup system that the computer plugs into. This is commonly referred to as an uninterruptible power supply (UPS).

These devices can be as small as a brick, like the one shown in Figure 1.78, or as large as an entire server rack. Some just have a few indicator lights, whereas others have LCD displays that show status and menus and come with their own management software. The back of the UPS will have several power plugs. It might divide the plugs such that a few of them provide surge protection only, whereas others provide surge protection as well as backup power, as shown in Figure 1.79.

- **Figure 1.78** An uninterruptible power supply
![[Image 1.78.png]]

- **Figure 1.79** The back of an uninterruptible power supply
![[Image 1.79.png]]

Inside the UPS are one or more batteries and fuses. Much like a surge suppressor, a UPS is designed to protect everything that’s plugged into it from power surges. UPSs are also designed to protect against power sags and even power outages. Energy is stored in the batteries, and if the power fails, the batteries can power the computer for a period of time so that the administrator can then safely power it down. Many UPSs and operating systems will also work together to safely power down automatically a system that gets switched to UPS power. These types of devices may be overkill for Uncle Bob’s machine at home, but they’re critically important fixtures in server rooms.

The UPS should be checked periodically to make sure that its battery is operational. Most UPSs have a test button that you can press to simulate a power outage. You will find that batteries wear out over time, and you should replace the battery in the UPS every couple of years to keep the UPS dependable.

> [!info] Note
> UPSs all have a limit as to how many devices they can handle at once. These power limitations should be strictly observed. If overloaded, it can cause a short, which could potentially result in fire. 

## Replacing Power Supplies

Sometimes power supplies fail. Sometimes you grow out of your power supply and require more wattage than it can provide. Often, it is just as cost effective to buy a whole new case with the power supply included rather than dealing with the power supply alone. However, when you consider the fact that you must move everything from the old case to the new one, replacing the power supply becomes an attractive proposition. Doing so is not a difficult task.

Regardless of which path you choose, you must make sure the power connection of the power supply matches that of the motherboard to be used. Additionally, the physical size of the power supply should factor into your purchasing decision. If you buy a standard ATX-compatible power supply, it might not fit in the petite case you matched up to your micro ATX motherboard. In that scenario, you should be on the lookout for a smaller form factor power supply to fit the smaller case. Odds are that the offerings you find will tend to be a little lighter in the wattage department as well.

The following instructions detail the process to remove an existing power supply. Use the reverse of this process to install the new power supply. Just keep in mind that you might need to procure the appropriate adapter if a power supply that matches your motherboard can no longer be found. There is no post-installation configuration for the power supply, so there is nothing to cover along those lines. Many power supply manufacturers have utilities on their websites that allow you to perform a presale configuration so that you are assured of obtaining the most appropriate power supply for your power requirements.

> [!info] Removing a Power Supply
> 1. With the power source removed from the system, ground yourself and the computer to the same source of ground.
> 2. Remove the cover from the system, exposing the internal components.
> 3. After locating the power supply, which can come in a variety of formats and appear on the left or right side of the case, follow all wiring harnesses from the power supply to their termini, disconnecting each one. 
> 4. Remove any obstructions that appear as if they might hinder the removal of the power supply.
> 5. Using the dimensions of the power supply, detectable from the inside of the case, note which machine screws on the outside of the case correspond to the power supply. There are often four such screws in a non-square pattern. If your case has two side panels, and you removed only one, there will likely be one or more screws holding the other panel on that appear to be for the power supply. These do not need to be removed. If all case screws have been removed, pay attention to their location and do not use these holes when securing the new power supply.
> 6. Remove the screws that you identified as those that hold the power supply in place. Be aware that the power supply is not lightweight, so you should support it as you remove the final couple of screws.
> 7. Maneuver the power supply past any obstructions that did not have to be removed, and pull the power supply out of the case.

## AC Adapters as Power Supplies

Just as the power supply in a desktop computer converts AC voltages to DC for the internal components to run on, the AC adapter of a laptop computer converts AC voltages to DC for the laptop’s internal components. And AC adapters are rated in watts and selected for use with a specific voltage just as power supplies are rated. One difference is that AC adapters are also rated in terms of DC volts out to the laptop or other device, such as certain brands and models of printer.

Because both power supplies and AC adapters go bad on occasion, you should replace them both and not attempt to repair them yourself. When replacing an AC adapter, be sure to match the size, shape, and polarity of the tip with the adapter you are replacing. However, because the output DC voltage is specified for the AC adapter, be sure to replace it with one of equal output voltage, an issue not seen when replacing AT or ATX power supplies, which have standard outputs. Additionally, and as with power supplies, you can replace an AC adapter with a model that supplies more watts to the component because the component uses only what it needs.

> [!info] Note
> For the exam, you need to know the characteristics of power supplies as well as how to install and replace them. Topics you should be familiar with include: 
> - Input 115V vs. 220V
> - Output 3.3V vs. 5V vs. 12V
> - 20-pin to 24-pin motherboard adapter
> - Redundant power supply
> - Modular power supply
> - Wattage rating
