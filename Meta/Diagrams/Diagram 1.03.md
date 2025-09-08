```mermaid
flowchart LR
Internet <--> Proxy[Proxy Server]
subgraph InternalNetwork[" "]
  Proxy <--> WebServer[Web Server]
end
```
