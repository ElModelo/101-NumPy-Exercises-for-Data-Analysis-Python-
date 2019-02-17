# 5. How to replace items that satisfy a condition with another value in numpy array?
# Q. Replace all odd numbers in arr with -1
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[1:10:2] = -1
print(arr)