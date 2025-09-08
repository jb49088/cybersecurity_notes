```mermaid
%%{ init: { 'flowchart': { 'curve': 'linear' } } }%%
graph TD
    root["/"] --> home
    root --> bin
    root --> etc
    home --> analyst
    home --> analyst2
    analyst --> projects
    analyst --> logs
    analyst --> reports
```