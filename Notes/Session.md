
# Session

A session is a period of time during which a user interacts with an application or system, often involving the exchange of information between a client and server. In computing, sessions are used to maintain state across multiple interactions, enabling users to perform actions without having to re-authenticate or re-submit information during each request.

- **Session management**: Ensures that data persists across user interactions by assigning a unique session identifier (ID) to each user. This ID is typically stored in cookies, local storage, or URLs.
- **Authentication**: Sessions are commonly used after a user logs into a system, keeping the user authenticated throughout their interaction without requiring them to log in repeatedly.
- **Session expiration**: Sessions often have a time limit, after which they automatically expire, requiring the user to re-authenticate. This helps protect against unauthorized access and session hijacking.
- **Session hijacking**: An attack in which an attacker takes over an active session by stealing the session ID. This can lead to unauthorized access to sensitive information or systems.
- **Stateful communication**: Sessions enable stateful communication, meaning that the server can remember user preferences, shopping cart contents, or other personalized information over time.
    

Session management is a key component in web and application security, ensuring a smooth user experience while preventing unauthorized access and data breaches.

---

See also:

- [[Session ID]]
- [[Cookie]]

