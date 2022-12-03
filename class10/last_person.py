def solve(A):
    ans =0
    s=1
    while s <= A:
        ans = s
        s *= 2

    p_killed = A-ans

    return 2 * p_killed +1

print(solve(100))