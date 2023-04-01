def solve(A):
    A.sort(key= lambda x : x[0])
    n = len(A)
    dp = [0] * n
    dp[0] = 1
    ans = 1
    for i in range(1, n):
        max_so_far = 0
        for j in range(i):
            if A[j][0] != A[i][0] and A[j][1] < A[i][1]:
                max_so_far = max(max_so_far, dp[j])
        dp[i] = 1 + max_so_far
        ans = max(ans, dp[i])
    return ans

A = [
         [5, 4],
         [6, 4],
         [6, 7],
         [2, 3]
     ]

print(solve(A))