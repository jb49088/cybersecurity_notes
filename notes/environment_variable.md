# Environment variable

An environment variable is a dynamic named value stored within a process's environment that can influence the behavior of running programs and scripts on an operating system. They provide a way to pass configuration information to processes without hardcoding values directly into application code, and are available to any process that inherits them from its parent.

- **Key-value pairs:** Environment variables are stored as key-value pairs, where the key is the variable name and the value is the associated data. For example, PATH=/usr/bin:/bin defines the directories the system searches when looking for executables.
- **Scope and inheritance:** Environment variables can be set at the system level, user level, or session level. Child processes inherit environment variables from their parent process, meaning variables set in a shell session are available to any programs launched from it.
- **Common variables:** Frequently used environment variables include PATH, which defines executable search directories, HOME, which stores the current user's home directory, and USER, which holds the current username.
- **Configuration and portability:** Applications commonly rely on environment variables for configuration such as database connection strings, API keys, and file paths, allowing the same code to behave differently across development, staging, and production environments.
- **Security considerations:** Sensitive values stored in environment variables, such as passwords or API keys, can be exposed through process listings, log files, or error outputs. Care must be taken to ensure these values are not inadvertently leaked.
- **Manipulation in attacks:** Attackers can exploit environment variables in several ways, including path hijacking by modifying the PATH variable, injecting malicious values into variables consumed by vulnerable applications, or extracting secrets from improperly secured environments.

Environment variables are a fundamental part of how operating systems and applications manage configuration and runtime behavior, and their misuse or misconfiguration can introduce significant security vulnerabilities.

---

See also:

- [[Linux]]
- [[Windows]]
- [[Operating system (OS)]]
- [[Path hijacking]]
- [[Privilege escalation]]
- [[Injection attack]]
