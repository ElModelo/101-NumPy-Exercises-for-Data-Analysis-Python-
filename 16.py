# 16. How to swap two columns in a 2d numpy array?
# Q. Swap columns 1 and 2 in the array arr.
import numpy as np
arr = np.arange(9).reshape(3,3)
arr2 = arr.copy()
arr2[::,0:1] = arr[::,1:2]
arr2[::,1:2] = arr[::,0:1]
print(arr2)