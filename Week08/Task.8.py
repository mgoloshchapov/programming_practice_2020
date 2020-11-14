import numpy as np
import numpy.random as random

m = np.random.sample([random.randint(1, 5) for i in range(random.randint(1, 5))])

n = float(input())
index = (np.abs(m-n)).argmin()
print(m.flat[index])