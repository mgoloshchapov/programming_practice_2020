import math
x1 = input()
y1 = input()
x2 = input()
y2 = input()
def distance(x1,y1,x2,y2):
    x = (float(x1)-float(x2))**2
    y = (float(y1)-float(y2))**2
    d = math.sqrt(x+y)
    return d
print(distance(x1,y1,x2,y2))