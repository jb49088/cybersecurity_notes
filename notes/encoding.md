# Encoding

Encoding is the process of converting data from one format or representation into another using a defined scheme or standard. Unlike encryption, encoding is not designed to protect data and requires no secret key to reverse. Its purpose is to ensure data is compatible with a particular system, protocol, or medium, and can always be decoded by anyone who knows the scheme used.

- **ASCII:** One of the earliest and most fundamental encoding standards, ASCII maps 128 characters including letters, digits, and control characters to numeric values between 0 and 127. It forms the foundation of most modern text encoding systems and is still widely encountered in computing and networking contexts.
- **Unicode and UTF-8:** Unicode is a universal encoding standard designed to represent characters from every language and symbol system in the world. UTF-8 is the most common implementation, encoding characters as one to four bytes and maintaining backward compatibility with ASCII. It is the dominant encoding standard for web content and modern applications.
- **URL encoding:** Also known as percent encoding, URL encoding replaces characters that are not safe for use in URLs with a percent sign followed by their hexadecimal value, for example a space becomes %20. In security testing, URL encoding and double URL encoding are commonly used to bypass input filters and web application firewalls.
- **HTML encoding:** HTML encoding replaces special characters with their HTML entity equivalents, such as replacing < with &lt;, to prevent them from being interpreted as markup. Improper or inconsistent HTML encoding is a common factor in cross-site scripting vulnerabilities.
- **Base64:** A widely used encoding scheme that converts binary data into a string of printable ASCII characters, commonly used for transmitting data in text-based formats and frequently encountered in credentials, tokens, and configuration files.
- **Hex encoding:** Represents data as hexadecimal values, with each byte expressed as two hex digits. Hex encoding is commonly seen in color codes, memory addresses, cryptographic hashes, and raw packet data.
- **Pixel and image encoding:** Colors in digital images are typically encoded as numeric values representing the intensity of red, green, and blue channels, most commonly as three bytes per pixel giving values from 0 to 255 per channel. This RGB encoding underpins most digital image formats and is relevant in security contexts such as steganography, where data is hidden within image pixel values.

Encoding is encountered constantly in security testing across web requests, file formats, network traffic, and application data. Recognizing different encoding schemes and knowing how to decode them is a fundamental skill for identifying hidden information and bypassing input validation controls.

---

See also:

- [[base64]]
- [[cross-site_scripting_(xss)]]
- [[steganography]]
