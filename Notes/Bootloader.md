# Bootloader

[[🏷️OS component]]

A bootloader is a small program that loads the operating system (OS) into memory when a computer or device starts up. It is responsible for initiating the boot process and transferring control to the operating system, allowing the system to start and operate.

- **Primary function**: The bootloader's main role is to load the OS kernel into memory and initiate its execution.
- **Stages**: Most bootloaders operate in multiple stages. In the first stage, a minimal program is loaded to locate and load the second stage, which in turn loads the OS kernel.
- **Common bootloaders**:
    - **GRUB (Grand Unified Bootloader)**: Commonly used in Linux distributions, GRUB is highly configurable and supports multiple OS installations.
    - **LILO (LInux LOader)**: An older bootloader used in Linux systems, which is now less common.
    - **Syslinux**: A lightweight bootloader for Linux, often used for live distributions or simple boot environments.
    - **Windows Boot Manager**: The default bootloader for Windows operating systems.
- **Multiboot support**: Bootloaders like GRUB allow users to choose between multiple operating systems during startup, providing a multiboot configuration.
- **Secure boot**: Some modern bootloaders, like those found in UEFI systems, support secure boot, a security feature that ensures only trusted software is loaded during startup.
- **Configuration files**: Bootloaders typically use configuration files to define boot options, such as the operating system to boot, kernel parameters, and boot options.

A bootloader is a crucial part of the system startup process, and its configuration and functionality can affect how the system behaves during boot, including booting from multiple operating systems, troubleshooting, or booting into recovery modes.

---

See also:

- [[Unified Extensible Firmware Interface (UEFI)]]
- [[Basic Input ⧸ Output System (BIOS)]]
- [[Secure boot]]