def solve(A):
    B = []
    for i in range(len(A) - 1, -1, -1):
        B.append(A[i])
    return B


A = (1, 2, 3, 4, 5)
print(solve(A))
