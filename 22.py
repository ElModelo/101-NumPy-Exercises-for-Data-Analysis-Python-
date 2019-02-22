# 22. How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
# Q. Pretty print rand_arr by suppressing the scientific notation (like 1e10)
import numpy as np
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress = True)
print(rand_arr)
