import turtle as t
t.shape('turtle')
t.color('pink')
for i in range(3,14):
    t.pendown()
    for j in range(1,i+1):
        t.forward(3+6*i+(i/2)**2)
        t.right(int(360/i))
    t.penup()
    t.left(360/i)
    t.forward(2.7*i)
    t.right(360/i)