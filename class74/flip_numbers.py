def solve_memo(A,B,idx,weight,dp):
    if idx ==0 or weight ==0:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    if B[idx-1] <= weight:
        dp[idx][weight] = max(A[idx-1] +solve_memo(A,B,idx-1, weight- B[idx-1],dp), solve_memo(A,B,idx-1, weight,dp))
    else:
        dp[idx][weight] = solve_memo(A,B,idx-1,weight,dp)
    return dp[idx][weight]
def mem_solve(A,B,C):
    dp =[[-1 for _ in range(C+1)]
         for _ in range(len(A)+1)]
    return solve_memo(A,B,len(A), C , dp)

def tab_solve(A,C):
    n = len(A)
    dp = [[n+1 for _ in range(C + 1)]
          for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] =0

    for i in range(1,n+1):
        for j in range(1,C+1):
            if j - A[i - 1] >= 0:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i-1][j - A[i-1]])
            else:
                dp[i][j] = dp[i - 1][j]
    for i in range(C, -1, -1):
        if dp[n][i] < n:
            return dp[n][i]


def solve(A,idx,weight):
    if idx ==0 or weight ==0:
        return 0

    if A[idx-1] <= weight:
        return min(1 + solve(A,idx-1, weight- A[idx-1]), solve(A,idx-1, weight))
    return solve(A,idx-1,weight)

A = [15, 10, 6]
A = [14, 10, 4]
A = [ 8, 4, 5, 7, 6, 2 ]
C = sum(A)// 2
# A = [10, 20, 30, 40]
# B = [12, 13, 15, 19]
# C = 10
# print(solve(A,len(A),C))
# print(mem_solve(A,B,C))
print(tab_solve(A,C))