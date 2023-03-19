def solve(A,B,C,D):

    dp = [[ 0 for _ in range(len(A))]
           for _ in range(3)]

    dp[0][0] = A[0] * B
    dp[1][0] = dp[0][0] + A[0] * C
    dp[2][0] = dp[1][0] + A[0] * D

    for i in range(1,len(A)):
        dp[0][i] = max(A[i]*B,dp[0][i-1])
        dp[1][i] = max(dp[0][i] + A[i] * C, dp[1][i-1])
        dp[2][i] = max(dp[1][i] + A[i] * D, dp[2][i-1])

    return dp[2][len(A)-1]

A = [1, 5, -3, 4, -2]
B = 2
C = 1
D = -1

A = [3, 2, 1]
B = 1
C = -10
D = 3
print(solve(A,B,C,D))
