# 9. How to stack two arrays horizontally?
# Q. Stack the arrays a and b horizontally.
import numpy as np
a = np.arange(10).reshape(2,-1)

b = np.repeat(1, 10).reshape(2,-1)

c = np.hstack([a,b])

print(c)