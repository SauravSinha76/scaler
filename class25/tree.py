import sys


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder_itrative(self,A):
        s = []
        ans =[]
        current = A
        while True:
            if current is not None:
                s.append(current)
                current = current.left
            elif len(s) != 0:
                current = s.pop()
                ans.append(current.val)
                current = current.right
            else:
                break
        return ans
    def preorder_itrative(self,A):
        s = []
        ans =[]
        current = A
        while True:
            if current is not None:
                s.append(current)
                ans.append(current.val)
                current = current.left
            elif len(s) != 0:
                current = s.pop()
                current = current.right
            else:
                break
        return ans
    def preorder(self,A):
        if A is None:
            return
        print(A.val,end=" ")
        self.preorder(A.left)
        self.preorder(A.right)


    def postorder(self,A):
        if A is None:
            return
        self.postorder(A.left)
        self.postorder(A.right)
        print(A.val, end=" ")

    def postorder_itrative(self, A):
        s = []
        ans = []
        current = A
        while True:
            if current is not None:
                s.append(current)
                s.append(current)
                current = current.left
            elif len(s) != 0:
                current = s.pop()
                if len(s) > 0 and current == s[-1]:
                    current = current.right
                else:
                    ans.append(current.val)
                    current = None
            else:
                break
        return ans


    def solve(self,A,max_val):
        if A is None:
            return 0
        if max_val < A.val:
            max_val = A.val
            return self.solve(A.left,max_val) + self.solve(A.right,max_val) +1
        return self.solve(A.left,max_val) + self.solve(A.right,max_val)

    def solve2(self,A,max_val):
        res = 0
        if A is None:
            return 0
        if max_val < A.val:
            max_val = A.val
            res += 1
        res += self.solve(A.left,max_val)
        res += self.solve(A.right,max_val)
        return res

    def isLeaf(self,node):
        if node is None:
            return False
        if node.left is None and node.right is None:
            return True
        return False

    # This function return sum of all left leaves in a
    # given binary tree
    def leftLeavesSum(self,root):

        # Initialize result
        res = 0

        # Update result if root is not None
        if root is not None:

            # If left of root is None, then add key of
            # left child
            if self.isLeaf(root.left):
                res += root.left.val
            else:
                # Else recur for left child of root
                res += self.leftLeavesSum(root.left)

            # Recur for right child of root and update res
            res += self.leftLeavesSum(root.right)
        return res

    def left_leave(self,A,total,isLeft):
        if A is None:
            return
        if A.left is None and A.right is None and isLeft:
            total += A.val

        self.left_leave(A.left,total,True)
        self.left_leave(A.right,total,False)

A = TreeNode(5)
A.left = TreeNode(3)
A.left.right = TreeNode(7)
A.left.left = TreeNode(6)
A.right = TreeNode(4)
A.right.left = TreeNode(8)
A.right.right = TreeNode(9)
s = Solution()
# print(s.inorder_itrative(A))
# print(s.preorder_itrative(A))
# print(s.preorder(A))
# print(s.postorder(A))
# print(s.postorder_itrative(A))
print(s.solve(A,-sys.maxsize))
print(s.solve2(A,-sys.maxsize))
print(s.leftLeavesSum(A))
# total =0
# s.left_leave(A,total,True)
# print(total)