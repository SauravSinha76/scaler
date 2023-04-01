class Solution:
    def __init__(self,A):
        self.A = A
        self.n = len(A)
        self.max =0

    def checkPelindrom(self,A):
        start =0
        end = len(A)-1
        while start < end:
            if A[start] != A[end]:
                return False
            start += 1
            end -= 1
        return True
    def solve_recursive(self,i,j,A,B):
        if i< 0 or j < 0:
            return 0

        if A[i] == B[j]:
            return 1 + self.solve_recursive(i-1,j-1,A,B)
        else:
            return max(self.solve_recursive(i-1,j,A,B), self.solve_recursive(i,j-1,A,B))

    def solve_memo(self,i,j,A,B,dp):
        if i <0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if A[i] == B[j]:
            dp[i][j] = 1 + self.solve_memo(i-1,j-1,A,B,dp)
        else:
            dp[i][j] = max(self.solve_memo(i-1,j,A,B,dp),self.solve_memo(i,j-1,A,B,dp))
        return dp[i][j]

    def solve_tab(self,A,B):
        n = len(A)
        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][n]

    def solve(self,A):
        B = A[::-1]
        print(self.solve_recursive(len(A)-1,len(A)-1,A,B))
        n = len(A)
        dp = [[-1] * n for _ in range(n)]
        print(self.solve_memo(len(A)-1,len(B)-1,A,B,dp))
        print(self.solve_tab(A,B))


A = "bebeeed"
S = Solution(A)
S.solve(A)