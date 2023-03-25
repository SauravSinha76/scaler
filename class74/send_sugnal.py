def solve_memo(A,prv_state,dp):
    if A == 0:
        return 1

    if dp[A][prv_state] != -1:
        return dp[A][prv_state]

    if prv_state == 1:
        dp[A][prv_state] = solve_resur(A-1,0)
    else:
        dp[A][prv_state] = solve_resur(A-1,1) + solve_resur(A-1, 0)
    return dp[A][prv_state]

def solve_tab(A):
    dp = [[0 for _ in range(2)]
          for _ in range(A + 1)]

    dp[0][0] = 1
    for i in range(1,A+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]
    return dp[A][0] + dp[A][1]
def solve_resur(A,prv_state):
    if A == 0:
        return 1

    if prv_state == 1:
        return solve_resur(A-1,0)
    else:
        return solve_resur(A-1,1) + solve_resur(A-1, 0)

def solve(A):
    return solve_resur(A,0)

def memo_solve(A):
    dp = [[-1 for _ in range(1)]
          for _ in range(A+1)]

    return solve_memo(A,0,dp)

print(solve(3))
print(memo_solve(3))
print(solve_tab(3))
