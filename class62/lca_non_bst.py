from class58.TreeNode import Node


def search(A,k):
    if A is None:
        return False
    if A.val == k:
        return True
    return search(A.left,k) or search(A.right,k)

def path_from_root(A,k,path):
    if A is None:
        return False
    if A.val ==k:
        path.append(A.val)
        return True
    res = path_from_root(A.left,k,path) or path_from_root(A.right,k,path)
    if res:
        path.append(A.val)
    return res

def solve(A,B,C):
    path_B =[]
    path_C =[]
    path_from_root(A,B,path_B)
    path_from_root(A,C,path_C)
    path_C.reverse()
    path_B.reverse()
    n = min(len(path_B),len(path_C))
    prv = -1
    for i in range(n):
        if path_C[i] != path_B[i]:
            return prv
        prv = path_B[i]
    return prv

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.left = Node(7)
print(search(root,56))
print(solve(root,4,5))