from class58.TreeNode import Node


def build_tree(B,start,end,pos,hm):
    if start > end:
        return
    root = Node(B[pos])
    idx = hm[B[pos]]
    root.left = build_tree(B,start,idx -1,idx -1,hm)
    root.right = build_tree(B,idx+1,end,pos-1,hm)
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)

def solve(A,B):
    hm ={}
    n1 = len(A)
    n2 = len(B)
    for i in range(n1):
        hm[A[i]] = i

    root = build_tree(B,0,n1-1,n1-1,hm)
    return root
A = [2, 1, 3]
B = [2, 3, 1]
A = [6, 1, 3, 2]
B = [6, 3, 2, 1]
root = solve(A,B)
inorder(root)

