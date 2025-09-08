
# Hypervisor

A hypervisor allows multiple operating systems to run on a single physical machine by creating and managing virtual machines. It divides and allocates the hardware resources, like CPU, memory, and storage, to each virtual machine, so they can operate independently. 

There are two types of hypervisors. The main difference between Type 1 and Type 2 hypervisors lies in their interaction with the underlying hardware and operating systems:

## Type 1 Hypervisor (Bare-Metal Hypervisors):

- **Direct Hardware Access:** Type 1 hypervisors run directly on the physical hardware of the host machine, without needing an underlying operating system.

- **Performance:** Generally offers better performance and efficiency because they have direct access to the hardware.

- **Use Case:** Commonly used in enterprise environments and data centers where performance, scalability, and security are critical.

- **Examples:** VMware ESXi, Microsoft Hyper-V, Citrix XenServer.

## Type 2 Hypervisors (Hosted Hypervisors):

- **Runs on an OS:** Type 2 hypervisors run on top of an existing operating system (host OS). They rely on the host OS to manage hardware interactions.

- **Performance:** Typically less efficient than Type 1 hypervisors due to the additional layer of the host OS, which can introduce overhead.

- **Use Case:** Often used for personal or testing environments where ease of setup and flexibility are more important than performance.

- **Examples:** VMware Workstation, Oracle VirtualBox, Parallels Desktop.

Cloud service providers (CSPs) commonly use type one hypervisors. CSPs are responsible for managing the hypervisor and other virtualization components. The CSP ensures that cloud resources and cloud environments are available, and it provides regular patches and updates. Vulnerabilities in hypervisors or misconfigurations can lead to virtual machine escapes (VM escapes). A VM escape is an exploit where a malicious actor gains access to the primary hypervisor, potentially the host computer and other VMs. As a CSP customer, you will rarely deal with hypervisors directly.