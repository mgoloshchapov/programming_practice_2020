A = {}
while True:
    B = input().split()
    if B == []:# если считается, что текст задается
        break  # одной строкой, убрать эту часть
    for j in B:
        if j in A:
            A[j] += 1
        else:
            A[j] = 1
for val, key in A.items():
    print(val + ': ',key)