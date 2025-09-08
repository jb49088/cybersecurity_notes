
# Redundant array of independent disks (RAID)

Redundant array of independent disks (RAID) is a data storage technology that combines multiple physical disk drives into a single logical unit to improve performance, redundancy, and/or capacity. RAID uses various techniques like data striping, mirroring, and parity to enhance data availability, fault tolerance, and overall storage efficiency.

RAID is commonly used in servers, workstations, and enterprise storage systems to protect data from drive failures and improve system reliability.

- **RAID 0 (Striping):** Distributes data across multiple disks for improved speed but offers no redundancy. A failure of one disk results in complete data loss.
- **RAID 1 (Mirroring):** Duplicates data across two or more disks for fault tolerance. If one disk fails, the system continues running with the remaining copies.
- **RAID 5 (Striping with Parity):** Uses striping along with parity data to allow recovery if a single disk fails. Requires at least three disks.
- **RAID 6 (Striping with Double Parity):** Similar to RAID 5 but can tolerate two disk failures instead of one. Requires at least four disks.
- **RAID 10 (RAID 1+0):** Combines mirroring and striping for both performance and redundancy. Requires at least four disks.

RAID levels vary in terms of performance, redundancy, and storage efficiency, allowing organizations to choose the best configuration for their needs.

---

See also: