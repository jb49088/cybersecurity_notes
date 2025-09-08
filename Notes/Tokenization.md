
# Tokenization

[[🏷️Obfuscation]]

Tokenization is a security technique used to protect sensitive data by replacing it with a unique identifier, known as a "token." These tokens are used in place of the actual data, such as credit card numbers or personal identification information, within a system. The original sensitive data is stored securely in a separate database, known as a token vault, while the token itself has no exploitable value.

![[Image 2.57.png]]

Unlike encryption, tokenization does not require complex mathematical operations to protect data; instead, it relies on a one-to-one mapping between the sensitive data and the token. This makes tokenization an effective way to minimize the exposure of sensitive information, especially in environments where compliance with privacy regulations (e.g., PCI DSS for payment card data) is required.

Tokenization is commonly used in payment processing, healthcare, and financial services to protect personally identifiable information (PII) and reduce the risk of data breaches.

---

See also:

- [[Obfuscation]]
- [[Steganography]]
- [[Data masking]]
- [[Payment Card Industry Data Security Standard (PCI DSS)]]
- [[Personally identifiable information (PII)]]
