# CyberChef

CyberChef is a web-based data analysis and transformation tool developed by GCHQ, the UK's signals intelligence agency. It provides a visual interface for applying a wide variety of encoding, decoding, encryption, hashing, and data manipulation operations, making it an indispensable utility for security professionals, CTF players, and bug bounty hunters who frequently need to process and transform data quickly.

- **Recipe-based workflow:** CyberChef operates on the concept of recipes, where individual operations are chained together in sequence to transform an input into a desired output. This makes it easy to apply multiple transformations in a single workflow, such as base64 decoding followed by URL decoding followed by JSON formatting.
- **Magic operation:** CyberChef includes a Magic operation that attempts to automatically detect the encoding or format of an input and suggest or apply the appropriate transformations. This is particularly useful when encountering an unknown string during a bug bounty engagement where the encoding is not immediately obvious.
- **Encoding and decoding:** CyberChef supports a comprehensive range of encoding schemes including base64, base32, base16, URL encoding, HTML encoding, and more, making it the go-to tool for quickly decoding suspicious strings encountered during reconnaissance and enumeration.
- **Hashing and cryptography:** CyberChef can generate and compare cryptographic hashes, apply symmetric encryption and decryption operations, and work with XOR ciphers, making it useful for both analyzing captured data and verifying cryptographic implementations.
- **File and binary analysis:** CyberChef can process raw binary data, extract files from hex dumps, analyze byte patterns, and perform operations on file contents, making it a lightweight companion tool for basic malware analysis and forensics work.
- **Offline availability:** CyberChef can be downloaded and run entirely offline in a browser, which is important in professional engagements where sensitive data should not be submitted to external online services.
- **CTF and bug bounty use:** CyberChef is a staple tool in CTF challenges and bug bounty hunting for quickly identifying and reversing encoding schemes, decoding tokens and cookies, and processing data found in HTTP responses, configuration files, and application source code.

CyberChef's combination of breadth, accessibility, and chainable operations makes it one of the most practical and frequently reached for tools in offensive security work, capable of turning an unfamiliar blob of encoded data into actionable information within seconds.

---

See also:

- [[encoding]]
- [[encryption]]
- [[base16]]
- [[base64]]
- [[exclusive_or_(xor)]]
- [[reconnaissance]]
- [[web_application]]
