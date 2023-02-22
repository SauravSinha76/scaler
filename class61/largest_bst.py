import sys

from class58.TreeNode import Node


class Triplet:
    def __init__(self,bst=False,min=-sys.maxsize,max=sys.maxsize,length =0):
        self.bst = bst
        self.min = min
        self.max = max
        self.length = length

    def __str__(self):
        return f"bst = {self.bst}, min = {self.min}, max = {self.max}, length = {self.length}"

def isBst(A):
    if A is None:
        return Triplet(True,sys.maxsize,-sys.maxsize)

    l = isBst(A.left)
    r = isBst(A.right)
    mt =Triplet()
    if l.bst and r.bst and  l.max < A.val and A.val < r.min:
        mt.bst = True
        mt.length = 1 + l.length + r.length
    else:
        mt.length = max(r.length,l.length)
    mt.min = min(A.val,l.min,r.min)
    mt.max = max(A.val,l.max, r.max)
    return mt

root = Node(9)
root.left = Node(20)
root.right = Node(14)
root.left.left = Node(12)
root.left.right = Node(11)
# root.right.right = Node(20)
print(isBst(root))