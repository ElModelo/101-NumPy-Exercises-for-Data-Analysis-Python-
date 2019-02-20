# 12. How to remove from one array those items that exist in another?
# Q. From array a remove all items present in array b
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
c = a[np.isin(a, b, invert= True)]
print(c)