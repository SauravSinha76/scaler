def solve(A,B):
    n = len(A)
    res = []
    for i in range(1,n):
        if i % 2 != 0:
            A[i] = A[i-1]
        else:
            A[i] += A[i-1]

    b_len = len(B)
    for i in range(b_len):
        l = B[i][0]
        r = B[i][1]

        if l == 0:
            res.append(A[r])
        else:
            res.append(A[r] - A[l-1])
    return res

# A = [1, 2, 3, 4, 5]
# B = [   [0,2],
#         [1,4]   ]

A = [2, 1, 8, 3, 9]
B = [   [0,3] ,
        [2,4]   ]
print(solve(A,B))
print(-40%9)