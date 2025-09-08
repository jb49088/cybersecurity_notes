```mermaid
flowchart LR
    A[Server] --> F
    F --> B[Recipient Server]

    subgraph F[" "]
        F1[Temporary Storage]
        F2[Proxy Server]
        F1 <--> F2
    end
```
