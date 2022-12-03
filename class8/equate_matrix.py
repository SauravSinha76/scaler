def solve(A,B):
    row = len(A)
    column = len(A[0])

    for i in range(row):
        for j in range(column):
            if A[i][j] != B[i][j]:
                return 0
    return 1

# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# B = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[1, 2, 3],[7, 8, 9],[4, 5, 6]]
print(solve(A,B))