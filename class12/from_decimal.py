def solve(A,B):
    ans = 0
    pow = 1
    while A > 0:
        r = A % B
        A = A//B

        ans += r*pow
        pow *= 10

    return ans

A = 4
B = 3
print(solve(A,B))