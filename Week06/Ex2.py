def gcd(a):
    b = []  # массив для значений нод
    if type(a) == list:  # проверить,что дан массив
        for i in range(len(a)):
            if a[i][1] > a[i][0]:
                a[i][1], a[i][0] = a[i][0], a[i][1]  # проверить, что первое число пары наибольшее
            while True:  # алгоритм Евклида
                if a[i][1] < 0:
                    b += [f'Negative number in pair {i+1}']  # проверить, что числа неотрицательные
                    break
                if a[i][1] == 0:
                    b += [a[i][0]]
                    break
                a[i][0], a[i][1] = a[i][1], a[i][1] % a[i][0]
    else:
        print('NOT LIST')
    return b
