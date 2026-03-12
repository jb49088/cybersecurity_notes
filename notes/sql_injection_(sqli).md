# SQL injection (SQLi)

SQL Injection (SQLi) occurs when an attacker inserts or "injects" their own SQL code into an application's query. This can happen if the application fails to properly sanitize user inputs. The injected SQL code can manipulate the database, potentially allowing unauthorized access to, or modification of, sensitive data. SQLi is a serious vulnerability that can lead to data breaches, loss of information, or complete database compromise.

SQL injections are commonly executed via user input fields on web pages, such as login forms, search bars, or contact forms. Attackers can craft malicious SQL queries to bypass authentication, retrieve confidential data, or even modify or delete records.

To prevent SQLi, use prepared statements with parameterized queries to treat user input as data, not executable code. Additionally, ensure input sanitization to cleanse harmful characters, and validate input by enforcing expected formats, length restrictions, and valid data types.

## Example

Consider the following website code:

`“SELECT * FROM users WHERE name = ‘“ + userName + “’”;`

If the `userName` is "Professor", this query becomes:

`“SELECT * FROM users WHERE name = ‘Professor’”;`

An attacker can manipulate the input to inject malicious code, turning the query into:

``“SELECT * FROM users WHERE name = ‘Professor’ OR ‘1’ = ‘1’”;``

This will always return true, bypassing the authentication and exposing the data.

---

See also:

- [[code_injection]]
- [[structured_query_language_(sql)]]
- [[prepared_statement]]
- [[input_sanitization]]
- [[input_validation]]
