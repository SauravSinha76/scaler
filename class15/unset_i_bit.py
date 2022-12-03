def solve(A,B):
    if A >> B & 1:
        return A ^ (1 << B)
    else:
        return A

print(solve(5,2))
