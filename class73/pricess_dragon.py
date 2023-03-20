def solve(A):
    N = len(A)
    M = len(A[0])
    dp = [[0 for _ in range(M)]
          for _ in range(N)]

    dp[N-1][M-1] = max(1, 1 - A[N-1][M-1])

    for j in range(M-2,-1,-1):
        dp[N-1][j] = max(1, dp[N-1][j+1] - A[N-1][j])

    for i in range(N-2,-1,-1):
        dp[i][M-1] = max(1, dp[i+1][M-1] - A[i][M-1])


    for i in range(N-2,-1,-1):
        for j in range(M-2,-1,-1):
            dp[i][j] = max(1,min(dp[i+1][j], dp[i][j+1]) - A[i][j])

    return dp[0][0]

A = [
       [-2, -3, 3],
       [-5, -10, 1],
       [10, 30, -5]
     ]
# A = [
#     [1, -1, 0],
#     [-1, 1, -1],
#     [1, 0, -1]
# ]
print(solve(A))
