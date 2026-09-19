# Count the number of words and lines in a text file
def count_words_and_lines(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            print(f"Total lines: {line_count}")
            print(f"Total words: {word_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the file path and try again.")
        

count_words_and_lines("input.txt")