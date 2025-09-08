
# Input validation

Input validation is a critical process in ensuring that user-supplied data is correct, secure, and in the expected format. It helps protect applications from harmful or unintended data, reducing the risk of security vulnerabilities such as injection attacks or data corruption. By verifying and sanitizing inputs, developers can improve the overall integrity and security of their systems.

Key steps in input validation:

- **What is the expected input?**: Clearly define the types of input that are expected in each case. For example, if an input field expects a numeric value, the validation process should check that only numbers are entered. Comparing the actual input to the expected input helps ensure data accuracy.
- **Document all input methods**: Record all ways through which data can be input, such as forms, fields, or other entry points. Each input method should have clear documentation, including the types of data expected, required formats, and any constraints.
- **Check and correct all input (normalization)**: Input should be checked for correctness and normalized to ensure consistency. This includes formatting issues, such as ensuring a zip code is entered with the correct number of characters or properly formatted phone numbers. If needed, the system should automatically fix minor mistakes in input format.
- **Fuzzers will find what you missed**: Automated fuzz testing tools are designed to input random or unexpected data into an application to test how it handles edge cases or unusual inputs. These tools help uncover vulnerabilities that may not have been considered during manual testing. It's essential to harden your application to prevent fuzzers from exploiting weak spots.
    
Effective input validation is vital for preventing many common security issues. It protects against malicious data input and ensures that applications behave predictably and securely, even when faced with unexpected user inputs.

---

See also:

- [[Input sanitization]]
- [[Injection attack]]