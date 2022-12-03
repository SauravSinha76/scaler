def solve(A):
    A.sort()
    diff = A[1]- A[0]
    n = len(A)
    for i in range(2,n):
        if A[i] - A[i-1] != diff:
            return 0
    return 1

A = [3, 5, 1]
A = [2, 4, 1]
print(solve(A))