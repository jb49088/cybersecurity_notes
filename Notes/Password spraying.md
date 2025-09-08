
# Password spraying

[[🏷️Password attack]]

Password spraying is a type of password attack where an attacker tries a common set of passwords across multiple accounts rather than targeting a single account with many different passwords. This method is used to avoid account lockouts that typically occur when multiple incorrect login attempts are made on one account.

The attacker focuses on using a small number of widely-used passwords, such as "123456" or "password," and attempts them across many accounts. If the first set of passwords doesn’t work on a particular account, the attacker moves on to the next account. This technique is effective because it doesn’t trigger security mechanisms like account lockouts or alerts that would occur with many failed attempts on a single account.

To defend against spraying attacks, organizations can implement account lockout policies after a certain number of failed login attempts across all accounts, monitor for unusual login patterns, and require multi-factor authentication (MFA) to add an extra layer of security.

---

See also:

- [[Brute force attack]]