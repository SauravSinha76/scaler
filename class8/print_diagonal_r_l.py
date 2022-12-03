def solve(A):
    n = len(A)
    res = []

    for i in range(n):
        r =[0 for _ in range(n)]
        row = 0
        column = i
        k =0
        while row < n and column > -1:
            r[k]=A[row][column]
            row += 1
            column -= 1
            k += 1
        res.append(r)
    for i in range(1,n):
        r =[0 for _ in range(n)]
        row = i
        column = n-1
        k = 0
        while row < n and column > -1:
            r[k] = A[row][column]
            row += 1
            column -= 1
            k += 1
        res.append(r)
    return res


def solve2(A):
    n = len(A)
    res = []

    for i in range(n-1,-1,-1):
        r =[0 for _ in range(n)]
        row = i
        column = 0
        k =0
        while row < n and column < n:
            r[k]= A[row][column]
            row += 1
            column += 1
            k += 1
        res.append(r)
    for i in range(1,n):
        r =[0 for _ in range(n)]
        row = 0
        column = i
        k = 0
        while row < n and column < n:
            r[k] = A[row][column]
            row += 1
            column += 1
            k += 1
        res.append(r)
    return res

A=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(solve(A))
print(solve2(A))