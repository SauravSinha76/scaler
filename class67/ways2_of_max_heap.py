import math
import sys

sys.setrecursionlimit(106)


class Solution:
    MOD = 109 + 7

    def init(self):
        self.dp = [-1] * 1005
        self.dp2 = [-1] * 1005
        self.log = [-1] * 1005
        self.nCk = [[-1] * 1005 for _ in range(1005)]

    def solve(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        A.sort()
        min_repeating = A[0] == A[1]
        if min_repeating:
            return (self.number_of_ways2(n) + self.MOD) % self.MOD
        return (self.number_of_ways(n) + self.MOD) % self.MOD

    def number_of_ways2(self, n):
        if n == 0:
            return 0
        if n <= 3:
            return 1
        if self.dp2[n] != -1:
            return self.dp2[n]
        height = self.log2(n)
        nodes = (1 << height) - 1
        left = ((nodes - 1) // 2) + min(n - nodes, (nodes + 1) // 2)
        right = n - left - 1
        ans = (self.compute(n - 3, left - 2) * self.number_of_ways2(left) * self.number_of_ways(right)) % self.MOD
        ans += (self.compute(n - 3, right - 2) * self.number_of_ways(left) * self.number_of_ways2(right)) % self.MOD
        ans += (self.compute(n - 3, left - 1) * self.number_of_ways(left) * self.number_of_ways(right)) % self.MOD
        self.dp2[n] = ans % self.MOD
        return self.dp2[n]

    def number_of_ways(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if self.dp[n] != -1:
            return self.dp[n]
        height = self.log2(n)
        nodes = (1 << height) - 1
        left = ((nodes - 1) // 2) + min(n - nodes, (nodes + 1) // 2)
        right = n - left - 1
        self.dp[n] = (self.compute(n - 1, left) * self.number_of_ways(left) * self.number_of_ways(right)) % self.MOD
        return self.dp[n]

    def compute(self, n, k):
        if k < 0 or k > n:
            return 0
        if n <= 1 or k == 0:
            return 1
        if self.nCk[n][k] != -1:
            return self.nCk[n][k]
        answer = (self.compute(n - 1, k - 1) + self.compute(n - 1, k)) % self.MOD
        self.nCk[n][k] = answer
        return answer

    def log2(self, n):
        if self.log[n] != -1:
            return self.log[n]
        self.log[n] = int(math.log2(n) + 1e-10)
        return self.log[n]