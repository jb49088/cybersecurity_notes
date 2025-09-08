
# Snapshot

A snapshot is a backup technique that has gained popularity, particularly in virtual machine (VM) environments, and is highly useful in cloud environments. It allows for the capture of an instant backup of an entire system, preserving its current configuration and data at a specific moment in time. This process provides an efficient way to safeguard the system and its settings without the need for a full backup.

Once a snapshot is taken, it captures the entire state of the system. After 24 hours, another snapshot can be taken, which will only contain the changes made since the previous snapshot. By taking regular snapshots, such as daily, you can create a series of restore points that allow for quick recovery in the event of a problem. Reverting to any previous snapshot can be done swiftly, making it an effective tool for fast system recovery. Snapshots can be restored almost instantly, making the process of recovering from errors or failures much faster compared to traditional full backups.

This ability to roll back to previous system states while maintaining the integrity of data makes snapshots especially valuable for managing systems in dynamic, cloud-based environments.

---

See also:

- [[Backup]]
- [[Virtual machine (VM)]]
- [[Virtualization]]