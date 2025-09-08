
# Session hijacking

[[🏷️Web application attack]]

Session hijacking is an attack where an attacker takes control of a user’s active session, typically after intercepting session tokens or credentials transmitted during communication. The attacker can impersonate the legitimate user, gaining unauthorized access to web applications or networks.

Session hijacking often occurs through methods like sniffing (capturing session tokens over insecure networks), cross-site scripting (XSS), or on-path attacks. Once the attacker obtains the session cookie or session ID, they can use it to authenticate themselves without needing the user’s login credentials.

![[Image 3.45.png|center|700]]

To prevent session hijacking, it is essential to use secure protocols such as HTTPS, implement secure cookie attributes (e.g., HttpOnly, Secure), and regularly rotate session tokens. Additionally, session timeouts and multifactor authentication (MFA) can help minimize the risks.

---

See also:

- [[Session]]
- [[Session ID]]
- [[Cookie]]
- [[Cross-site scripting (XSS)]]
- [[On-path attack]]

