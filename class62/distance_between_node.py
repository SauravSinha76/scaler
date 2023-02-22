from class58.TreeNode import Node


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
    arr_A=[]
    path_from_root(A,B,arr_A)

    arr_B = []
    path_from_root(A,C,arr_B)
    arr_B.reverse()
    arr_A.reverse()

    i = 0
    j = 0

    while i < len(arr_A) and j < len(arr_B):
        if arr_A[i] == arr_B[j]:
            i += 1
            j += 1
        else:
            break

    dist_A =len(arr_A) - i
    dist_B = len(arr_B) - j

    return dist_A + dist_B


root = Node(5)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(4)
root.right = Node(8)
root.right.right = Node(11)
root.right.left = Node(6)

print(solve(root,2,5))

