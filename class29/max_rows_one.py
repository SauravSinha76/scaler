def solve(A):
    n = len(A)
    m = len(A[0])
    idx = -1
    j = m - 1
    for i in range(n):
        while j > -1 and A[i][j] == 1:
            idx =i
            j -= 1


    return idx

A = [   [0, 1, 1],
         [0, 0, 1],
         [0, 1, 1]   ]

# A = [[0, 0, 0, 0],
#      [0, 1, 1, 1]]
print(solve(A))
