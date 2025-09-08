
```mermaid
flowchart LR
    Hosts["Hosts"] --- LAN["LAN"]
    LAN --- IPS["IPS"]:::highlight
    IPS --- Router["Router"]
    Router --- Firewall["Firewall"]
    Firewall --- Modem["Modem"]
    Modem --- WebService["Web Service"]

    classDef highlight fill:#003366,stroke:#003366,stroke-width:2px,color:#ffffff;
```


