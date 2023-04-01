class Solution:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def solve(self, i, j):
        if i < 0 and j < 0:
            return 1
        elif i < 0 :
            while j > -1:
                if B[j] != '*':
                    return 0
                j -= 1
            return 1
        elif i < 0 or j < 0:
            return 0

        if self.A[i] == self.B[j] or self.B[j] == '.':
            return self.solve(i - 1, j - 1)
        elif self.B[j] == "*" and self.B[j-1] == self.A[i] or self.B[j-1] == '.':
            return self.solve(i, j - 2) or self.solve(i - 1, j)
        elif self.B[j] =="*" and self.B[j-1] != self.A[i]:
            return self.solve(i, j-2)
        else:
            return 0

    def solve_memo(self,i,j,dp):
        if i < 0 and j < 0:
            return 1
        elif i < 0 and self.B[j] == '*':
            return 1
        elif i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if self.A[i-1] == self.B[j-1] or self.B[j-1] == '?':
            dp[i][j] = self.solve_memo(i - 1, j - 1,dp)
        elif self.B[j-1] == "*":
            dp[i][j] = self.solve_memo(i, j - 1,dp) or self.solve_memo(i - 1, j,dp)
        else:
            dp[i][j] = 0

        return dp[i][j]

    def memo_solve(self):
        n = len(self.A)
        m = len(self.B)
        dp = [[-1 for _ in range(m+1)]
              for _ in range(n+1)]
        dp[0][0] = 1
        return self.solve_memo(n,m,dp)

    def tab_solve(self):
        n = len(self.A)
        m = len(self.B)
        dp = [[0 for _ in range(m + 1)]
              for _ in range(n + 1)]
        dp[0][0] = 1
        for j in range(1, m + 1):
            if B[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if self.A[i - 1] == self.B[j - 1] or self.B[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif self.B[j - 1] == "*" and (self.B[j-2] == self.A[i-1] or self.B[j-2] == '.'):
                    dp[i][j] = dp[i - 1][j] or dp[i][j-2]
                elif self.B[j - 1] == "*" and self.B[j-2] != self.A[i-1]:
                    dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = 0
        return dp[n][m]
A = "aab"
B = "c*a*b"
A = "acz"
B = "a.a"
A = "baaaaaabaaaabaaaaababababbaab"
B = "..a*aa*a.aba*a*bab*"
S = Solution(A, B)
print(S.solve(len(A) - 1, len(B) - 1))
# print(S.memo_solve())
print(S.tab_solve())
