class Solution:
    def __init__(self):
        self.A = None
        self.B = None

    def solve_rec(self,i,j):
        if i == -1 or j == -1:
            return 0

        if self.A[i] == self.B[j]:
            return 1 + self.solve_rec(i-1,j-1)
        else:
            return max(self.solve_rec(i-1,j), self.solve_rec(i,j-1))

    def solve_memo(self,i,j,dp):
        if i == -1 or j == -1:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if self.A[i] == self.B[j]:
            dp[i][j] = 1 + self.solve_rec(i-1,j-1)
        else:
            dp[i][j] = max(self.solve_rec(i-1,j), self.solve_rec(i,j-1))

        return dp[i][j]

    def memo_solve(self,A,B):
        self.A = A
        self.B = B
        dp =[[-1 for _ in range(len(B)+1)]
             for _ in range(len(A)+1)]
        return self.solve_memo(len(A)-1,len(B)-1,dp)

    def tab_solve(self,A,B):
        n = len(A)
        m = len(B)

        dp =[[0 for _ in range(m+1)]
             for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

    def solve(self,A,B):
        self.A = A
        self.B = B
        return self.solve_rec(len(A)-1, len(B)-1)


A = "abbcdgf"
B = "bbadcgf"

# A = "aaaaaa"
# B = "ababab"
S = Solution()
print(S.solve(A,B))
print(S.memo_solve(A,B))
print(S.tab_solve(A,B))
