import matplotlib.pyplot as plt


def f(a):
    if -5 <= a <= 5:
        return a * a
    elif a < - 5:
        return 2 * abs(a) - 1
    else:
        return 2 * a


try:
    x = int(input('Enter x:  '))
    print(f(x))
    f1 = f(x)
    x1 = x
    plt.scatter(x1, f1, color='r')
except ValueError:\
    print('Bad x')


arg = [i for i in range(-10, 11, 1)]
f = [f(i) for i in range(-10, 11, 1)]
plt.plot(arg, f)
plt.show()
