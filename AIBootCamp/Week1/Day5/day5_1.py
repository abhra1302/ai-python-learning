#Strings and String Operations

first="Hello"
second="World"
result=first + " " + second
#print(result)

text = "Python Programming"
#print(text[0:6])  # Output: Python
#print(text[-11:])  # Output: Programming

name = "Alice"
age = 30
# Using f-string for formatting
#print(f"My name is {name} and I am {age} years old.")

# split and join
# sentence = "Python, is, a, powerful, programming, language"
# words = sentence.split(",")  # Split into words
# print(words)

# # Join the words back into a string
# new_sentence = "|".join(words)
# print(new_sentence)

text = "Java is great"
updated_text = text.replace("Java", "Python")
print(updated_text)  # Output: Python is great

messy = "   This is a messy string.   "
cleaned_text = messy.strip()
print(cleaned_text)  # Output: This is a messy string.