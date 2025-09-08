```mermaid
%%{ init: { 'flowchart': { 'curve': 'bump' } } }%%
graph TD
Modem --- Firewall
Modem --- Firewall1[Firewall]
Firewall --- Router 
Firewall1 --- Router1[Router]
Router --- CPU
Router --- PC
Router --- PC1[PC]
Router --- Laptop
Router1 --- CPU1[CPU]
Router1 --- PC2[PC]
Router1 --- PC3[PC] 
Router1 --- Laptop1[Laptop]
```
