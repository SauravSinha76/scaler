def solve_memo(A,B,idx,weight,dp):
    if idx ==0 or weight ==0:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    if B[idx-1] <= weight:
        dp[idx][weight] = max(A[idx-1] +solve_memo(A,B,idx, weight- B[idx-1],dp), solve_memo(A,B,idx-1, weight,dp))
    else:
        dp[idx][weight] = solve_memo(A,B,idx-1,weight,dp)
    return dp[idx][weight]
def mem_solve(A,B,C):
    dp =[[-1 for _ in range(C+1)]
         for _ in range(len(A)+1)]
    return solve_memo(A,B,len(A), C , dp)

def tab_solve(A,B,C):
    dp = [[0 for _ in range(C + 1)]
          for _ in range(len(A) + 1)]

    for i in range(1,len(A)+1):
        for j in range(1,C+1):
            dp[i][j] = dp[i-1][j]
            if j - B[i - 1] >= 0:
                dp[i][j] = max(dp[i-1][j], A[i-1] + dp[i][j - B[i-1]])

    return dp[len(A)][C]


def solve(A,B,idx,weight):
    if idx ==0 or weight ==0:
        return 0

    if B[idx-1] <= weight:
        return max(A[idx-1] + solve(A,B,idx, weight- B[idx-1]), solve(A,B,idx-1, weight))
    return solve(A,B,idx-1,weight)

A = 10
B = [6, 7]
C = [5, 5]
# A = [10, 20, 30, 40]
# B = [12, 13, 15, 19]
# C = 10
print(solve(B,C,len(B),A))
print(mem_solve(B,C,A))
print(tab_solve(B,C,A))