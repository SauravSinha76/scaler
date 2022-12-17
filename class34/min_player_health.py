def gcd(a,b):
    if b == 0:
        return a
    return gcd(b , a % b)

def solve(A):
    n = len(A)
    ans = A[0]
    for i in range(1,n):
        if ans != 1:
            ans = gcd(ans,A[i])
    return ans

A = [2, 3, 4]
# A = [6, 4]
print(solve(A))