def solve(A,B):

    ans =0
    pow = 1

    while A > 0:
        r = A % 10
        A = int(A / 10)

        ans += r * pow
        pow *= B

    return ans

A = 22
B = 3
print(solve(A,B))
