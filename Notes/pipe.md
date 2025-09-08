
# pipe

[[🏷️Linux command]]

The pipe (`|`) is a powerful command-line feature in Linux that allows the output of one command to be passed directly as input to another. It enables users to build complex command sequences by connecting simple tools together in a streamlined workflow. Pipes are essential for effective use of the Unix philosophy—doing one thing well and chaining tools to perform more complex tasks.

- **Command chaining:** The pipe connects the standard output (stdout) of one command to the standard input (stdin) of another. This allows users to process data step by step without creating intermediate files.
- **Streamlined data processing:** Pipes are commonly used to filter, sort, or transform data. For example, you can combine `ps`, `grep`, and `sort` to search for and organize running processes.
- **Efficiency and simplicity:** Using pipes avoids unnecessary disk writes by passing data in memory between commands, making operations faster and more resource-efficient.
- **Examples:**
    - `ls -l | grep "txt"` — lists all `.txt` files in long format.
    - `cat file.txt | wc -l` — counts the number of lines in a file.
    - `dmesg | less` — views kernel log messages page by page.

Pipes are fundamental to shell scripting and interactive command-line use, enabling users to compose powerful, custom workflows with minimal effort.

---

See also:

- [[Standard input (stdin)]]
- [[Standard output (stdout)]]
- [[Redirection (Linux)]]
- [[Shell scripting]]