def solve(A):
    n = len(A)
    dp =[0] * n
    dp[0] = 1
    ans = 1
    for i in range(1,n):
        max_so_far = 0
        for j in range(i):
            if A[j] < A[i]:
                max_so_far = max(max_so_far,dp[j])
        dp[i] = 1 + max_so_far
        ans = max(ans,dp[i])
    return ans
A = [1, 2, 1, 5]
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(solve(A))