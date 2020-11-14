#  если я правильно понял условие
import numpy as np


def color_box(n, m, border, inside):
    matrix = np.zeros((n, m))
    matrix[::n - 1] = border
    matrix[::, ::m - 1] = border
    matrix[1:n - 1, 1:m - 1] = inside
    return matrix


print(color_box(4, 5, 1, 4))
