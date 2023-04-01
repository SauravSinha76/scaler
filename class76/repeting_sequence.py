
def solve(A):
    n = len(A)
    def lsc(i,j,dp):
        if i == len(A) or j == len(A):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if i != j and A[i] == A[j]:
            dp[i][j] = 1 + lsc(i+1,j+1,dp)
        else:
            dp[i][j] = max(lsc(i+1,j,dp), lsc(i,j+1,dp))
        return dp[i][j]
    dp = [[-1 for _ in range(n+1)]
          for _ in range(n+1)]
    return 1 if lsc(0,0,dp) > 1 else 0

A = "abba"
print(solve(A))