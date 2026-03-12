# curl

curl is a command-line tool and library used for transferring data to or from a server using a wide variety of network protocols. It is available on most operating systems and is widely used by developers, system administrators, and security professionals for testing, debugging, and interacting with network services and APIs.

- **Protocol support:** curl supports a broad range of protocols including HTTP, HTTPS, FTP, SFTP, SMTP, and more, making it a versatile tool for interacting with many different types of network services.
- **HTTP requests:** curl is most commonly used to send HTTP and HTTPS requests, allowing users to retrieve web pages, interact with REST APIs, submit forms, and test web server responses directly from the command line.
- **Custom headers and data:** curl allows users to specify custom request headers, HTTP methods, and request bodies, making it useful for testing APIs and web applications that require specific input formats or authentication tokens.
- **Authentication support:** curl supports a variety of authentication mechanisms including basic authentication, digest authentication, bearer tokens, and client certificates, enabling interaction with protected resources.
- **Following redirects:** By default curl does not follow HTTP redirects, but the -L flag instructs it to do so, making it easier to interact with services that redirect traffic.
- **Security testing:** In penetration testing, curl is frequently used to manually probe web applications, test for misconfigurations, interact with admin interfaces, and craft specific requests to identify vulnerabilities such as server-side request forgery (SSRF) or improper authentication handling.
- **libcurl:** The underlying library powering curl, libcurl, can be integrated into applications and scripts to provide programmatic network transfer capabilities in languages such as Python, C, and PHP.

curl is an essential utility in both development and security workflows, providing a straightforward and powerful way to interact with network services and inspect their behavior at the protocol level.

---

See also:

- [[hypertext_transfer_protocol_(http)]]
- [[hypertext_transfer_protocol_secure_(https)]]
- [[file_transfer_protocol_(ftp)]]
- [[ssh_file_transfer_protocol_(sftp)]]
- [[simple_mail_transfer_protocol_(smtp)]]
