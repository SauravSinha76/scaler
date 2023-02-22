from collections import deque

from class58.TreeNode import Node

class Pair:
    def __init__(self,node,level):
        self.node= node
        self.level = level

class Solution:

    ans =[]

    def is_leaf(self, node):

        if node.left is None and node.right is None:
            return True
        return False

    def left_view(self,node):
        curr = node.left
        while curr:
            if not self.is_leaf(curr):
                self.ans.append(curr.val)

            if curr.left:
                curr =curr.left
            else:
                curr= curr.right

    def bottom_leaf(self,node):

        if self.is_leaf(node):
            self.ans.append(node.val)

        if node.left:
            self.bottom_leaf(node.left)

        if node.right:
            self.bottom_leaf(node.right)

    def right_view(self,node):
        tmp =[]
        curr = node.right
        while curr:
            if not self.is_leaf(curr):
                tmp.append(curr.val)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        tmp.reverse()
        self.ans.extend(tmp)
    def solve(self,A):
        self.ans.append(A.val)
        self.left_view(A)
        self.bottom_leaf(A)
        self.right_view(A)
        return self.ans

root = Node(1)
root.left = Node(2)
root.right = Node(32)
root.left.left = Node(36)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(5)
root.right.right.right.right = Node(15)

print(Solution().solve(root))