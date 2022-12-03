def solve(A,B):
    row = len(A)
    column = len(A[0])

    for i in range(row):
        for j in range(column):
            A[i][j] *= B
    return A

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = 2
print(solve(A,B))