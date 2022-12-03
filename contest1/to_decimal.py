def solve(A,B):
    pow =1
    ans = 0
    for i in range(B):
        pow *= 2

    for i in range(A):
        ans += pow
        pow *= 2

    return ans

A = 2
B = 3
print(solve(A,B))