def solve(A,B):
    res =[]
    n = len(A)
    for i in range(n):
        if A[i] % 2 == 0:
            A[i] = 1
        else:
            A[i] = 0
        if i>0:
            A[i] += A[i-1]

    for b in B:
        l = b[0]
        r = b[1]

        if l<1:
            res.append(A[r-1])
        else:
            res.append(A[r]-A[l-1])

    return res
A = [1, 2, 3, 4, 5]
B = [[0,2],[1,4]]
print(solve(A,B))