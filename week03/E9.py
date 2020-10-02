n = int(input())
A = {}
for i in range(n):
    B = input().split()
    for j in B:
        if j in A:
            A[j] += 1
        else:
            A[j] = 1
Key = []
Val = []
for key, val in A.items():
    Key += [key]
    Val += [val]
max = Val[0]
I = 0
for i in range(len(Val)):
    if Val[i] > max:
        I = i
        max = Val[I]
    elif Val[i] == max:
        if Key[i] < Key[I]:
            I = i
            max = Val[I]
print(Key[I])
