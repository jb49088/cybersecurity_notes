# Wordlist

A wordlist is a plain text file containing a collection of words, phrases, usernames, passwords, or directory names used as input for security tools during penetration testing and security assessments. Wordlists are fundamental to many brute-force and enumeration attacks, as they define the scope and effectiveness of automated guessing attempts.

- **Password cracking:** Wordlists are commonly used with tools like Hashcat or John the Ripper to attempt to crack hashed passwords by comparing hashes of wordlist entries against a captured hash.
- **Directory and file enumeration:** Tools like Gobuster or Dirb use wordlists to brute-force hidden paths on web servers, cycling through common directory and file names to discover unlisted resources.
- **Credential stuffing:** Wordlists of known username and password combinations, often sourced from previous data breaches, are used to attempt unauthorized access to accounts across multiple services.
- **Quality and relevance:** The success of a wordlist-driven attack depends on the quality of the list. A wordlist tailored to the target's industry, language, or technology stack will outperform a generic one.
- **Common wordlist sources:** SecLists is one of the most widely used repositories of wordlists, offering curated lists for a variety of attack types including passwords, usernames, fuzzing, and web content discovery.
- **Custom wordlists:** Tools like CeWL can generate custom wordlists by crawling a target website, producing a list of words unique to that target and increasing the likelihood of success.

Wordlists are a foundational resource in offensive security, and their quality directly influences the effectiveness of many enumeration and brute-force techniques.

---

See also:

- [[brute_force_attack]]
- [[credential_stuffing]]
- [[enumeration]]
- [[gobuster]]
- [[john_the_ripper]]
- [[default_credentials]]
