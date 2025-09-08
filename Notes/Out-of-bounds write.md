
# Out-of-bounds write

An out-of-bounds write occurs when a program writes data beyond the allocated boundaries of a buffer or memory region. This can result in memory corruption, crashes, or the execution of malicious code, posing significant security risks.

Common causes include:

- **Improper Input Validation:** Failing to verify the size or type of input data.
- **Programming Errors:** Incorrect buffer size calculations or array indexing.
- **Unchecked Memory Access:** Writing data without ensuring it fits within allocated memory.

Out-of-bounds writes are often exploited to inject malicious code or overwrite critical memory structures, leading to system compromise or privilege escalation. Mitigation involves using safe coding practices, bounds checking, and tools to identify vulnerabilities during development.

---

See also:

- [[Buffer overflow]]
- [[Code injection]]

