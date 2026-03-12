# Base64

Base64 is an encoding scheme that converts binary data into a string of ASCII characters, making it safe to transmit or store data in environments that only support text. It is important to understand that base64 is encoding, not encryption, meaning it provides no confidentiality and can be instantly decoded by anyone without a key or password.

- **How it works:** Base64 represents binary data by mapping every three bytes of input into four printable ASCII characters drawn from a set of 64 characters consisting of A-Z, a-z, 0-9, and the symbols + and /. Padding characters (=) are appended to the end of the output when the input length is not divisible by three.
- **Identifying base64:** Base64 encoded strings have several recognizable characteristics that make them relatively easy to spot. They consist entirely of alphanumeric characters along with + and /, are often padded with one or two = characters at the end, and tend to appear as long unbroken strings of seemingly random characters. The length of a base64 string is always a multiple of four.
- **Common locations:** Base64 is frequently encountered in HTTP headers, cookies, JSON web tokens, API responses, HTML source code, and configuration files. In bug bounty hunting it is worth decoding any suspicious-looking strings found in these locations as they often reveal sensitive information.
- **Passwords and credentials:** Developers sometimes store or transmit passwords, API keys, and other credentials encoded in base64 under the mistaken belief that encoding provides security. Encoded credentials are regularly discovered in source code, configuration files, environment variables, and HTTP Basic Authentication headers, where credentials are passed as a base64-encoded username and password pair.
- **Chaining with other findings:** Decoded base64 strings frequently contain further encoded or encrypted data, credentials, internal URLs, or serialized objects, making decoding a valuable step when investigating findings during a bug bounty engagement.
- **Decoding:** Base64 can be decoded instantly using command-line tools such as `echo "string" | base64 -d` on Linux, online decoders, or tools like CyberChef, which is widely used in security testing for chaining multiple encoding and decoding operations together.

Base64 is one of the first things to check when encountering an unfamiliar or suspicious string during reconnaissance and enumeration, as it is extremely common and frequently conceals information that is directly useful in an assessment.

---

See also:

- [[encoding]]
- [[base16]]
- [[reconnaissance]]
