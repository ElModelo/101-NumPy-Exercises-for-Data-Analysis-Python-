# 18. How to reverse the rows of a 2D array?
# Q. Reverse the rows of a 2D array arr.
import numpy as np
arr = np.arange(9).reshape(3,3)
arr1 = arr[::-1]
print(arr1)