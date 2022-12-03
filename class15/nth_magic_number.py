def solve(A):
    ans = 0
    pow =5
    while A > 0:
        if A & 1:
          ans += pow
        pow *= 5
        A = A >> 1
    return ans

print(solve(10))