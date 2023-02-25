from class58.TreeNode import Node


class Solution:
    def __init__(self,B):
        self.k =B
        self.ans =0
    def inorder(self,root):
        # Base case
        if (root == None):
            return None

        # Search in left subtree
        left = self.inorder(root.left)

        # If k'th smallest is found in
        # left subtree, return it
        if (left != None):
            return left

        # If current element is k'th
        # smallest, return it
        self.k -= 1
        if (self.k == 0):
            return root

        # Else search in right subtree
        return self.inorder(root.right)

root = Node(3)
root.left = Node(2)
root.left.left= Node(1)

def solve(A,k):

    curr = A
    ans =[]

    while curr:

        if curr.left is None:
            ans.append(curr.val)
            curr = curr.right
        else:
            temp = curr.left
            while temp.right and temp.right != curr:
                temp = temp.right
            if temp.right is None:
                temp.right = curr
                curr = curr.left
            else:
                temp.right = None
                ans.append(curr.val)
                curr = curr.right
    return ans[k-1]
sal = Solution(1)
print(sal.inorder(root).val)
print(sal.ans)
print(solve(root,1))