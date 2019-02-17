# 10. How to generate custom sequences in numpy without hardcoding?
# Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
import numpy as np
a = np.array([1,2,3])
x1, x2, x3 = np.split(a,[1,2])
arr = np.concatenate([x1,x1,x1,x2,x2,x2,x3,x3,x3,a,a,a])
print(arr)