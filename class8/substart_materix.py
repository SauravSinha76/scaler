def solve(A,B):
    row = len(A)
    column = len(A[0])
    res = [[0 for column in range(column)]
           for row in range(row)]
    for i in range(row):
        for j in range(column):
            res[i][j] = A[i][j] - B[i][j]
    return res

A = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print(solve(A,B))