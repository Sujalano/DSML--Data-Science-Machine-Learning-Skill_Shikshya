import numpy as np

# Checking Numpy Version
print(np.__version__)

"""
Creating a NumPy Array:
NumPy arrays are a powerful way to store and process large datasets. In this section, you will learn to create arrays.

Task 2:

Create a 1D NumPy array from a Python list of numbers: [1, 2, 3, 4, 5].
Create a 2D NumPy array of shape (3x3) using the numbers from 1 to 9.
Generate an array of 10 evenly spaced values between 0 and 5.
"""
Demin_01=np.array([1,2,3,4,5])
Demin_02= np.arange(1,10).reshape(3,3)
Dem_03 = np.linspace(0,5,10)

print("1D Array:", Demin_01)
print("\n2D Array:\n", Demin_02)
print("\nLinspace Array:\n", Dem_03)

"""
Indexing and Slicing Arrays:
Indexing and slicing allow you to access and modify specific elements of an array.

Task 3:

Access the element in the second row, third column of the 2D array you created above.
Slice the first two rows and the first two columns from the same array.
Modify the value in the last row and first column to 100.
"""
print(Demin_02[1,2])
print(Demin_02[:2,:2])
Demin_02[-1,0]=100
print(Demin_02)

"""
Properties and Methods of NumPy Arrays
NumPy arrays have several useful properties and methods.

Task 4:

Find the shape, size, and data type of the 2D array.
Change the 1D array into a 2D array of shape (5,1).
Flatten a multi-dimensional array back into a 1D array.
"""
print(Demin_02.shape)
print(Demin_02.size)
print(Demin_02.dtype)

Demin_02_Modify = Demin_02.reshape(9,1)
print(Demin_02_Modify)
arr_1d_back=Demin_02.flatten()
print(arr_1d_back)

"""
Operations on NumPy Arrays
Perform operations such as addition, subtraction, multiplication, and matrix multiplication on arrays.

Task 5:

Add 5 to every element in the 1D array.
Multiply the 2D array by 3.
Perform matrix multiplication between the following two arrays:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
"""

result_add = Demin_01 + 5
print(result_add)
result_mult = Demin_02 * 2
print(result_mult)
A = np.array([[1,2],[3,4]])
B = np.array([[5, 6], [7, 8]])
matrix_product= np.dot(A,B)
print(matrix_product)

"""
Understanding Broadcasting
Broadcasting allows NumPy to work with arrays of different shapes during arithmetic operations.

Task 6:

Create a 3x3 matrix of ones and a 1D array of length 3.
Add the 1D array to each row of the matrix using broadcasting.
"""
matix = np.ones((3,3))

row_to_add = np.array([1,2,3])
result = matix + row_to_add
print(result)