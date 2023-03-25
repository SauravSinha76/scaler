def tab_solve(A,B,C):
    dp = [[0 for _ in range(C + 1)]
          for _ in range(len(A) + 1)]

    for i in range(1,len(A)+1):
        for j in range(1,C+1):
            dp[i][j] = dp[i-1][j]
            if j - B[i - 1] >= 0:
                dp[i][j] = max(dp[i-1][j], A[i-1] + dp[i][j - B[i-1]])

    return dp[len(A)][C]


def solve(A,B,C,D):
    n = len(A)
    for i in range(n):
        A[i] = A[i] * B[i]
    return tab_solve(A,C,D)

A = [1, 2, 3]
B = [2, 2, 10]
C = [2, 3, 9]
D = 8
A = [2]
B = [5]
C = [10]
D = 99
print(solve(A,B,C,D))