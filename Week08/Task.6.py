import numpy as np


def cute_norm(m):
    return m / max(abs(np.max(m)), abs(np.min(m)))


matrix = np.array([[1, 2, 3], [4, 5, -19]])
matrix = cute_norm(matrix)
print(matrix)
