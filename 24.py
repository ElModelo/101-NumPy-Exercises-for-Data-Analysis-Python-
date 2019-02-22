# 24. How to print the full numpy array without truncating 
# Q. Print the full numpy array a without truncating.
import numpy as np
np.set_printoptions(threshold=6)
a = np.arange(15)
np.set_printoptions(threshold=np.nan)
print(a)

