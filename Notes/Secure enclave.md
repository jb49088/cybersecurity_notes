
# Secure enclave

[[🏷️Security hardware]]

A secure enclave is a dedicated security processor built into systems to provide a protected environment for sensitive data and operations. It acts as a highly secure area within a device’s main processor, offering features that enhance security and protect against unauthorized access or tampering.

The Secure Enclave provides several key security features:

- **System Monitoring:** It continuously monitors the system to detect any irregular or malicious activity, ensuring that security processes are not compromised.
- **True Random Number Generator (TRNG):** Secure Enclaves often include a hardware-based TRNG to generate unpredictable, high-quality random numbers used in cryptographic operations, improving the security of encryption keys and algorithms.
- **Real-Time Encryption:** Secure Enclaves perform real-time encryption and decryption operations, ensuring that sensitive data is always protected, even while being used or processed.
- **Root Cryptographic Keys:** These systems securely store root cryptographic keys, which are used to authenticate and encrypt communication within the device, ensuring that only authorized entities can access or modify data.

By isolating sensitive data and cryptographic operations from the rest of the system, Secure Enclaves help protect against attacks that could compromise the device or its data. They are commonly used in mobile devices, payment systems, and hardware-based security solutions.

---

See also:

- [[Encryption]]
- [[Hardware Security Module (HSM)]]
- [[Trusted platform module (TPM)]]