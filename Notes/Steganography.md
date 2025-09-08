
# Steganography

[[🏷️Obfuscation]]

Steganography is the practice of concealing messages or information within other, seemingly innocuous data. Unlike encryption, which scrambles data to make it unreadable without a key, steganography focuses on hiding the existence of the message itself. This technique is used for both legitimate purposes, like watermarking, and malicious purposes, such as evading detection in cyberattacks.

## Common applications of steganography

- **Network-based Steganography**: Messages or data can be embedded within network protocols, such as TCP packets, without disrupting normal communication. This method can be used to covertly exfiltrate information or establish hidden channels.
- **Multimedia Steganography**: Images, audio files, and videos are popular mediums for hiding information. For example:
    - **Images**: Data can be embedded into the least significant bits (LSB) of pixel values.
    - **Audio**: Subtle modifications to frequencies or timing can encode hidden data.
    - **Videos**: Information can be hidden in specific frames or within the audio tracks of a video file.
- **Invisible Watermarks**: Steganography is used in printers and digital content for watermarking, ensuring authenticity and preventing counterfeiting. For instance, some printers embed microscopic dots in printed documents that contain identifying information about the printer and date of printing.

Steganography is a powerful tool for discreet communication and copyright protection. However, it is also exploited in cybersecurity by threat actors to hide malware, exfiltrate sensitive data, or bypass detection systems.

---

See also:

- [[Encryption]]
- [[Obfuscation]]
- [[Tokenization]]
- [[Data masking]]