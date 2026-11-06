import numpy as np 

scores = np.array([12, 13, 14])

print(scores * 5, "\n") # Multiplying the array by 5

print(scores.mean(), "\n") # Mean of the array

two_d_array = np.array([[1, 2, 3], [4, 5, 6]])

print(two_d_array, "\n") # Printing the 2D array

print(two_d_array.shape, "\n") # The shape of the array is (2, 3) which means 2 rows and 3 columns

print(two_d_array[0, 1], "\n") # Accessing the element in the first row and second column

print(two_d_array[1, :], "\n") # Accessing all elements in the second row

input("Press Enter to continue...")

temps = np.array([25, 35, 54, 12, 32, 45, 67, 89, 90, 100])

print((temps * 9/5) + 32, "\n") # Converting Celsius to Fahrenheit

print(temps[temps > 50], "\n") # Filtering the array to get values greater than 50