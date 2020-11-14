import time
import matplotlib.pyplot as plt
import numpy as np
import random


plt.figure()
T_python = []
T_numpy = []

x = [int(i) for i in range(10000)] # считаем для простяцкого питона
y = 10000
for i in x:
    start_time = time.time()
    z = 2*i**2 +4*y
    T_python += [time.time() - start_time]

mean_python = [sum(T_python)/10000 for i in range(10000)]

plt.plot(x, T_python, 'b', label='Данные для Python')



x = np.arange(10000)
y = 10000

for i in x: # крутяцкий numpy
    start_time = time.time()
    z = 2*x**2 + 4*y
    T_numpy = T_numpy + [time.time() - start_time]
mean_numpy = [sum(T_numpy)/10000 for i in range(10000)]

plt.plot(x, T_numpy, 'y', label='Данные для Numpy ')


plt.plot(x, mean_python, 'green', label='Среднее для Python = {}'.format(sum(T_python)/10000))
plt.plot(x, mean_numpy, 'r', label='Среднее для Numpy = {}'.format(sum(T_numpy)/10000))

plt.title('Для выражений Python примерно в {} раз быстрее'.format(round(sum(T_numpy)/sum(T_python))))
plt.legend()
plt.show()

##########################
plt.figure()

T_python_matrix = []
T_numpy_matrix = []


def matrixmult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


for i in range(1000):
    x = [[random.randint(2, 1000) for k in range(10)] for j in range(10)]
    start_time = time.time()
    matrixmult(x, x)
    T_python_matrix += [time.time() - start_time]

plt.plot([int(i) for i in range(1, 1001)], T_python_matrix, 'b', label='Данные для Python')
plt.plot([int(i) for i in range(1, 1001)], [sum(T_python_matrix)/1000 for i in range(1, 1001)], 'g',
         label='Среднее для Python = {}'.format(sum(T_python_matrix)/1000))

for i in range(1000):
    x = np.array([[random.randint(2, 1000) for k in range(10)] for j in range(10)])
    start_time = time.time()
    np.matmul(x, x)
    T_numpy_matrix += [time.time() - start_time]

plt.plot([int(i) for i in range(1, 1001)], T_numpy_matrix, 'y', label='Данные для Numpy')
plt.plot([int(i) for i in range(1, 1001)], [sum(T_numpy_matrix)/1000 for i in range(1, 1001)], 'r',
         label='Среднее для Numpy = {}'.format(sum(T_numpy_matrix)/1000))

plt.title('Для матриц Numpy в {} раз быстрее Python'.format(round(sum(T_python_matrix)/sum(T_numpy_matrix))))
plt.legend()
plt.show()
