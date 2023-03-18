from math import sqrt


class Solution:
    def __init__(self):
        self.count = 0

    def is_perfect_squar(self,A):
        return int(sqrt(A)) ** 2 == A

    def permutation(self, n, curr_ans, freq):

        if len(curr_ans) > 1:
            if not self.is_perfect_squar(curr_ans[-1] + curr_ans[-2]):
                return
        if len(curr_ans) == n:
            self.count += 1
            return

        for i in freq:
            if freq[i] > 0:
                freq[i] -= 1
                curr_ans.append(i)
                self.permutation(n, curr_ans, freq)
                curr_ans.pop()
                freq[i] += 1

    def solve(self,A):
        n = len(A)
        if n < 2:
            return 0
        freq = {}
        for i in range(n):
            freq[A[i]] = freq.get(A[i],0) +1
        self.permutation(n, [], freq)
        return self.count

A = [1, 17, 8]
# A = [2, 2, 2]
A = [ 41 ]
print(Solution().solve(A))
