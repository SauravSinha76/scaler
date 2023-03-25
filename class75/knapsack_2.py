def tab_solve(A,B,C):
    add = sum(A)
    dp = [[0 for _ in range(add + 1)]
          for _ in range(len(A) + 1)]
    for j in range(1,add+1):
        dp[0][j] = 1 << 31

    for i in range(1,len(A)+1):
        for j in range(1,add+1):
            dp[i][j] = dp[i-1][j]
            if j - A[i - 1] >= 0:
                dp[i][j] = min(dp[i-1][j], B[i-1] + dp[i-1][j - A[i-1]])
    ans = 0
    for j in range(add , -1 ,-1):
        if dp[-1][j] <= C:
            ans = j
            break
    return ans

A = [6, 10, 12]
B = [10, 20, 30]
C = 50
# A = [ 8, 5 ]
# B = [ 1, 20 ]
# C = 17
# A = [ 6, 1, 3, 9, 7, 1, 3, 5, 9, 7, 6, 1, 10, 1, 1, 7, 2 ]
# B = [ 44, 49, 30, 24, 35, 5, 7, 41, 17, 27, 32, 9, 45, 40, 27, 24, 38 ]
# C = 297
print(tab_solve(A,B,C))