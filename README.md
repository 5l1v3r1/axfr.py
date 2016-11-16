# axfr.py
Attempts zone transfers (axfr queries) on multiple domains in a list against a single name server.

### Usage:
-n NAMESERVER, --nameserver NAMESERVER (Name server e.g. ns1.target.com)  <br />
-d DOMAINS, --domains DOMAINS (Path to list of domain names)  <br />
-o OUTPUT, --output OUTPUT (Destination output file)  <br />

### Example:
$ axfr.py -n nameserver.target.com -d list_of_domains.txt
