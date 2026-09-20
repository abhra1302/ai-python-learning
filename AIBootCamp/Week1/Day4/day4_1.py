#List

# numbers = [1, 2, 3, 4, 5]

# fruits = ["apple", "banana", "cherry"]

# mixed_list = [1, "apple", 3.14, True]

# print(numbers[2])
# print(fruits[-1])
# print(mixed_list[-1])

# fruits.append("orange")
# fruits.remove("banana")
# fruits.insert(1, "kiwi")
# print(fruits)
# del fruits[0]
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.clear()
# print(fruits)

# print(fruits) 

# sliced_fruits = fruits[1:3]  # Slicing from index 1 to 2 (3 is exclusive)
# print(sliced_fruits)  # Output: ['banana', 'cherry'] 

#Tuple

# colors = ("red", "green", "blue")
# single_element_tuple = (42,)  # Note the comma to indicate it's a tuple

# print(colors[1])  # Output: green
# print(single_element_tuple[0])  # Output: 42
# print(len(colors))  # Output: 3
# print(colors[-1])  # Output: blue

# Dictionaries

# student = {
#     "name": "Alice",
#     "age": 20,
#     "courses": ["Math", "Science"]
# }

# print(student["name"])  # Output: Alice
# print(student.get("age"))  # Output: 20 

# student["age"] = 21  # Update age
# student["grade"] = "A"  # Add new key-value pair
# print(student) 

# del student["courses"]  # Remove the "courses" key
# print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A'}

# student.pop("grade")  # Remove the "grade" key
# print(student)  # Output: {'name': 'Alice', 'age': 21}

# for key, value in student.items():
#     print(f"{key}: {value}")  # Output: name: Alice, age: 21
    
#Sets
numbers_set = {1, 2, 3, 4, 5}

empty_set = set()  # Correct way to create an empty set

# Union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)  # or set_a | set_b
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a.intersection(set_b)  # or set_a & set_b
print("Intersection:", intersection_set)  # Output: {3}

# Difference
difference_set = set_a.difference(set_b)  # or set_a - set_b
print("Difference:", difference_set)  # Output: {1, 2}
