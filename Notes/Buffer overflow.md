
# Buffer overflow

[[🏷️Injection attack]]

A buffer overflow occurs when data exceeds the allocated memory buffer and spills into adjacent memory areas. This happens when a program does not properly manage memory, especially by failing to perform bounds checking. Attackers can exploit this vulnerability to overwrite important data, including function pointers or return addresses, which can lead to arbitrary code execution.

![[Image 2.76.png|center]]

While a buffer overflow may seem like a simple exploit, it often requires sophisticated manipulation to avoid causing a system crash. Attackers need to precisely control the overflow to make it execute specific commands, often through trial and error. However, when executed successfully, buffer overflows can lead to serious security risks, allowing attackers to gain unauthorized access, escalate privileges, or introduce malicious code into the system.

A particularly dangerous buffer overflow is one that is repeatable, meaning that the attacker can consistently trigger the exploit on the same system, which increases the likelihood of compromising it.

---

See also:

- [[Memory injection]]
- [[Address space layout randomization (ASLR)]]
- [[Data execution prevention (DEP)]]