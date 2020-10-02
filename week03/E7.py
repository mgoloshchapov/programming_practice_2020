n = int(input())
A = set()
for i in range(n):
    B = input().split()
    for j in A:
        A.add(j)
print(len(A))