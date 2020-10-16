def rectangle():
    print('Enter the sides of the rectangle')
    a = float(input())
    b = float(input())
    if a < 0 or b < 0:
        return 'Bad boy'
    else:
        return a * b


def triangle():
    print('Enter the sides')
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    if a <= 0 or b <= 0 or c <= 0 or p - a <=0 or p - b <= 0 or p -c <= 0: # проверить, что треугольник существует
        return 'Bad boy'
    else:
        s = (p * (p - a) * (p - b) * (p-c)) ** 0.5
        return s


def circle():
    r = float(input('Enter the radius:'))
    return 3.14159265359 * r * r


fig = input('Figure? (Choose from rectangle, triangle, circle):  ')

if fig == 'square':
    print(round(rectangle(), 4))
elif fig == 'triangle':
    print(triangle())
elif fig == 'circle':
    print(circle())
else:
    print('Bad boy')
