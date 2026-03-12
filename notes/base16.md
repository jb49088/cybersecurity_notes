# Base16

Base16 is an encoding scheme that represents binary data as a string of hexadecimal characters, using the sixteen symbols 0-9 and A-F to encode each byte of data as exactly two characters. It is more commonly referred to as hex encoding and is one of the most frequently encountered representations in computing, networking, and security contexts.

- **How it works:** Each byte of input data has a value between 0 and 255, which maps exactly to a two-character hexadecimal value between 00 and FF. Because each character represents four bits, two characters are always required to represent a full byte, meaning base16 output is always exactly twice the length of the original input in bytes.
- **Identifying base16:** Base16 encoded strings consist exclusively of the characters 0-9 and A-F, are always an even number of characters in length, and are case insensitive, meaning lowercase a-f is equally valid. Unlike base64, base16 strings never contain symbols or padding characters, making them relatively straightforward to identify.
- **Common uses:** Base16 is widely used to represent cryptographic hashes such as MD5, SHA-1, and SHA-256, color values in web development, memory addresses in debugging and reverse engineering, raw packet data in network analysis tools like Wireshark, and byte sequences in malware analysis.
- **Color encoding:** In web development and image processing, colors are commonly expressed as base16 values representing the intensity of red, green, and blue channels. For example #FF5733 encodes three bytes where FF is full red intensity, 57 is the green value, and 33 is the blue value.
- **Security testing:** In bug bounty hunting and penetration testing, base16 encoded strings are frequently encountered in cookies, tokens, file hashes, and application parameters. Recognizing and decoding them can reveal underlying values that aid in further testing, such as identifying hash types for cracking or uncovering obfuscated identifiers.
- **Decoding:** Base16 can be decoded using command-line tools such as `echo "4a4b4c" | xxd -r -p` on Linux, CyberChef, or Python's built-in bytes.fromhex() method.

Base16 is one of the most universally encountered encodings in technical security work, appearing everywhere from hash outputs and network captures to color values and memory dumps, making it an essential encoding scheme to recognize and work with fluently.

---

See also:

- [[encoding]]
- [[base64]]
- [[wireshark]]
