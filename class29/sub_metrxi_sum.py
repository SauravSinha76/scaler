def solve(A,B,C,D,E):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(1,m):
            A[i][j] += A[i][j-1]
    for i in range(1,n):
        for j in range(m):
            A[i][j] += A[i-1][j]
    res =[]
    for i in range(len(B)):
        sum = A[D[i]-1][E[i]-1]
        if C[i] > 1:
            sum -= A[D[i]-1][C[i]-2]
        if B[i] > 1:
            sum -= A[B[i]-2][E[i]-1]
        if B[i] > 1 and C[i] > 1:
            sum += A[B[i]-2][C[i]-2]
        res.append(sum)

    return res

A = [   [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]   ]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]

print(solve(A,B,C,D,E))
