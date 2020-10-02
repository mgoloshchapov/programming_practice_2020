a,b,c = input(), input(), input()
if c > b:
    a,b,c = a,c,b
if c > a:
    a,b,c = c,a,b
print(c)