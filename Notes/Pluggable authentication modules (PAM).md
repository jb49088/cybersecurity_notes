
# Pluggable authentication modules (PAM)

Pluggable authentication modules (PAM) provide a flexible authentication framework used in Unix-based operating systems to manage authentication mechanisms dynamically. PAM allows system administrators to configure authentication policies without modifying individual applications.

- **Modular authentication:** Uses **stackable modules** to define how authentication is handled for various services.
- **Centralized management:** Controls authentication for multiple applications, such as **SSH, sudo, and system logins**, through configuration files.
- **Multiple authentication methods:** Supports **passwords, biometrics, smart cards, and multi-factor authentication (MFA)**.
- **Customizable security policies:** Allows administrators to define rules for authentication, access control, and session management.
- **Configuration files:** Managed through `/etc/pam.d/` and `/etc/pam.conf`, where different authentication modules can be enabled or disabled.

PAM enhances security by allowing **authentication methods to be updated without changing applications**, making it a critical component of Linux and Unix-based security frameworks.

---

See also: