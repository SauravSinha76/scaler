def solve(A,B):
    res = []
    for b in B:
        total =0
        l = b[0]
        r = b[1]
        while l<=r:
            total +=A[l-1]
            l +=1
        res.append(total)
    return res

# A = [1, 2, 3, 4, 5]
# B = [[1, 4], [2, 3]]
A = [2, 2, 2]
B = [[1, 1], [2, 3]]
print(solve(A,B))