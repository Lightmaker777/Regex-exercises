#Exercise 2: Write a regex pattern that matches any string containing only uppercase letters.

import re

strings = ["HELLO", "WORLD", "123", "Hello", "UPPERCASE"]

pattern = r"^[A-Z]+$"

for string in strings:
    if re.match(pattern, string):
        print(f"Match found in '{string}'")
    else:
        print(f"No match found in '{string}'")
