n = int(input())
sum = 0
a = 1
for i in range(1,n+1):
    sum += a*i
    a = a*i
print(sum)
print(a)