```mermaid
%%{ init: { 'flowchart': { 'curve': 'bump' } } }%%
graph TD
Internet --- Modem
Modem --- Firewall
Firewall --- Router
Router --- Switch
Switch --- Server
Switch --- Printer
Switch --- Laptop
Switch --- Desktop
Switch --- Router1[Router]
Router1 ---|Wi-Fi| Laptop2[Laptop]
Router1 ---|Wi-Fi| SmartPhone[Smart Phone]
```