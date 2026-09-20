import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix:")
print(matrix)

# Transpose the matrix
transposed_matrix = np.transpose(matrix)  # or matrix.T can also be used for transposing
print("Transposed Matrix:")
print(transposed_matrix)


another_matrix = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Addition of two matrices:")
print(matrix + another_matrix)
print("Multiplication of two matrices:")
print(matrix * another_matrix)