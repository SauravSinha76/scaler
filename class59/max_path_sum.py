import sys

from class58.TreeNode import Node
class Solution:
    max_sum = - sys.maxsize

    def max_path_sum(self,A):
        if A is None:
            return 0
        l = max(0,self.max_path_sum(A.left))
        r = max(0,self.max_path_sum(A.right))

        self.max_sum = max(self.max_sum, l+r+A.val)
        return max(l , r) + A.val
    def solve(self,A):
        self.max_path_sum(A)
        return self.max_sum

root = Node(20)
root.left = Node(-10)
root.right = Node(20)
root.right.left = Node(-10)
root.right.right = Node(-50)
print(Solution().max_path_sum(root))