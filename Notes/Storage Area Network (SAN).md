
# Storage Area Network (SAN)

[[🏷️Network type]]

A storage area network (SAN) is designed to do exactly what it says, which is to store information. Although a SAN can be implemented a few different ways, imagine a network (or network segment) that holds nothing but networked storage devices, whether they be network- attached storage (NAS) hard drives or servers with lots of disk space dedicated solely to storage. This network won’t have client computers or other types of servers on it. It’s for storage only. Image 2.22 shows what a SAN could look like.

![[Image 2.22.png|center]]

Perhaps you’re thinking, why would someone create a network solely for storage? It’s a great question, and there are several benefits to having a SAN.

- **Dedicated SANs relieve network loads:** With a SAN, all storage traffic, which may include huge data files or videos, is sent to a specific network or network segment, relieving traffic on other network segments.
  <br>
- **SANs offer fast data access:** Most SANs use high-speed Fibre Channel connections, which allow for very fast access even for huge files.
  <br>
- **SANs are easily expandable:** In most cases, it’s a matter of connecting a new storage unit, which might even be hot- swappable (removed and replaced without powering down the system), and a few clicks to configure it. Then it’s ready to go.
  <br>
- **Block-level storage is more efficient:** This is getting into the weeds a bit, but most SANs are configured to store and retrieve data in a system called block storage. This contrasts with the file- based access systems you’re probably used to, such as the ones in Windows and macOS. For anyone who has used a Windows- based or Mac computer, file storage is instantly recognizable. It’s based on the concept of a filing cabinet. Inside the filing cabinet are folders, and files are stored within the folders. Each file has a unique name when you include the folders and subfolders it’s stored in. For example, c:\files\doc1.txt is different from c:\papers\doc1.txt. The hierarchical folder structure and the naming scheme of file storage make it relatively easy for humans to navigate. Larger data sets and multiple embedded folders can make it trickier—who here hasn’t spent 10 minutes trying to figure out which folder they put that file in?—but it’s still pretty straightforward. 

With file storage, each file is treated as its own singular entity, regardless of how small or large it is. With block storage, files are split into chunks of data of equal size, assigned a unique identifier, and then stored on the hard drive. Because each piece of data has a unique address, a file structure is not needed. Image 2.23 illustrates what this looks like.

![[Image 2.23.png|center]]

Block storage allows a file to be broken into more manageable chunks rather than being stored as one entity. This allows the operating system to modify one portion of a file without needing to open the entire file. In addition, since data reads and writes are always of the same block size, data transfers are more efficient and therefore faster. Latency with block storage is lower than with other types of storage.

One of the first common use cases for block storage was for databases, and it remains the best choice for large, structured databases today. Block storage is also used for storage area networks (SANs). 

The downsides to SANs are that they are a bit complicated to set up and can be more expensive to run than non- SAN storage solutions. For huge networks that need to get data to large numbers of users, though, they’re a good choice.



