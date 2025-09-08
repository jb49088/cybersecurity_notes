
# Backup

Creating backups is an incredibly important process designed to ensure that important and valuable data can be recovered in the event of a disaster. A solid backup strategy is essential for minimizing data loss and ensuring business continuity. The implementation of backups can vary depending on several factors, including the total amount of data, the type of backup, the backup media used, storage location, and the backup and recovery software. Planning the frequency of backups is also key, whether it's done on a daily, weekly, or even hourly basis.

Onsite backups are stored within the same location as the primary data, which eliminates the need for an Internet link. Data can be accessed immediately, and these backups are typically less expensive. However, onsite backups are vulnerable in the event of a local disaster such as a fire or flood. Offsite backups, on the other hand, are transferred over the Internet or a WAN link and stored in a different location. This makes them essential for disaster recovery, as the data can be accessed and restored from anywhere after an incident. Many organizations use both onsite and offsite backups to ensure they have multiple copies of their data, increasing the options available during restoration.

The frequency of backups is crucial to the effectiveness of the backup strategy. Organizations must decide how often backups should occur—whether it’s daily, weekly, or on an hourly basis. Different systems may require different backup frequencies based on how often data changes. Some systems may not change much on a daily basis, while others may require more frequent backups. Multiple backup sets (e.g., daily, weekly, and monthly) may be needed to ensure comprehensive coverage, which requires significant planning and media management.

Backup data, especially when stored offsite, often contains a history of sensitive information. This makes it an attractive target for attackers. Protecting backup data with encryption ensures that everything on the backup media is unreadable without the recovery key. This is especially important for cloud backups, where data may be transferred across the internet or stored in third-party data centers. By encrypting backup data, organizations prevent unauthorized access and safeguard sensitive information, even if the backup media is compromised.

---

See also:

- [[Snapshot]]
- [[Replication]]
- [[Journaling]]
- [[High availability (HA)]]