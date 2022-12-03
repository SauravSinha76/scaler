def solve(A):
    ans = 0
    pow = 1 << 31
    while A > 0:
        if A & 1:
           ans += pow
        A = A >> 1
        pow = pow >> 1
    return ans
print(bin(4))
print(bin(solve(4)))