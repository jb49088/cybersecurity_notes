
# Session Fixation

[[🏷️Web application attack]]

Session fixation is a type of security vulnerability where an attacker is able to set or "fix" a user's session identifier (session ID) before the user logs in. This allows the attacker to take control of the user's session once they authenticate, effectively hijacking their session and gaining unauthorized access to the victim's account.

In a session fixation attack, the attacker tricks the victim into using a session ID they control. After the victim logs in, the attacker can use the same session ID to impersonate the victim and access their sensitive information or perform malicious actions.

To mitigate session fixation attacks, websites should implement measures such as regenerating session IDs after a user logs in, using secure cookies with the `HttpOnly` and `Secure` flags, and enforcing session timeouts. These practices make it much harder for attackers to exploit session IDs and hijack user sessions.

---

See also:

- [[Session ID]]
- [[Session hijacking]]

