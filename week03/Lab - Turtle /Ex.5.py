import turtle as t

t.shape('turtle')

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
for i in range(4):
    t.penup()
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.pendown()
    t.right(90)
    t.forward(80 - 20*i)
    t.left(90)
    t.forward(80 - 20*i)
    t.left(90)
    t.forward(80 - 20*i)
    t.left(90)
    t.forward(80 - 20*i)


