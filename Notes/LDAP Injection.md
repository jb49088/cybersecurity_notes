
# LDAP Injection

[[🏷️Injection attack]]

 - **Description:** Attackers inject malicious LDAP (Lightweight Directory Access Protocol) statements into queries.
- **Impact:** Can lead to unauthorized access to directory services, such as reading, modifying, or deleting directory entries.
- **Example:** `(&(uid=admin)(userPassword=*))`