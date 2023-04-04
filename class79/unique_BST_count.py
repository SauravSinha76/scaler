def solve(A):

    dp = [0] * (A+1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2,A+1):
        val = 0
        for j in range(i):
            val += dp[j] * dp[i - 1 -j]
        dp[i] = val
    return dp[A]

A = 4
print(solve(A))