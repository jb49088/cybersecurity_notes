```mermaid
flowchart LR
subgraph InternalNetwork[" "]
  Endpoint <--> Proxy[Proxy Server]
end
Proxy <--> Internet
```
