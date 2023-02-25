from collections import deque


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def solve(self,A):
        queue = deque()
        prv = None
        queue.append(A)
        dummy = TreeLinkNode(-1)
        queue.append(dummy)
        while len(queue) > 1:
            n = queue.popleft()

            if n == dummy:
                queue.append(dummy)
            else:
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
                if prv and prv != dummy:
                    prv.next = n
            prv = n
        return A

root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.left.left = TreeLinkNode(3)
root.left.right = TreeLinkNode(4)
root.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

Solution().solve(root)