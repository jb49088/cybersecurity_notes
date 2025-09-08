
# Cross-site request forgery (CSRF)

[[🏷️Web application attack]]

Cross-site request forgery (CSRF), also known as one-click attack or session riding, is an attack that exploits the trust a web application has in the user's browser. In a CSRF attack, the attacker sends unauthorized requests to a web application where the user is authenticated, taking actions without the user's knowledge or consent.

For example, an attacker could post a status on your Facebook account without you realizing it. This happens because the website trusts your browser and the session that is already established. The attacker exploits this trust to make the web application execute actions on your behalf.

![[Image 3.46.png|center|600]]

To prevent CSRF attacks, web applications should implement anti-forgery mechanisms, such as cryptographic tokens that verify the authenticity of requests and ensure they were made intentionally by the user.

---

See also:

- [[Cross-site request]]
- [[Cross-site scripting (XSS)]]
