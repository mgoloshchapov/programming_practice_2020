import turtle as t

t.begin_fill()
t.fillcolor('yellow')
for j in range(100):
    t.forward(6.28)
    t.right(3.6)
t.end_fill()
t.penup()
t.goto(-50,-60)

t.pendown()
t.begin_fill()
t.fillcolor('blue')
for j in range(100):
    t.forward(1.57)
    t.right(3.6)
t.end_fill()
t.penup()
t.goto(50,-60)

t.pendown()
t.begin_fill()
t.fillcolor('blue')
for j in range(100):
    t.forward(1.57)
    t.right(3.6)
t.end_fill()
t.penup()
t.goto(0,-120)

t.pendown()
t.right(90)
t.color('brown')
t.width(5)
t.backward(30)
t.penup()
t.goto(0,-180)
t.pendown()

t.right(270)
t.color('red')
for j in range(50):
    t.width(5)
    t.forward(2)
    t.left(1.8)
t.penup()
t.goto(0,-180)
t.pendown()
t.right(90)
for j in range(50):
    t.backward(2)
    t.right(1.8)
t.right(1000)


