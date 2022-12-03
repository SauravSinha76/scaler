def solve(A):
    row = len(A)
    column = len(A[0])

    a = []

    for i in range(column):
        r = []
        for j in range(row):
            r.append(A[j][i])
        a.append(r)
    return a

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# A = [[1, 2],[1, 2],[1, 2]]
print(A[0][0])
print(solve(A))