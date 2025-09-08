
# X.500

X.500 is a set of standards defined by the International Telecommunication Union (ITU) for directory services. It establishes a framework for organizing and accessing directory information using a hierarchical structure.

- **Attribute-value pairs:** Data in X.500 directories is stored as attribute-value pairs, where each attribute has a specific value. The most specific attribute is listed first.
- **Hierarchical structure:** The directory is organized in a tree-like structure, allowing for easy categorization and retrieval of data.
- **Container objects:** These are used to group related information, such as country, organization, or organizational units.
- **Leaf objects:** These represent individual entries like users, computers, printers, and files at the endpoints of the directory tree.

This table describes the distinguished names used in X.500 directory services for identifying individuals, organizations, and locations.

![[Table 1.11]]

This diagram illustrates the hierarchical structure of an X.500 directory, showing how different components are organized.

![[Diagram 1.14]]

X.500 serves as the foundation for various directory service protocols, including LDAP, and helps in managing large-scale directory information.

---

See also:

- [[Lightweight directory access protocol (LDAP)]]
- [[Active directory (AD)]]