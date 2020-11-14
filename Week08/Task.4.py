import numpy.random as random
import numpy as np

n = random.randint(10, 101)  # размерность матрицы
print(n)

matrix = random.sample((n, n))  # создание рандоматрицы
print(matrix)

maximum = np.max(matrix)  # загадка от Жака Фреско: Что это?
print(maximum)

matrix = matrix / maximum  # поделить все на максимум
print(matrix)

summa = matrix.sum()  # сумма элементов
print(summa)

matrix = matrix - np.mean(matrix, axis=1)  # от строки среднее отнять
print(matrix)
matrix.flat[np.argmax(matrix)] = -1  # удар по максимуму
