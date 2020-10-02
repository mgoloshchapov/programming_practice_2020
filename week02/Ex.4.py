v = int(input())#float(input()),если предполагается, что скорость не только целая
t = int(input())#аналогично
a = v*t
if a <0:
    while a < 0:
        a += 109
print(a)

