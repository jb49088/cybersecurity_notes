
# Code signing

Code signing is the process of digitally signing an application or software code to verify its authenticity and integrity before it is deployed. This ensures that users can trust the application they are running and that it has not been tampered with during deployment.

When an application is deployed, users run the executable or scripts. However, several security questions arise: Has the application been modified in any way? Can you confirm that the application was written by a specific developer?

To address these concerns, the developer can digitally sign the application code. This involves using asymmetric encryption, where a trusted Certificate Authority (CA) signs the developer’s public key. The developer then signs the code with their private key, allowing users to verify that the code is both authentic and unaltered. For internal applications, organizations can use their own CA to sign the code.

---

See also:

- [[Asymmetric encryption]]
- [[Certificate authority (CA)]]
- [[Digital signature]]
- [[Digital certificate]]