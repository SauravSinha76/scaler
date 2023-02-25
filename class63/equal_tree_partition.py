import sys


class Solution:
    def __init__(self):
        self.hs =set()
        sys.setrecursionlimit(10001)
    def sum_tree(self,A):
        if A is None:
            return 0
        lsum = self.sum_tree(A.left)
        rsum = self.sum_tree(A.right)
        total = lsum + rsum + A.val
        self.hs.add(total)
        return total

    def solve(self,A):
        k = self.sum_tree(A)

        if k //2 in self.hs:
            return 1
        else:
            return 0