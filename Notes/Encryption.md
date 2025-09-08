
# Encryption

[[🏷️Cryptography]] [[🏷️Obfuscation]]

Encryption is the process of converting data into a coded form to prevent unauthorized access, ensuring data confidentiality and integrity. There are various types of encryption that protect data at different levels of a system, each offering unique benefits based on the security needs.

## Types of encryption

- **Full Disk Encryption (FDE):** Full disk encryption protects the entire disk, including the operating system, applications, and user files. It ensures that all data on the drive is encrypted, offering robust protection, especially in case of device theft or loss.
- **Partition Encryption:** This encryption secures specific sections or partitions of a storage device. Unlike FDE, partition encryption allows for more granular control by encrypting only selected partitions where sensitive data resides.
- **File Encryption:** File encryption secures individual files by converting them into unreadable formats using an encryption key. This method ensures that only authorized users with the decryption key can access the file, offering targeted protection for specific data.
- **Volume Encryption:** Volume encryption works on logical volumes or virtual disks, encrypting all data within a particular volume. It provides security at the volume level while maintaining flexibility for managing encrypted data in virtualized or partitioned environments.
- **Database Encryption:** Database encryption secures data stored within databases, ensuring sensitive information like financial records and personal details is protected. This encryption can be applied to individual fields, tables, or the entire database, depending on the level of protection needed.
- **Record Encryption:** Record encryption secures specific records within a database or data structure. Unlike database-level encryption, it focuses on encrypting only selected records, such as credit card numbers or personally identifiable information (PII), offering a selective and efficient approach to data protection.

Each of these encryption methods plays a vital role in safeguarding data across different levels, from entire drives to individual records, ensuring confidentiality and minimizing the risks of unauthorized access.

---

See also:

- [[Plaintext]]
- [[Ciphertext]]
- [[Algorithm]]
- [[Confidentiality]]
- [[Advanced encryption standard (AES)]]
