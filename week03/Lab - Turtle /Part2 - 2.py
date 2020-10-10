import turtle as t


def a0():
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.penup()
    t.left(90)
    t.forward(40)


def a1():
    t.penup()
    t.forward(30)
    t.pendown()
    t.left(90)
    t.pendown()
    t.forward(60)
    t.left(135)
    t.forward(42.42641)
    t.left(45)
    t.penup()
    t.forward(30)
    t.left(90)
    t.forward(40)


def a2():
    t.forward(30)
    t.pendown()
    t.backward(30)
    t.left(45)
    t.forward(42.42641)
    t.left(45)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.penup()
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(40)


def a3():
    t.pendown()
    t.left(45)
    t.forward(42.42641)
    t.left(135)
    t.forward(30)
    t.right(135)
    t.forward(42.42641)
    t.left(135)
    t.forward(30)
    t.penup()
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(40)


def a4():
    t.forward(30)
    t.left(90)
    t.pendown()
    t.forward(60)
    t.backward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.penup()
    t.backward(60)
    t.right(90)
    t.forward(40)


def a5():
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(60)
    t.left(90)
    t.forward(10)


# тут должны были быть оставшиеся цифры

A = [a0, a1, a2, a3, a4, a5]

inp = open('Text', 'r')
s = inp.read()


inp.close()
print(s)

t.penup()
t.goto(-300,0)
t.pendown()
for i in range(len(s)):
    A[int(s[i])]()
