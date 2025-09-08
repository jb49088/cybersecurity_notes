# Redirection (Linux)

Redirection in Linux is a shell feature that allows users to change the standard input (stdin), standard output (stdout), and standard error (stderr) streams of commands. This enables control over where input comes from and where output or error messages are sent, facilitating more flexible and powerful command-line operations.

- **Output redirection (`>` and `>>`):** Sends the output of a command to a file instead of the terminal. Using `>` overwrites the file, while `>>` appends to it.
- **Input redirection (`<`):** Takes input for a command from a file instead of the keyboard.
- **Error redirection (`2>` and `2>>`):** Redirects error messages to a file. Like output redirection, `2>` overwrites and `2>>` appends.
- **Combining redirection:** Standard output and error can be redirected together using syntax like `command > file 2>&1`, sending both output and errors to the same file.
- **Here documents (`<<`):** Allows feeding multiple lines of input directly into a command from within a script or command line.

Redirection is fundamental for scripting and advanced shell usage, enabling users to capture outputs, log errors, and automate complex workflows.

---

See also:

- [[Standard input (stdin)]]
- [[Standard output (stdout)]]
- [[Standard error (stderr)]]
-  [[pipe]]