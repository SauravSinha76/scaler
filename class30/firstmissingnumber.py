def solve(A):
    n = len(A)

    for i in range(n):
        while 1 <= A[i] <= n and A[i] != i+1:
            if A[i] == A[A[i] -1]:
                break
            val = A[i] -1
            tmp = A[i]
            A[i] = A[val]
            A[val] = tmp

    for i in range(n):
        if A[i] != i+1:
            return i+1
    return n+1

A =[1, 2, 0]
A = [3, 4, -1, 1]
A = [-8, -7, -6]
print(solve(A))