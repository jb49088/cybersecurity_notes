
# Just-in-time permissions

Just-in-time permissions are a security strategy that grants users elevated access rights only for a limited time. This approach reduces the risks associated with persistent administrative privileges, aligning with the principle of least privilege and narrowing the scope of potential security breaches.

- **Limit permanent administrator rights:** In many organizations, IT teams often have elevated rights like administrator or root access. These accounts are high-value targets for attackers. Just-in-time permissions eliminate the need for permanent elevated access.
- **Grant admin access temporarily:** Users receive administrator rights only for the duration required to complete a task, reducing unnecessary exposure to high-risk privileges.
- **Scope of breaches is minimized:** Since accounts with just-in-time permissions don't retain permanent elevated rights, even if an account is compromised, its access is limited, reducing the potential damage.
- **Centralized request system:** Users request access through a central clearinghouse, which approves or denies access based on predefined security policies and organizational rules.
- **Password vaulting:** Primary credentials are stored in a secure password vault. The vault manages access to these credentials, ensuring that they are only released under strict conditions.
- **Temporary accounts and credentials:** Just-in-time permissions often involve creating time-limited accounts with ephemeral credentials. These credentials are used for one session and are deleted immediately after use, ensuring that primary passwords are never exposed.

Just-in-time permissions enhance security by minimizing the duration and scope of elevated access, ensuring that critical systems are less vulnerable to misuse or attack.

---

See also:

- [[Least privilege]]