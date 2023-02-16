from class58.TreeNode import Node

import sys
sys.setrecursionlimit(10000)
def build_tree(A,start,end,pos,hm):
    if start > end:
        return
    root = Node(A[pos])
    idx = hm[A[pos]]
    root.left = build_tree(A,start,idx -1,pos +1,hm)
    root.right = build_tree(A,idx+1,end,pos + (idx -start) +1,hm)
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)

def solve(A,B):
    hm ={}
    n1 = len(B)
    for i in range(n1):
        hm[B[i]] = i

    root = build_tree(A,0,n1-1,0,hm)
    return root

import sys
sys.setrecursionlimit(10000)
A = [1, 2, 3]
B = [2, 1, 3]
A = [1, 6, 2, 3]
B = [6, 1, 3, 2]
# A = [ 2, 1, 6, 5, 3, 4 ]
# B = [ 5, 6, 1, 2, 3, 4 ]
# A = [ 1, 2, 3, 4, 5 ]
# B = [ 3, 2, 4, 1, 5 ]
root = solve(A,B)
inorder(root)
