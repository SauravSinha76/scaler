from class58.TreeNode import Node


def build_tree(B,pstart,pend,iend,hm):
    if pstart > pend:
        return
    root = Node(B[pend])
    idx = hm[B[pend]]
    l = iend - idx
    root.left = build_tree(B,pstart,pend-l-1,idx-1,hm)
    root.right = build_tree(B,pend - l,pend-1,iend,hm)
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

