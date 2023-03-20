import sys


class Solution:
    def numbers(self,A,B,dp):
        if B < 0:
            return 0
        if A == 0 and B == 0:
            return 1
        if A == 0:
            return 0

        if dp[A][B] != -1:
            return dp[A][B]
        ans = 0
        for i in range(0,10):
            ans += self.numbers(A-1,B-i,dp)

        dp[A][B] = ans
        return ans

    # def tab(self,A,B,dp):

    def solve(self,A,B):
        dp =[[-1 for _ in range(B+1)]
             for _ in range(A+1)]
        ans = 0
        for i in range(1,10):
            ans += self.numbers(A-1,B-i,dp)
        dp[A][B] = ans
        return ans

s = Solution()
print(s.solve(3,6))

