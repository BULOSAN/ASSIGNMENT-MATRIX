print("DOT METHOD")
print()
print("1.)")
print()

import numpy as np

m1 = np.array([[1, 2, 3], [6, 7, 8]])
m2 = np.array([[4, 5], [9, 10], [11, 12]])

result = np.dot(m1, m2)

print("Matrix 1:")
print(m1)
print()
print("Matrix 2:")
print(m2)
print()
print("The result is:")
print(result)
print()

print()
print("2.)")
print()

import numpy as np

m1 = np.array([[2, 8], [6, 4]])
m2 = np.array([[3, 3], [9, 1]])

result = np.dot(m1, m2)

print("Matrix 1:")
print(m1)
print()
print("Matrix 2:")
print(m2)
print()
print("The result is:")
print(result)

print()
print("3.)")
print()

import numpy as np

m1 = np.array([[1, 1], [3, 2], [7, 9]])
m2 = np.array([[5, 5, 5], [6, 6, 6]])

result = np.dot(m1, m2)

print("Matrix 1:")
print(m1)
print()
print("Matrix 2:")
print(m2)
print()
print("The result is:")
print(result)

print()
print("------------------------------------------")
print()

print("TRANSPOSE METHOD")
print()
print("1.)")
print()

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
array_transpose = np.transpose(array)

print("Original matrix:")
print(array)
print()
print("Transposed matrix:")
print(array_transpose)

print()
print("2.)")
print()

import numpy as np

array = np.array([[2, 2, 2], [3, 3, 3], [5, 5, 5]])
array_transpose = np.transpose(array)

print("Original matrix:")
print(array)
print()
print("Transposed matrix:")
print(array_transpose)

print()
print("3.)")
print()

import numpy as np

array = np.array([[1, 9], [8, 6,], [5, 1]])
array_transpose = np.transpose(array)

print("Original matrix:")
print(array)
print()
print("Transposed matrix:")
print(array_transpose)

print()
print("------------------------------------------")
print()

print("LINALG.INV METHOD")
print()
print("1.)")
print()

import numpy as np

array = np.array([[5, 6], [3, 2]])
array_inv = np.linalg.inv(array)

print("Original matrix:")
print(array)
print()
print("Inversed matrix:")
print(array_inv)

print()
print("2.)")
print()

import numpy as np

array = np.array([[1, 4, 7], [5, 10, 8], [3, 6, 1]])
array_inv = np.linalg.inv(array)

print("Original matrix:")
print(array)
print()
print("Inversed matrix:")
print(array_inv)

print()
print("3.)")
print()

import numpy as np

array = np.array([[1, 4, 8, 7], [5, 12, 10, 8], [9, 3, 6, 1], [1, 2, 3, 4]])
array_inv = np.linalg.inv(array)

print("Original matrix:")
print(array)
print()
print("Inversed matrix:")
print(array_inv)

print()
print("------------------------------------------")
print()

print("LINALG.DET METHOD")
print()
print("1.)")
print()

import numpy as np

array = np.array([[3, 2], [2, 3]])
det_array = np.linalg.det(array)

print("Matrix:")
print(array)
print()
print("Determinant:")
print(det_array)

print()
print("2.)")
print()

import numpy as np

array = np.array([[1, 2, 9], [12, 3, 4], [1, 1, 1]])
det_array = np.linalg.det(array)

print("Matrix:")
print(array)
print()
print("Determinant:")
print(det_array)

print()
print("3.)")
print()

import numpy as np

array = np.array([[8, 1, 8], [12, 1, 12], [2, 9, 10]])
det_array = np.linalg.det(array)

print("Matrix:")
print(array)
print()
print("Determinant:")
print(det_array)

print()
print("------------------------------------------")
print()

print("FLATTEN METHOD")
print()
print("1.)")
print()

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
array_flattened = array.flatten()

print("Original matrix:")
print(array)
print()
print("Flattened array:")
print(array_flattened)

print()
print("2.)")
print()

import numpy as np

array = np.array([[6, 3, 9], [0, 7, 1], [9, 6, 6], [0, 9, 8]])
array_flattened = array.flatten()

print("Original matrix:")
print(array)
print()
print("Flattened array:")
print(array_flattened)

print()
print("3.)")
print()

import numpy as np

array = np.array([[0, 1], [1, 8], [2, 0], [0, 5]])
array_flattened = array.flatten()

print("Original matrix:")
print(array)
print()
print("Flattened array:")
print(array_flattened)