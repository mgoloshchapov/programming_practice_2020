import numpy as np


def sort_by_col(m):
    n_m = m[m[:, 2].argsort()]
    return n_m


matrix = np.array([[1, 2, 3], [5, 1, 5], [4, 4, 2]])
matrix = sort_by_col(matrix)
print(matrix)

