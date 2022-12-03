def solve(A):
    n = len(A)
    res =[]
    for i in range(n):
        for j in range(i,n):
            sub =[]
            for k in range(i,j+1):
                sub.append(A[k])
            res.append(sub)
    return res

A = [1, 2, 3]
print(solve(A))