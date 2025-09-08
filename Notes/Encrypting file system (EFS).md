
# Encrypting file system (EFS)

Encrypting file system (EFS) is a Windows feature that offers file-level encryption to secure sensitive data. As part of the NTFS (New Technology File System), EFS allows users to encrypt specific files and folders on their storage drives, ensuring that only authorized individuals can access the protected data.

EFS employs public key cryptography, generating a unique encryption key for each file and securing it with the user’s public key. This ensures that only the associated private key can decrypt the data. The system integrates seamlessly into the operating system, working in the background so users can access encrypted files without manual decryption after authentication. To prevent data loss, EFS provides recovery mechanisms, such as recovery agents, which can restore access if the user’s private key is lost.

This encryption method is particularly effective for safeguarding sensitive data on local drives or shared network locations. However, securely backing up encryption keys is critical to avoid irreversible data loss.

---

See also:

- [[Windows]]
- [[New technology file system (NTFS)]]
- [[Encryption]]
- [[Public key Infrastructure (PKI)]]
- [[Asymmetric encryption]]