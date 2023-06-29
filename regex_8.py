#Exercise 8: Write a regex pattern that matches any string containing a word that starts with a capital letter and is followed by one or more lowercase letters.

import re

sentences = ["Hello, World!", "This is a Sentence.", "openAI", "python", "One Two Three"]

pattern = r"\b[A-Z][a-z]+\b"

for sentence in sentences:
    if re.search(pattern, sentence):
        print(f"Match found in '{sentence}'")
    else:
        print(f"No match found in '{sentence}'")
