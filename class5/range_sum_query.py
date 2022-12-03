def solve(A,B):
    res =[]
    n = len(A)
    for i in range(1,n):
        A[i] += A[i-1]
    for b in B:
        l = b[0]
        r = b[1]

        if l <2:
           res.append(A[r-1])
        else:
            res.append(A[r-1] -A[l-2])
    return res

# A = [1, 2, 3, 4, 5]
# B = [[1, 4], [2, 3]]
A = [2, 2, 2]
B = [[1, 1], [2, 3]]
print(solve(A,B))