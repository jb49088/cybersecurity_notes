
# Interpreting the CVSS Vector

The CVSS vector uses a single-line format to convey the ratings of a vulnerability on all eight of the metrics. For example, see the CVSS vector for the vulnerability
presented in Image 2.51.

![[Image 2.51.png]]

`CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N`

This vector contains nine components. The first section, “CVSS:3.0,” simply informs the reader (human or system) that the vector was composed using CVSS version 3. The next eight sections correspond to each of the eight CVSS metrics. In this case, the SSL vulnerability in Image 2.51 received the following ratings:

- Attack Vector: Network (score: 0.85) 
- Attack Complexity: Low (score: 0.77) 
- Privileges Required: None (score: 0.85) 
- User Interaction: None (score: 0.85) 
- Scope: Unchanged  
- Confidentiality: High (score: 0.56) 
- Integrity: None (score: 0.00) 
- Availability: None (score: 0.00)