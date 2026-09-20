# [expression for item in iterable if condition]

# Create a list of squares
squares = [x**2 for x in range(10)]
#print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Filter even numbers from a list
evens = [x for x in range(20) if x % 2 == 0]
#print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Lambda functions
# lambda arguments: expression

add = lambda x, y: x + y
#print(add(5, 3))  # Output: 8

# map() function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
#print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# filter() function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print(even_numbers)  # Output: [2, 4]

# reduce() function
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
#print(product)  # Output: 120

# Pythons OS and Sys Modules
import os

#print(os.getcwd())
#os.mkdir('test_directory')  # Create a new directory named 'test_directory'
#os.rmdir('test_directory')  # Remove the directory named 'test_directory'
#os.remove('test_file.txt')  # Remove a file named 'test_file.txt'

import sys

#print(sys.version)  # Print the Python version
#print(sys.platform)  # Print the platform (e.g., 'win32', 'linux', 'darwin')
#print(sys.argv)  # Print the list of command-line arguments passed to the script