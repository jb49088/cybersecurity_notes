
# Data execution prevention (DEP)

Data execution prevention (DEP) is a security feature that helps protect systems from malicious attacks by preventing the execution of code in certain regions of memory that are not meant to execute program instructions. DEP helps mitigate exploits such as buffer overflow attacks, which attempt to inject malicious code into executable regions of memory.

- **Memory protection:** DEP marks certain areas of memory (such as the stack and heap) as non-executable, meaning no code can run from these regions.
- **Prevention of buffer overflow attacks:** By restricting execution to only certain parts of memory, DEP reduces the risk of exploits that rely on injecting code into regions like the stack.
- **Hardware-based DEP:** Modern processors include hardware-based DEP, which provides stronger protection by using specific CPU features to enforce memory execution rules.
- **Software-based DEP:** For systems that lack hardware support, software-based DEP offers a similar level of protection through operating system-level safeguards.
- **Compatibility and exceptions:** While DEP improves security, certain older applications or drivers may not be compatible with DEP and may require exceptions to allow execution in restricted memory areas.

DEP is an important component in defending against memory-based vulnerabilities, helping enhance the overall security of systems by reducing the likelihood of successful exploitation.

---

See also:

- [[Buffer overflow]]
- [[Address space layout randomization (ASLR)]]