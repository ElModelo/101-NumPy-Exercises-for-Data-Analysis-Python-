# 23. How to limit the number of items printed in output of numpy array?
# Q. Limit the number of items printed in python numpy array a to a maximum of 6 elements.
import numpy as np
a = np.arange(15)
np.set_printoptions(threshold = 6)
print(a)