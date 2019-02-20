# 14. How to extract all numbers between a given range from a numpy array?
# Q. Get all items between 5 and 10 from a.
import numpy as np
a = np.array([2, 6, 1, 9, 10, 3, 27])
b = a[(a > 5) & (a <= 10)]
print(b)