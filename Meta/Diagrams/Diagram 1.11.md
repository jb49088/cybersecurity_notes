```mermaid
sequenceDiagram
    participant CHAP Server
    participant Client

    CHAP Server->>Client: Challenge
    Client->>CHAP Server: Response including Username and Password
    CHAP Server->>Client: Accept or Reject response
```
