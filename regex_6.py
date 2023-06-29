#Exercise 6: Write a regex pattern that matches any string containing a valid phone number in the format "+XX-XXXXXXXXXX", where X represents a digit.

import re

phone_numbers = ["+91-1234567890", "+44-9876543210", "+1-1234567890", "+12-9876543210", "+1-1234"]

pattern = r"\+\d{2}-\d{10}\b"

for phone_number in phone_numbers:
    if re.search(pattern, phone_number):
        print(f"Match found in '{phone_number}'")
    else:
        print(f"No match found in '{phone_number}'")

