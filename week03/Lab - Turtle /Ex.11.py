import turtle as t

t.color('red')
t.shape('turtle')
t.speed(9)
for j in range(11):
    for i in range(100):
        t.forward(1+0.5*j)
        t.right(3.6)
    t.right(180)
    for i in range(100):
        t.forward(1+0.5*j)
        t.right(3.6)
    t.right(180)