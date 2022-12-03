def solve(A,B):
    ans = 1
    for _ in range(B):
        ans *=A
    return ans

print(solve(2,3))