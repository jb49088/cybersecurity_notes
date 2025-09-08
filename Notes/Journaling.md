
# Journaling

Journaling is a technique used to prevent data corruption in case of unexpected power loss or system crashes while writing data to storage. When power is lost during a write operation, the stored data is often left in a corrupted state, making recovery a complicated process. This typically requires removing corrupted files and restoring the data from a backup.

To mitigate this risk, journaling involves creating a journal entry before data is written to storage. The journal records the data changes, ensuring that if a failure occurs, the system can refer to the journal to determine which data was in the process of being written. Once the journal entry is made, the data is written to storage. After the data is successfully stored, the journal entry is updated and cleared, preparing it for the next set of changes. This process provides a safeguard against incomplete or corrupted writes, ensuring a more reliable recovery process.

---

See also:

- [[Backup]]
- [[Integrity]]
