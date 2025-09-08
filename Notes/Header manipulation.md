
# Header manipulation

[[🏷️Network attack]]

Header manipulation is the process of modifying HTTP headers or cookies to alter the behavior of a web application, typically for malicious purposes. This attack often involves **information gathering** tools like Wireshark or Kismet to capture network traffic and identify vulnerable headers or cookies.

Once the data is collected, attackers may exploit vulnerabilities such as cross-site scripting (XSS) or use tools like Tamper, Firesheep, or Scapy to modify headers, gaining unauthorized access or manipulating user sessions. Cookies may also be modified using tools like the Cookies Manager+ Firefox add-on to hijack sessions or bypass security mechanisms.

To mitigate header manipulation attacks, web applications should validate input, use secure protocols like HTTPS, and implement proper session management techniques.

---

See also:

- [[Cross-site scripting (XSS)]]
- [[Session hijacking]]