def solve(A):
    n = len(A)
    m = len(A[0])
    for j in range(1,m):
        A[0][j] += A[0][j-1]

    for i in range(1,n):
        A[i][0] += A[i-1][0]

    for i in range(1,n):
        for j in range(1,m):
            A[i][j] += min(A[i-1][j], A[i][j-1])

    return A[n-1][m-1]

A = [
       [1, 3, 2],
       [4, 3, 1],
       [5, 6, 1]
     ]
A = [
       [1, -3, 2],
       [2, 5, 10],
       [5, -5, 1]
     ]
print(solve(A))

