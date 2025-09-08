
# Inside operating systems

Previously, you learned about what operating systems are. Now, let's discuss how they work. In this video, you'll learn what happens with an operating system, or OS, when someone uses a computer for a task. 

Think about when someone drives a car. They push the gas pedal and the car moves forward. They don't need to pay attention to all the mechanics that allow the car to move. Just like a car can't work without its engine, a computer can't work without its operating system. 

The job of an OS is to help other computer programs run efficiently. The OS does this by taking care of all the messy details related to controlling, the computer's hardware, so you don't have to. 

First, let's see what happens when you turn on the computer. When you press the power button, you're interacting with the hardware. This boots the computer and brings up the operating system. Booting the computer means that a special microchip called a BIOS is activated. On many computers built after 2007, the chip was replaced by the UEFI. Both BIOS and UEFI contain booting instructions that are responsible for loading a special program called the [[Bootloader|bootloader]]. Then, the bootloader is responsible for starting the operating system. Just like that, your computer is on. 

As a security analyst, understanding these processes can be helpful for you. Vulnerabilities can occur in something like a booting process. Often, the BIOS is not scanned by the antivirus software, so it can be vulnerable to malware infection. Now, that you learned how to boot the operating system, let's look at how you and all users communicate with the system to complete a task. 

The process starts with you, the user. And to complete tasks, you use applications on your computer. An application is a program that performs a specific task. When you do this, the application sends your request to the operating system. From there, the operating system interprets this request and directs it to the appropriate component of the computer's hardware. 
The hardware will also send information back to the operating system. And this in turn is sent back to the application. See [[Diagram 1.18]] for a visual representation of this process.

![[Diagram 1.18]]

Let's give a simple overview of how this works when you want to use the calculator on your computer. You use your mouse to click on the calculator application on your computer. When you type in the number you want to calculate, the application communicates with the operating system. Your operating system then sends a calculation to a component of the hardware, the central processing unit, or CPU. Once the hardware does the work of determining the final number, it sends the answer back to your operating system. Then, it can be displayed in your calculator application. 

Understanding this process is helpful when investigating security events. Security analysts should be able to trace back through this process flow to analyze where a security event could have occurred. 

Just like a mechanic needs to understand the inner workings of a car more than an average driver, recognizing how operating systems work is important knowledge for a security analyst. 