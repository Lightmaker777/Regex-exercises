#Exercise 1: Write a regex pattern that matches any string containing three consecutive digits.

import re

strings = ["123", "abc456", "789xyz", "12", "1a2b3c"]

pattern = r"\d{3}"

for string in strings:
    if re.search(pattern, string):
        print(f"Match found in '{string}'")
    else:
        print(f"No match found in '{string}'")