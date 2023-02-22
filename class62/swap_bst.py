
class Solution:
    def __init__(self):
        self.prv = None
        self.first = None
        self.second = None

    def inorder(self,A):
        if A is None:
            return
        self.inorder(A.left)
        if self.prv and self.prv.val > A.val:
            if self.first is None:
                self.first = self.prv
            self.second = A

        self.prv = A
        self.inorder(A.right)

    def solve(self,A):
        self.inorder(A)
        return [self.first.val,self.second.val]


