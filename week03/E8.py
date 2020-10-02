n = int(input())
A = dict()
for i in range(n):
    key, val = str(input()).split()
    A[key] = val
    A[val] = key
Key = input()
print(A)
print(A[Key])
