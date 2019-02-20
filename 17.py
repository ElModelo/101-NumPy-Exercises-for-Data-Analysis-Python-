# 17. How to swap two rows in a 2d numpy array?
# Q. Swap rows 1 and 2 in the array arr:
import numpy as np
arr = np.arange(9).reshape(3,3)
print(arr[[1,0,2],:])