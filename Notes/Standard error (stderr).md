# Standard error (stderr)

Standard error (stderr) is one of the three standard data streams in Unix-like operating systems, used specifically for outputting error messages and diagnostics from commands or programs. Unlike standard output (stdout), which handles regular output data, stderr is reserved for error reporting, allowing users and scripts to separate normal output from error messages.

- **Separate stream:** Stderr provides a dedicated channel for error messages, which helps in debugging and logging issues without mixing them with normal output.
- **File descriptor:** Stderr is represented by file descriptor 2 in the system, while stdout is 1 and stdin is 0.
- **Redirection:** Users can redirect stderr independently from stdout, for example, sending error messages to a file with `command 2> error.log` without affecting standard output.
- **Usage in scripting:** Separating stderr from stdout allows scripts to handle errors gracefully, log problems, or alert users without disrupting regular data processing.
- **Common in pipelines:** Tools in command pipelines often send errors to stderr so that output can continue flowing through the pipeline unaffected.

Understanding and managing stderr is crucial for effective command-line use, troubleshooting, and writing robust shell scripts.

---

See also:

- [[Standard input (stdin)]]
- [[Standard output (stdout)]]