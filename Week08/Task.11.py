import numpy as np


def board(n):
    m = np.zeros((n, n))
    m[1::2, ::2] = 1  # нечетные элементы на четных строках заменяются на 1
    m[::2, 1::2] = 1  # взяли все строки, сделали шаг 2, взяли нечетные столбцы
    print(m)  # profit


board(4)
