def solve(A):
    N = len(A)
    M = len(A[0])

    dp = [[0 for _ in range(M)]
           for _ in range(N)]
    if A[0][0] == 0:
        dp[0][0] =1
    for k in range(1,M):
        if A[0][k] == 0:
            dp[0][k] = dp[0][k-1]

    for k in range(1,N):
        if A[k][0] == 0:
            dp[k][0] = dp[k-1][0]

    for i in range(1,N):
        for j in range(1,M):
            if A[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[N-1][M-1]

A=[
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
]
A = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
     ]
A =[
  [1, 0]
]
A =[
  [0]
]

print(solve(A))