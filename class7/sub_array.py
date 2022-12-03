def solve(A,B,C):
    res = []
    for i in range(B,C+1):
        res.append(A[i])
    return res

# A = [4, 3, 2, 6]
# B = 1
# C = 3
A = [4, 2, 2]
B = 0
C = 1
print(solve(A,B,C))