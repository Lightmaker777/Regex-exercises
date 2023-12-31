#Exercise 4: Write a regex pattern that matches any string containing a valid date in the format "DD-MM-YYYY".

import re

dates = ["31-12-2022", "15-06-23", "02/05/2023", "2022-12-31", "01-13-2023"]

pattern = r"^(0[1-9]|[1-2][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$"

for date in dates:
    if re.search(pattern, date):
        print(f"Match found in '{date}'")
    else:
        print(f"No match found in '{date}'")
