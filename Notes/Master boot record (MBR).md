
# Master boot record (MBR)

The master boot record (MBR) is a special type of boot sector located at the beginning of a storage device, such as a hard drive. It contains the necessary information for the system to boot the operating system (OS) and manage the partitions on the drive. The MBR is crucial for initiating the boot process of legacy systems that use BIOS firmware.

The MBR has two main components:

1. **Bootloader**: A small program that tells the computer how to load the operating system. It is responsible for loading the OS from the active partition.
2. **Partition Table**: A record of the partitions on the disk, detailing where each partition begins and ends, allowing the system to properly access data stored on the drive.

While the MBR was once the standard for booting systems, it has limitations, particularly with disk size and the number of partitions. This led to the adoption of the GUID Partition Table (GPT) in newer systems, which supports larger disk sizes and more partitions.

Despite its limitations, the MBR is still used in many older systems and is critical for understanding how the boot process works on these devices.

---

See also:

- [[Basic Input ⧸ Output System (BIOS)]]
- [[Unified Extensible Firmware Interface (UEFI)]]
- [[Bootloader]]
- [[Operating system (OS)]]

