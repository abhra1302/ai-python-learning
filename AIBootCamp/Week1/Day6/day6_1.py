# Reading and Writing Files in Python

# r | w | a | r+(read & write) | w+(write & read) | a+(append & read)
    
with open("input.txt", "r") as file:
    content = file.readlines()
    print(content)
    
# Reading Files - .read() - reads the entire file, .readlines() - reads the file line by line, .readline() - reads one line at a time

# Writing Files - .write() - writes to the file, .writelines() - writes a list of lines to the file

with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.writelines(["This is line 1.\n", "This is line 2.\n", "This is line 3.\n"])
    
# using 'with' Stattements for File Handling - automatically closes the file after the block of code is executed, even if an exception is raised

# Basic Exception Handling - using try-except blocks to handle exceptions that may occur during file operations

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
    
# Common File Handling Errors - FileNotFoundError, PermissionError, IOError, etc.
