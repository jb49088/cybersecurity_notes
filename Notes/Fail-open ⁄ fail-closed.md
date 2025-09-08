
# Fail-open ⁄ fail-closed

Fail-open and fail-closed are two types of behaviors used to define how systems handle failures or disruptions in their operation. These terms describe how systems or security mechanisms respond when they encounter an error or are unable to perform their intended functions.

- **Fail-open**: In a fail-open configuration, when a system experiences a failure, it defaults to an open state, allowing traffic or access to continue. This approach prioritizes availability over security, ensuring that the system remains operational, even if certain components are not functioning properly. It’s useful in situations where continuous service is critical, but it may expose the system to additional risks, as malicious actors may be able to access resources or data.
- **Fail-closed**: In contrast, a fail-closed system defaults to a closed state when a failure occurs. If a system or security measure encounters an error or is unable to function properly, it will restrict access or deny traffic to maintain security. While this approach reduces the risk of unauthorized access, it can potentially cause service interruptions or operational downtime.
    
Both strategies come with trade-offs:

- Fail-open provides better availability but at the cost of potentially lowering security.
- Fail-closed improves security but could cause more significant disruptions if a failure occurs.

Choosing between fail-open and fail-closed often depends on the system’s priorities (availability vs. security) and the specific use case.

---

See also:

- [[Mean time to failure (MTTF)]]
- [[Mean time between failures (MTBF)]]
- [[Intrusion prevention system (IPS)]]
- [[Intrusion detection system (IDS)]]