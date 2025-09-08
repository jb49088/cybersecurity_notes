
# Cyclical redundancy check (CRC)

Cyclical redundancy check (CRC) is an error-detection technique used to ensure the integrity of data during transmission or storage. It works by generating a checksum value based on the data being sent, which the receiver uses to verify the data's accuracy.

- **Error detection:** CRC identifies errors that may occur during data transmission or storage, such as bit flips or corruption.
- **Checksum generation:** A mathematical algorithm is applied to the data to produce a unique checksum, which is transmitted alongside the data.
- **Verification process:** The receiver recalculates the checksum from the received data and compares it to the transmitted checksum to verify integrity.
- **Efficiency:** CRC is lightweight and fast, making it ideal for applications like networking, storage devices, and digital communication.
- **Limitations:** While CRC is effective at detecting most errors, it cannot correct them or detect errors if specific patterns occur.

CRC is widely used in network protocols, file systems, and error-checking systems to maintain reliable and accurate data communication.

---

See also:

- [[Integrity]]
- [[Checksum]]