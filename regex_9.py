#Exercise 9: Write a regular expression pattern that matches any hexadecimal color code in the format "#RRGGBB". Test it on the following color codes: "#FF0000", "#00FF00", "#0000FF", "#123ABC".

#To match hexadecimal color codes in the format "#RRGGBB", you can use the following regular expression pattern:

import re

color_codes = ["#FF0000", "#00FF00", "#0000FF", "#123ABC", "#abc123", "#1234567"]

pattern = r"^#[A-Fa-f0-9]{6}$"

for color_code in color_codes:
    if re.match(pattern, color_code):
        print(f"'{color_code}' is a valid hexadecimal color code")
    else:
        print(f"'{color_code}' is an invalid hexadecimal color code")
