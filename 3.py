# 3. How to create a boolean array?
# Q. Create a 3×3 numpy array of all True’s
import numpy as np
a = np.full((3,3), True, dtype = bool)
print(a)

# OR

b = np.ones((3,3), dtype=bool)
print(b)