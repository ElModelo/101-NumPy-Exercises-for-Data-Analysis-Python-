# 8. How to stack two arrays vertically?
# Q. Stack arrays a and b vertically
import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c = np.vstack([a,b])
print(c)