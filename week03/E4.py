A = [int(i) for i in input().split()]
for i in range(len(A)):
    n = 'x'
    for j in range(i+1,len(A)):
        if A[j] == A[i]:
            A[j] = 'f'
            n = i
    if n != 'x':
        A[i] = 'f'
B = []
for i in A:
    if i != 'f':
        B += [i]
print(*B)


