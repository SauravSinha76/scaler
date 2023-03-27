def tab_solve(A,B,C):
    add = sum(A)
    dp = [float('inf')] * (add +1)

    dp[0] =0

    for i in range(1,len(A)+1):
        for j in range(add,-1,-1):
            if j - A[i - 1] >= 0 and dp[j- A[i-1]] != float('inf'):
                dp[j] = min(dp[j], B[i-1] + dp[j - A[i-1]])
    ans = 0
    for j in range(add , -1 ,-1):
        if dp[j] <= C:
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