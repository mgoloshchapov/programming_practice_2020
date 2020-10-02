A = [int(i) for i in input().split()]
max = A[0]
min = A[0]
maxi = 0
mini = 0
for i in range(1,len(A)):
    if A[i] > max:
        max = A[i]
        maxi = i
    elif A[i] < min:
        min = A[i]
        mini = i
A[maxi], A[mini] = A[mini], A[maxi]
print(*A)

