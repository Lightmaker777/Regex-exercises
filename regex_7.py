#Exercise 7: Write a regex pattern that matches any string containing a valid IPv4 address in the format
#"XXX.XXX.XXX.XXX", where XXX represents a number between 0 and 255.

import re

ip_addresses = ["192.168.0.1", "10.0.0.0", "256.0.0.0", "172.16.0.0", "127.0.0.1", "0.0.0.0"]

pattern = r"\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"

for ip_address in ip_addresses:
    if re.search(pattern, ip_address):
        print(f"Match found in '{ip_address}'")
    else:
        print(f"No match found in '{ip_address}'")
