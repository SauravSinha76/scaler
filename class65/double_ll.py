import sys

from class58.TreeNode import Node

class Solution:
    def __init__(self):
        sys.setrecursionlimit(10000)
        self.prev = None
        self.head = None
    def BinaryTree2DoubleLinkedList(self,root):
        # Base case
        if (root == None):
            return

        # Recursively convert left subtree
        self.BinaryTree2DoubleLinkedList(root.left)


        if (self.prev == None):
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root

        # Finally convert right subtree
        self.BinaryTree2DoubleLinkedList(root.right)

root = Node(1)
root.left = Node(6)
root.right = Node(2)
root.right.left = Node(3)
print(solve(root))