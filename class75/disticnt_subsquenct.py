class Solution:
    def __init__(self):
        self.count =0
        self.A = None
        self.B = None
        self.n = 0
    def solve_recursive(self,i,tmp):
        if i == self.n:
            if ''.join(tmp) == B:
                self.count += 1
            return
        self.solve_recursive(i + 1, tmp)
        tmp.append(A[i])
        self.solve_recursive(i+1,tmp)
        tmp.pop()

    def solve1(self,i,j):
        if j < 0:
            return 1
        if i < 0:
            return 0

        if A[i] == B[j]:
            return self.solve1(i-1, j-1) + self.solve1(i-1,j)
        else:
            return self.solve1(i-1, j)
    def solve_memo(self,i,j,dp):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if A[i-1] == B[j-1]:
            dp[i][j]= self.solve_memo(i - 1, j - 1,dp) + self.solve_memo(i - 1, j,dp)
        else:
            dp[i][j] =self.solve_memo(i - 1, j,dp)
        return dp[i][j]

    def memo_solve(self,A,B):
        self.A = A
        self.B = B

        dp=[[-1 for _ in range(len(B)+1)]
            for _ in range(len(A) + 1)]

        return self.solve_memo(len(A),len(B),dp)

    def tab_solve(self,A,B):
        n = len(A)
        m = len(B)

        dp = [[0 for _ in range(m + 1)]
              for _ in range(n + 1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]

    def solve(self,A,B):
        self.A = A
        self.B = B
        self.n = len(A)
        self.solve_recursive(0,[])


A = "rabbbit"
B = "rabbit"
S = Solution()
S.solve(A,B)
print(S.count)
print(S.solve1(len(A)-1,len(B)-1))
print(S.memo_solve(A,B))
print(S.tab_solve(A,B))