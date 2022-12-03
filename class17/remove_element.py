def solve(A):
    A.sort(reverse=True)
    n = len(A)
    ans = 0
    for i in range(n):
        ans += A[i]*(i+1)
    return ans

A = [2, 1,4]
print(solve(A))