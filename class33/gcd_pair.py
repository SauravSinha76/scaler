def sqrt(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return i
        i += 1
    return -1

def solve(A):
    n = len(A)
    res_len = sqrt(n)
    res = []
    for i in range(res_len):
        res.append(A[i*res_len +i])
    return res

A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
A = [5, 5, 5, 15]
print(solve(A))