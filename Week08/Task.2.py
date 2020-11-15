import numpy as np
m = np.arange(2, 76)
print(m[m % 2 == 1])
m[m % 2 == 1] = -1
print(m)
