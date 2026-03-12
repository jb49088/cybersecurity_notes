# Debug mode

Debug mode is a configuration setting available in most web frameworks and servers that enables verbose logging, detailed error pages, and additional diagnostic output to assist developers during application development and testing. While invaluable in a development environment, leaving debug mode enabled in production is a significant security misconfiguration frequently encountered in bug bounty hunting.

- **Verbose error pages:** When debug mode is enabled and an error occurs, the application typically returns a detailed error page containing stack traces, function calls, and internal file paths, revealing information about the application's structure and logic that would otherwise be hidden.
- **Source code and variable exposure:** Many frameworks, most notably Django, will display local variable values, environment variables, configuration settings, and fragments of source code within debug error pages, potentially exposing credentials, secret keys, and other sensitive data.
- **Framework implementations:** Debug mode exists across most major frameworks. Django exposes a highly detailed error page with application internals, Flask outputs interactive stack traces, Express.js in Node.js reveals server-side error details, and ASP.NET can expose stack traces and configuration information when debug is enabled.
- **Identifying debug mode:** In bug bounty hunting, debug mode can often be identified by intentionally triggering errors through malformed input, invalid routes, or unexpected parameter values and observing whether the server returns a detailed diagnostic page rather than a generic error response.
- **Common misconfiguration:** Debug mode is frequently left enabled when applications are moved from development to production without proper environment-specific configuration, making it a reliable target during reconnaissance and enumeration phases.
- **Impact:** The information leaked through debug mode can significantly accelerate further attacks by revealing internal architecture, dependency versions, file paths, and secrets that aid in crafting more targeted exploits.

Debug mode misconfiguration is a low-hanging fruit finding in bug bounty programs, often yielding sensitive information disclosures that can chain into more severe vulnerabilities when the exposed data is leveraged further.

---

See also:

- [[disclosure]]
- [[web_application]]
- [[reconnaissance]]
