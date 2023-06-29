#Exercise 3: Write a regex pattern that matches valid email addresses.

import re

emails = ["test@example.com", "john.doe@gmail.com", "invalid_email", "user@domain", "abc@123.xyz"]

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

for email in emails:
    if re.match(pattern, email):
        print(f"Match found in '{email}'")
    else:
        print(f"No match found in '{email}'")
