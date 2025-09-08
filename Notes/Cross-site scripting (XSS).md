
# Cross-site scripting (XSS)

[[🏷️Web application attack]]

Cross-site scripting (XSS) is a common and dangerous web application vulnerability that exploits the trust users have in a website. Despite its name, XSS does not involve Cascading Style Sheets (CSS)—it originated from early browser security flaws that allowed malicious interactions between websites. Today, XSS remains a significant threat to online security.

XSS vulnerabilities allow attackers to inject malicious scripts, often using JavaScript, into web pages viewed by other users. These scripts can steal sensitive information such as session cookies, credentials, or other personal data without the user's knowledge.

![[Image 2.77.png|center|700]]

To protect against XSS, avoid clicking on suspicious links, especially from untrusted sources. Consider disabling JavaScript or using browser extensions for better control, though this isn't foolproof. Regularly update your browser and applications to patch vulnerabilities, and ensure websites validate and sanitize user inputs to prevent script injection, restricting the types of data users can submit.

## Non-persistent (Reflected) XSS

In a non-persistent XSS attack, the malicious script is executed immediately and does not remain on the website. This type of attack typically involves:

1. **User Input Exploitation**: Attackers exploit web pages that execute scripts based on user inputs, such as a search box.
2. **Malicious Links**: Attackers craft URLs containing the payload and send these links via email or other means.
3. **Execution in the Victim's Browser**: When the victim clicks the link, the script executes as if it originated from the trusted server, stealing sensitive data like credentials or session IDs.

## Persistent (Stored) XSS

Persistent XSS attacks are more potent and widespread. These attacks occur when malicious payloads are permanently stored on a website, such as in a comment section or social media post. Characteristics include:

1. **Stored Payload**: The attacker posts malicious scripts, embedding them within the website's data.
2. **Broad Impact**: Any user who views the infected page unknowingly triggers the malicious code.
3. **Self-Propagation**: Particularly in social networks, the attack can spread virally, as users interacting with the infected content unknowingly propagate it further.

---

See also:

- [[Injection attack]]
- [[JavaScript]]
- [[Web application]]
- [[Input sanitization]]
- [[Input validation]]


