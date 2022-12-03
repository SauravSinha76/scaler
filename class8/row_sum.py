def solve(A):
    row = len(A)
    column = len(A[0])
    res =[]
    for i in range(row):
        sum =0
        for j in range(column):
            sum += A[i][j]
        res.append(sum)
    return res

A =[
    [1,2,3,4],
    [5,6,7,8],
    [9,2,3,4]
]
print(solve(A))