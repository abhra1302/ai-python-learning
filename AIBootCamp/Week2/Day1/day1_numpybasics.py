import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
#print(arr)

zeroes = np.zeros((3, 4))
#print(zeroes)

ones = np.ones((2, 3))
#print(ones)

range_array = np.arange(1, 100, 3)
#print(range_array)

linspace_array = np.linspace(0, 1, 5)
#print(linspace_array)

reshaped_array = arr.reshape((2, 3))
#print(reshaped_array)

arr2 = np.array([1, 2, 3, 4, 5, 6])
expanded_array = arr2[:, np.newaxis]
#print(expanded_array)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)

arr3 = np.array([4, 9, 16, 25])
#print(np.sqrt(arr3))
#print(np.sum(arr3))
#print(np.mean(arr3))
#print(np.max(arr3))

arr4 = np.array([1,2,3,4,5,6])
#print(arr4[2])
#print(arr4[-1])
#print(arr4[1:4])
#print(arr4[3:])
#print(arr4[:3])
