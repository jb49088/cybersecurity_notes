```mermaid
graph LR
    User -->|Input| Application
    Application -->|Request| OperatingSystem[Operating System]
    OperatingSystem -->|Command| Hardware
    Hardware -->|Response| OperatingSystem
    OperatingSystem -->|Output| Application
    Application -->|Feedback| User
```