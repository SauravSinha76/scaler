def solve(A):
    ans = ""
    while A > 0:
        r = A % 26
        A = A // 26
        if r == 0:
            r = 26
            A = A-1
        ans= chr(ord('A')-1+r)+ans
    return ans
print(solve(943566))