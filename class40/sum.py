def solve(A):
    A.sort()

    n = len(A)

    ans =0

    for i in range(n):
        ans += A[i] * ((1 << i) - (1 << (n-i-1)))

    return ans

A =[1]
print(solve(A))