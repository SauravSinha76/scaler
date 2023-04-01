def tab_solve(A,B,C):
    dp = [[0 for _ in range(C + 1)]
          for _ in range(len(A) + 1)]
    for i in range(1,len(A)+1):
        for j in range(1,C+1):
            dp[i][j] = dp[i-1][j]
            if j - B[i - 1] >= 0:
                dp[i][j] = max(dp[i-1][j], A[i-1] + dp[i][j - B[i-1]])

    return dp[len(A)][C]

def solve(A,B,C):
    ans = 0
    max_capcity = max(A)

    dp = [0] * (max_capcity + 1)

    for i in range(1,max_capcity+1):
        minCost = 1 << 31
        for j in range(len(B)):
            if B[j] <= i:
                selected = C[j] + dp[i - B[j]]
                minCost = min(selected,minCost)
        dp[i] = minCost

    for a in A:
        ans += dp[a]
    return ans
A = [2, 4, 6]
B = [2, 1, 3]
C = [2, 5, 3]
# A = [2]
# B = [1]
# C = [2]
print(solve(A,B,C))