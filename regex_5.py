#Exercise 5: Write a regex pattern that matches any string containing a valid URL starting with "http://" or "https://".

import re

urls = ["http://www.example.com", "https://www.google.com", "ftp://invalid-url.com", "https://sub.domain.co.uk", "http://localhost"]

pattern = r"\b(?:http|https)://\S+\b"

for url in urls:
    if re.search(pattern, url):
        print(f"Match found in '{url}'")
    else:
        print(f"No match found in '{url}'")
