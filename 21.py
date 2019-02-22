# 21. How to print only 3 decimal places in python numpy array?
# Q. Print or show only 3 decimal places of the numpy array rand_arr.
import numpy as np
rand_arr = np.random.random((5,3))
arr1 = np.round(rand_arr, decimals=3)
print(arr1)