A = [int(i) for i in input().split()]
n = 0
for i in range(1,len(A)-1):
    if A[i] > A[i-1] and A[i] > A[i+1]:
        n += 1
print(n)