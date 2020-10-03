import turtle as t

n = 5
t.right(90+180/n)
for i in range(1,n+1):
    t.forward(100)
    t.right(180 - 180/n)

t.penup()
t.goto(200,0)
t.pendown()

n = 11
t.right(90 + 180 / n)
for i in range(1, n + 1):
    t.forward(100)
    t.right(180 - 180 / n)

t.right(3600)



