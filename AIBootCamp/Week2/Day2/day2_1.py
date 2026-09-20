import numpy as np

# Array and Scalar Broadcasting
# Broadcasting is a powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations. 
# It automatically expands the smaller array to match the shape of the larger array without making unnecessary copies of data. 
# This feature is particularly useful for vectorized operations, enabling efficient computations.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
scalar = 10
result = arr + scalar
#print("Original Array:")
#print(arr)
#print("After adding scalar 10:")
#print(result)

vector = np.array([1, 0, 1])
result_vector = arr + vector
#print("After adding vector [1, 0, 1]:")
#print(result_vector)


# Sum, Mean, Max, Min, Standard Deviation, Sum along row and column
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# print("Sum of all elements:", np.sum(arr2))
# print("Mean of all elements:", np.mean(arr2))
# print("Max of all elements:", np.max(arr2))
# print("Min of all elements:", np.min(arr2))
# print("Standard Deviation of all elements:", np.std(arr2))
# print("Sum along rows:", np.sum(arr2, axis=1))
# print("Sum along columns:", np.sum(arr2, axis=0))


# Boolean Indexing
arr3 = np.array([1, 2, 3, 4, 5])
evens = arr3[arr3 % 2 == 0]
# print("Even numbers in the array:", evens)

arr3[arr3 > 3] = 0
# print("Array after setting elements greater than 3 to 0:", arr3)


# Setting Seed ensures each generation will give same output
np.random.seed(12)

# Random Number Generation
random_arr = np.random.rand(2, 3)
print("Random Array: \n", random_arr)

random_integers = np.random.randint(0,10,size=(2,3))
print("Random Integers: \n", random_integers)



