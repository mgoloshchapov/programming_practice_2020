def power(a, n):
    c = a
    for i in range(n-1):
        a *= c
    return a
