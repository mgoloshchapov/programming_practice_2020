def remember(a):
    b = input('main or sub?')

    def pep8(m, v):
        l = len(m)
        c = 0
        if type(m) == list:  # проверить, что массив
            for i in range(l):  # 4-7 проверить, что матрица квадратная
                if len(m[i]) != l:
                    c = 1
                    break
                try:  # проверить, что на главной и побочной диагонали стоят числа
                    m[i][i], m[l - 1 - i][i] = float(m[i][i]), float(m[l - 1 - i][i])
                except ValueError:
                    c = 1
                    break
        else:
            c = 1
        if c == 0:  # начать выполнение, если матрица правильная
            if v == 'main':
                s = 0
                for k in range(len(m)):  # сумма на главной диагонали
                    try:
                        s += float(m[k][k])
                    except ValueError:
                        s = 'Bad boy'
                        break
                try:
                    s = int(s)
                except ValueError:
                    ''
                return s
            elif v == 'sub':
                s = 0
                for j in range(l):
                    try:
                        s += float(m[l - 1 - j][j])  # сумма на побочной
                    except ValueError:
                        s = 'Bad boy'
                        break
                try:
                    s = int(s)  # попытка напечатать целое число
                except ValueError:
                    ''
                return s
            else:
                return 'Bad boy'
        else:
            return 'Bad boy'
    return pep8(a, b)


d = [[1, 2], ['a', 3]]
print(remember(d))
