#Exercise 10 (Optional): Write a regular expression to validate a password with the following criteria: - At least 8 characters long - Contains at least one uppercase letter - Contains at least one lowercase letter - Contains at least one digit - Contains at least one special character (e.g., !@#$%^&*) The code Should include specific error messages for each validation criterion

import re

passwords = ["Abcd1234!", "passWORD!123", "abc123", "Password", "12345678"]

for password in passwords:
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least one digit")
    if not re.search(r"[!@#$%^&*]", password):
        errors.append("Password must contain at least one special character (!@#$%^&*)")
    
    if len(errors) == 0:
        print(f"'{password}' is a valid password.")
    else:
        error_message = ", ".join(errors)
        print(f"'{password}' is an invalid password. Reason(s): {error_message}.")
