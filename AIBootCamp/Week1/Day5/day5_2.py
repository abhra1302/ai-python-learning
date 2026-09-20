import re

text = "Contact me at 123-456-7890 or 987-654-3210. My office number is (555) 123-4567."
digits = re.findall(r"\d+", text)
print(digits)  # Output: ['123', '456', '7890', '987', '654', '3210', '555', '123', '4567']

updated_text = re.sub(r"\d", "X", text)
print(updated_text)  # Output: Contact me at XXX-XXX-XXXX or XXX-XXX-XXXX. My office number is (XXX) XXX-XXXX.


# clean text

def clean_text(text):
    #Remove punctuation
    text = re.sub(r"[^\w\s]","", text)
    #Remove extra whitespace
    text = " ".join(text.split())
    return text.lower()

input_text = "  Hello, World! This is a test.  "
cleaned_text = clean_text(input_text)
print(cleaned_text)  # Output: hello world this is a test

# check if a string is a palindrome

def is_palindrome(s):
    s = "".join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]