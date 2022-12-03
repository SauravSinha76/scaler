def solve(A,B):
    return A ^ (1 << B)

print(solve(5,2))