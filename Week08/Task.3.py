import numpy as np

A = np.array([1,2,3,4,5,6,7])
B = np.array([1,3,5,4])

C = np.setdiff1d(A, B)
print(C)
