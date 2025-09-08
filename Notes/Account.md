
# Account

Claiming an identity and being authorized to access a system or service requires an account. Accounts contain the information about a user, including things like rights and permissions that are associated with the account.

## Account Types 

There are many types of accounts, and they can almost all be described
as one of a few basic account types:

- **User accounts**, which can run the gamut from basic access to systems, devices, or applications to power users with broad rights and privileges. A common example of a user account is a Windows Standard User account, which relies on User Account Control and an administrator password to be entered when installing applications, editing the Registry, or other privileged actions.
- **Privileged or administrative accounts**, like the root account or members of the wheel group on Linux and Unix systems, and the Windows default Administrator account.
- **Shared and generic accounts or credentials**, which are often prohibited by security policies. Although shared accounts can be useful, many organizations build delegation capabilities to allow multiple users to act in the same way or with the same rights to avoid shared account issues such as the inability to determine who was logged into the shared account or what actions each user who shares the account took.
- **Guest accounts**, which are provided to temporary users and which typically have very limited privileges, but are also likely to have far less information about the user who uses them, if any.
- **Service accounts** associated with applications and services. Service accounts should not be used for interactive logins, and many organizations have specific security policies in place to ensure service account security.
