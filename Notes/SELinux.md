
# SELinux

Security-Enhanced Linux (SELinux) is a security architecture integrated into the Linux operating system, designed to provide enhanced access control and system security. It was developed by the National Security Agency (NSA) and is implemented as a set of kernel-level security patches.

Key aspects of SELinux:

- **Security patches for the Linux kernel:** SELinux adds mandatory access control (MAC) to the Linux kernel, enhancing its security features.
- **Mandatory access control (MAC):** Unlike Linux's traditional discretionary access control (DAC), where users can control access to their files, MAC enforces strict security policies determined by the system administrator, limiting how processes and users can interact with each other.
- **Limits application access:** SELinux operates on the principle of least privilege, ensuring that applications and users have the minimum access necessary to perform their tasks. This reduces the risk of damage or exploitation in the event of a breach.
- **Least privilege:** By enforcing strict policies on application and process behavior, SELinux ensures that the potential scope of a breach is minimized. Even if an attacker gains access to one process or application, their ability to exploit the system is limited.
- **Open source:** SELinux is open-source software, and it is included as an option with many Linux distributions, such as Red Hat Enterprise Linux (RHEL), Fedora, and CentOS. This ensures that it is accessible and customizable for different use cases.

SELinux is a powerful tool for enhancing the security of Linux systems, helping protect against both external attacks and internal threats by controlling how processes interact with one another.

---

See also:

- [[Linux]]
- [[Mandatory access control (MAC)]]
- [[Discretionary access control (DAC)]]