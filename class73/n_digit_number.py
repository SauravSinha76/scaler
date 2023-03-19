import sys


class Solution:
    def __init__(self):
        self.ans =0
        sys.setrecursionlimit(10** 6)
    def numbers(self,A,B,num):

        if A == 0:
            if B == 0:
                print(num)
                self.ans += 1
            return
        for i in range(0,10):
            num.append(i)
            self.numbers(A-1,B-i,num)
            num.pop()

    def solve(self,A,B):
        num = []
        for i in range(1,10):
            num.append(i)
            self.numbers(A-1,B-i,num)
            num.pop()
        return self.ans

s = Solution()
print(s.solve(3,6))

