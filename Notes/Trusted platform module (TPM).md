
# Trusted platform module (TPM)

[[🏷️Security hardware]]

A trusted platform module (TPM) is a specialized security chip embedded in computers and other devices that provides hardware-based protection for sensitive information. TPMs are designed to securely store cryptographic keys, passwords, and other critical data, protecting it from tampering, theft, or unauthorized access.

Key features of a TPM include:

- **Secure Storage:** TPMs store sensitive information such as encryption keys, certificates, and passwords in a secure, tamper-resistant environment, making it nearly impossible for attackers to extract or manipulate the data.
- **Platform Integrity:** TPMs can measure the integrity of the system by validating the firmware, boot process, and operating system during startup. This ensures that only trusted software is running on the device, protecting it from rootkits and other malicious software.
- **Cryptographic Operations:** TPMs can perform cryptographic operations such as key generation, encryption, and digital signing directly within the hardware, providing a higher level of security than software-based solutions.
- **Sealing and Binding:** TPMs can bind data to specific hardware, preventing it from being decrypted on unauthorized systems. This ensures that sensitive data can only be accessed when the device is in a trusted state.

TPMs are widely used in applications like disk encryption (e.g., BitLocker), secure boot, and digital rights management (DRM). By providing hardware-based security, TPMs ensure that data is protected even in the event of a system compromise.

---

See also:

- [[Encryption]]
- [[Secure enclave]]
- [[Hardware Security Module (HSM)]]
- [[Secure boot]]