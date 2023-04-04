def solve(A,i,j):
    if i == j:
        return 0

    cost = float('inf')

    for k in range(i,j):
        cost = min(cost,solve(A,i,k)+solve(A,k+1,j) +A[i-1]*A[k]*A[j])

    return cost



def memo_solev(A):
    n = len(A)

    dp =[[-1] * (n) for _ in range(n)]

    def solve_memo(A, i, j, dp):
        if i == j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        cost = float('inf')

        for k in range(i, j):
            cost = min(cost, solve_memo(A, i, k, dp) + solve_memo(A, k + 1, j, dp) + A[i - 1] * A[k] * A[j])

        dp[i][j] = cost
        return dp[i][j]
    return solve_memo(A,1,n-1,dp)

def solve_tab(A):

    n = len(A)

    dp =[[float('inf')] * n for _ in range(n)]

    for i in range(n,0,-1):
        for j in range(i,n):
            if i ==j:
                dp[i][j] = 0
                continue
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k]+ dp[k+1][j]+ A[i-1]*A[k]*A[j])
    return dp[1][n-1]
A = [40, 20, 30, 10, 30]
print(solve(A,1,len(A)-1))
print(memo_solev(A))
print(solve_tab(A))