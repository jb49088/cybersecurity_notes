# Exclusive or (XOR)

Exclusive or (XOR) is a fundamental logical and bitwise operation that returns true only when its two inputs differ. In computing it operates on individual bits, outputting 1 when the compared bits are different and 0 when they are the same. Despite its simplicity, XOR is one of the most widely used operations in cryptography, encoding, and low-level programming.

- **Truth table:** XOR follows a straightforward rule: 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, and 1 XOR 1 = 0. The output is 1 only when the inputs are different, hence the name exclusive or.
- **Self-inverse property:** One of XOR's most useful properties is that applying it twice with the same key returns the original value. If A XOR B = C, then C XOR B = A. This makes XOR naturally suited for reversible operations like encryption and decryption using the same key.
- **Use in cryptography:** XOR is a core building block in many cryptographic algorithms and stream ciphers, where a plaintext byte is XORed against a keystream byte to produce ciphertext. The same operation with the same key reverses the process, making it an elegant and computationally cheap method of encryption.
- **XOR cipher weaknesses:** A simple XOR cipher using a short or repeating key is cryptographically weak and can be broken through frequency analysis or known plaintext attacks. If an attacker knows or can guess part of the plaintext, they can recover portions of the key by XORing the known plaintext against the ciphertext.
- **Use in malware and obfuscation:** XOR encoding is commonly used by malware authors to obfuscate payloads, strings, and shellcode, as it is simple to implement and can evade basic signature-based detection. Single-byte XOR obfuscation in particular is trivially reversible and frequently encountered in malware analysis and CTF challenges.
- **Checksums and error detection:** XOR is used in checksum calculations and error detection schemes such as CRC, where XORing blocks of data together produces a value that can verify data integrity.

XOR is a deceptively simple operation that appears throughout cryptography, malware analysis, and low-level security work. Recognizing XOR obfuscation and understanding its self-inverse property are practical skills that come up regularly in CTF challenges, reverse engineering, and vulnerability research.

---

See also:

- [[Encoding]]
- [[Stream cipher]]
- [[Cryptography]]
- [[Obfuscation]]
