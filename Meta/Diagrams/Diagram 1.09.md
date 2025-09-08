```mermaid
%%{ init: { 'flowchart': { 'curve': 'bump' } } }%%
graph TD
Internet --- Modem
Modem --- Router
Router --- Wireless_Access_Point[Wireless Access Point]
Router --- Wired_Computer[Wired Computer]
Wireless_Access_Point --- |Wi-Fi| Wireless_Laptop[Wireless Laptop]
Wireless_Access_Point --- |Wi-Fi| Wireless_Server[Wireless Server]
Wireless_Server --- |Wi-Fi| Wireless_Printer[Wireless Printer]
style Wireless_Access_Point fill:#4169e1,stroke:none
```
