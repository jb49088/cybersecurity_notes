
# Message integrity code (MIC)

A message integrity code (MIC) is a security mechanism used to ensure that data transmitted over a network has not been altered or tampered with during transmission. It provides a way to verify the integrity of the message by generating a checksum, which is appended to the message before it is sent. The recipient can then use the same algorithm to calculate a checksum on the received message and compare it with the MIC to confirm that the data has not been modified.

MICs are commonly used in communication protocols to prevent malicious actors from modifying data in transit, ensuring that the message received is exactly what was sent. They are an important part of cryptographic systems, where data integrity and authenticity are critical.

While MICs help protect against tampering, they do not provide confidentiality. To secure the content of a message, encryption must also be applied. The combination of encryption and MIC helps ensure both the privacy and integrity of the data being transmitted.

---

See also:

- [[Integrity]]
- [[Hashing]]
- [[Checksum]]