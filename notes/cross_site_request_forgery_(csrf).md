# Cross-site request forgery (CSRF)

Cross-site request forgery (CSRF) is a web application attack where a malicious actor tricks an authenticated user into unknowingly submitting a request to a web application they are currently logged into. Because the request originates from the victim's browser, it carries their session credentials and is processed by the server as if it were a legitimate action performed by the user.

- **How it works:** When a user is authenticated to a web application, their browser automatically includes session cookies with every request made to that domain. An attacker can craft a malicious page or link that silently sends a request to the target application on the victim's behalf, causing actions such as changing account details, transferring funds, or modifying settings without the user's knowledge.
- **Conditions for exploitation:** A successful CSRF attack requires that the victim is authenticated to the target application, that the application relies solely on session cookies for authentication, and that the targeted action can be triggered by a predictable request without any secret value the attacker cannot obtain.
- **Common targets:** CSRF attacks typically target state-changing actions such as password or email changes, fund transfers, account deletions, form submissions, and administrative actions, rather than data retrieval, as the attacker cannot directly read the response.
- **GET vs POST requests:** Applications that use GET requests for state-changing actions are particularly vulnerable, as an attacker can trigger them with something as simple as an embedded image tag. POST-based CSRF typically requires a hidden form that auto-submits via JavaScript.
- **Impact:** The impact of a CSRF attack is directly tied to the privileges of the victim. If an administrator is targeted, the attacker may be able to perform highly privileged actions such as creating new admin accounts or modifying application-wide settings.
- **Mitigations:** The primary defense against CSRF is the use of CSRF tokens, which are unpredictable secret values tied to the user's session that must be included in every state-changing request. Additional mitigations include SameSite cookie attributes and verifying the Origin and Referer headers.

CSRF is a well-established vulnerability class that remains relevant in bug bounty hunting, particularly in applications that handle sensitive actions without properly validating the origin of requests or implementing token-based protections.

---

See also:

- [[cross-site_request_forgery_(csrf)_token]]
- [[cross-site_request]]
- [[cross-site_scripting_(xss)]]
