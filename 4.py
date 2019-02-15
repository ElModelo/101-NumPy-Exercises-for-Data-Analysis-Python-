# 4. How to extract items that satisfy a given condition from 1D array?
# Q. Extract all odd numbers from arr
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = []
for a in arr:
	if a % 2 != 0:
		x.append(a)
print(x)
