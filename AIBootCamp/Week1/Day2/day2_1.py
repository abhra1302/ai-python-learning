# Control Flow Statements in Python

#Example 1: Checking a condition using if-else statements
# num=-50
# if num > 0:
#     print("The number is positive.")
# elif num == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")
    
#Example 2: Nested conditions
# age=25
# if age > 18:
#     if age < 30:
#         print("You are an young adult.")
#     else:
#         print("Adult")

#Syntax for for-loop

# for item in sequence:
#     # Code block to be executed for each item in the sequence

# Loop with range
# for i in range(5):      #[0,1,2,3,4]
#     print("Iteration:", i)
    
# Loop through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print("Fruit:", fruit)

# Syntax for while-loop
# while condition:
#     # Code block to be executed as long as the condition is True

# Count down from 5
# count = 5
# while count > 0:
#     print("Count:", count)
#     count -= 1  # Decrement the count by 1
# print("Countdown finished!")

# break and continue statements
# for i in range(10):
#     if i == 6:
#         break  # Exit the loop when i is 6
#     print("Iteration:", i)

# for i in range(10):
#     if i == 6:
#         continue  # Skip the rest of the code in the loop when i is 6
#     print("Iteration:", i)
    
# for i in range(10):
#     if i % 2 == 0:
#         continue  # Skip even numbers
#     print("Odd Iteration:", i)
