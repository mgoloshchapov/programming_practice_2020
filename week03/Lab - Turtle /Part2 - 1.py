import random as r
import turtle as t

t.shape('turtle')
t.color('pink')

while True:
    t.right(r.randint(-90,90))
    t.forward(r.randint(-30, 30))