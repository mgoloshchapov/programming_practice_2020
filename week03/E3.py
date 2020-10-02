A = [i for i in input().split()]
n = 0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[j] == A[i]:
            n += 1