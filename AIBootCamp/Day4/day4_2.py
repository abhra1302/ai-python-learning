sentence = input("Enter a sentence: ")

#Split the sentence into words
words = sentence.split()

# Initialize a dictionary to hold word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    word = word.lower()  # Convert to lowercase for case-insensitive counting
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
