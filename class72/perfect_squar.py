def solve(A):
    dp = [-1] * (A+1)

    dp[0] =0

    for i in range(1, A+1):

        ans = 1 << 31

        x = 1
        while x*x <= i:
            ans = min(ans, dp[i - x * x])
            x += 1
        dp[i] = ans + 1

    return dp[A]

print(solve(12))
