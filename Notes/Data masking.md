
# Data masking

[[🏷️Obfuscation]]

Data masking is a technique used to protect sensitive information by replacing it with fictitious but realistic data. The goal is to ensure that sensitive data is not exposed to unauthorized users while maintaining the usability of the data for testing, training, or analysis purposes. Data masking is widely employed in industries like healthcare, finance, and software development to ensure compliance with privacy regulations and secure data handling.

## Techniques used in data masking

- **Static Data Masking**: Sensitive data is replaced with masked values in a non-production environment. The original data remains untouched in the production database.
- **Dynamic Data Masking**: Sensitive data is masked in real time, displaying altered data to unauthorized users while keeping the original data accessible to authorized users.
- **Tokenization**: Original data is replaced with tokens, which can only be mapped back to the real data using a secure system.
- **Character Shuffling and Substitution**: Data values are rearranged or substituted with random characters, retaining the original data's structure but obfuscating the content.
- **Nulling or Blank Out**: Certain data fields are replaced with null values or blanks to prevent unauthorized access.

Data masking ensures that sensitive information, such as social security numbers, credit card numbers, or personal health information, is not exposed in environments where it is not required. This approach is particularly important for compliance with laws such as GDPR, HIPAA, and PCI-DSS.

---

See also:

- [[Tokenization]]
- [[Obfuscation]]
- [[Steganography]]
- [[Anonymization]]