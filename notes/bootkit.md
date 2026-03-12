# Bootkit

A bootkit is a type of malicious software designed to infect the boot process of a computer, typically targeting the master boot record (MBR) or UEFI firmware. It allows an attacker to gain control of a system before the operating system (OS) starts, giving them the ability to bypass traditional security measures like antivirus programs and firewalls.

Bootkits operate by modifying or replacing the bootloader, which is responsible for loading the OS. Once installed, they can hide themselves from the OS, making detection difficult. Bootkits can enable attackers to execute arbitrary code with high-level privileges, steal sensitive information, or even create persistent backdoors on the infected system.

Because bootkits work outside the OS, they are especially dangerous and challenging to remove. They often require specialized tools or techniques, such as re-flashing the firmware or wiping the hard drive, to fully eradicate.

---

See also:

- [[malware]]
- [[master_boot_record_(mbr)]]
- [[unified_extensible_firmware_interface_(uefi)]]
- [[operating_system_(os)]]
- [[rootkit]]
- [[secure_boot]]
