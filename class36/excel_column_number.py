def solve(A):
    n = len(A)
    pow = 1
    ans = 0
    for i in range(n-1,-1,-1):
         val = ord(A[i]) - (ord('A')-1)
         ans += val * pow
         pow *= 26
    return ans

print(solve("BB"))