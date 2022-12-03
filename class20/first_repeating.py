def solve(A):
    d = {}
    for i in range(len(A)):
        if A[i] not in d:
            d[A[i]] = 1
        else:
            d[A[i]] += 1

    for i in range(len(A)):
        if d[A[i]] > 1:
            return A[i]
    return -1

A = [10, 5, 3, 4, 3, 5, 6]
A = [6, 10, 5, 4, 9, 120]
print(solve(A))
