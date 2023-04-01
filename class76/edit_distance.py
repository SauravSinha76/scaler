class Solution:
    def __init__(self,A,B):
        self.A = A
        self.B = B

    def solve(self,n,m):
        if n <0 and m < 0:
            return 0
        if n < 0:
            return m +1
        if m < 0:
            return n+1

        if self.A[n] == self.B[m]:
            return self.solve(n-1,m-1)
        else:
            return 1 + min(self.solve(n,m-1), self.solve(n-1,m), self.solve(n-1,m-1))

    def solve_memo(self,i,j,dp):
        if i <0 and j < 0:
            return 0
        if i < 0:
            return j +1
        if j < 0:
            return i+1
        if dp[i][j] != -1:
            return dp[i][j]

        if self.A[i-1] == self.B[j-1]:
            dp[i][j] = self.solve(i-1,j-1)
        else:
            dp[i][j] = 1 + min(self.solve_memo(i,j-1,dp), self.solve_memo(i-1,j,dp), self.solve_memo(i-1,j-1,dp))
        return dp[i][j]

    def solve_tab(self):
        n = len(self.A)
        m = len(self.B)
        dp =[[0 for _ in range(m+1)]
             for _ in range(n+1)]

        for i in range(1,n+1):
            dp[i][0] = 1*i
        for j in range(1,m+1):
            dp[0][j] = 1 *j

        for i in range(1,n+1):
            for j in range(1,m+1):
                if self.A[i-1] == self.B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[n][m]

    def memo_solve(self):
        n = len(self.A)
        m = len(self.B)
        dp = [[-1 for _ in range(m+1)]
              for _ in range(n+1)]
        return self.solve_memo(n,m,dp)
A = "abad"
B = "abac"
A = "Anshuman"
B = "Antihuman"
S = Solution(A,B)
print(S.solve(len(A)-1,len(B)-1))
print(S.memo_solve())
print(S.solve_tab())