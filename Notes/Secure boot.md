
# Secure boot

Secure boot is a security feature that ensures a device boots using only trusted software. It helps protect against bootkit and rootkit attacks by validating the bootloader and operating system (OS) during startup. If the system firmware (UEFI) detects any unsigned or unauthorized code, the boot process is halted to prevent malicious software from running.

Secure boot works by checking the digital signatures of bootloaders and other critical software against a list of trusted certificates stored in the firmware. If the signatures are valid, the system continues to boot; otherwise, it prevents the system from starting.

Primarily used in modern UEFI-based systems, secure boot adds an essential layer of security, ensuring that only verified software is executed during startup, protecting the system from early-stage attacks.

---

See also:

- [[Bootloader]]
- [[Unified Extensible Firmware Interface (UEFI)]]
- [[Operating system (OS)]]
- [[Bootkit]]
- [[Rootkit]]