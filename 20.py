# 20. How to create a 2D array containing random floats between 5 and 10?
# Q. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.
import numpy as np
arr = np.random.uniform(5,10, size=(5,3))
print(arr)