class Solution:
    def __init__(self):
        self.dp =[]

    def solve(self,A):
        if A <= 2:
            return A

        return self.solve(A-1) + self.solve(A-2)

    def memo_solve(self,A):
        if A <= 2:
            return A

        if self.dp[A] != -1:
            return self.dp[A]

        self.dp[A] = self.memo_solve(A-1) + self.memo_solve(A-2)

        return self.dp[A]

    def solve_m(self,A):
        self.dp = [-1] * (A+1)
        return self.memo_solve(A)


    def tab_solve(self,A):
        self.dp[1] = 1
        self.dp[2] = 2

        for i in range(3,A+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]

        return self.dp[A]

    def space_op_solve(self,A):
        dp_1 = 1
        dp_2 = 2
        ans = dp_2
        for i in range(3,A+1):
            ans = dp_2 + dp_1
            dp_1 = dp_2
            dp_2 = ans

        return ans % (10**9+7)



s = Solution()
print(s.solve(3))
print(s.solve_m(3))
print(s.tab_solve(3))
print(s.space_op_solve(3))
