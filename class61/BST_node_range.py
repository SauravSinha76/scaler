from class58.TreeNode import Node


def inorder(A,arr):
    if A is None:
        return
    inorder(A.left,arr)
    arr.append(A.val)
    inorder(A.right,arr)


def solve(A,B,C):
    arr =[]
    inorder(A,arr)

    n = len(arr)
    first = -1
    second = n

    for i in range(n):
        if arr[i] >= B:
            i +=1
            break
    for j in range(n):
        if first == -1:
            return 0
        if arr[j] > C:
            j -=1
            break
    return second - first

root = Node(6)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(5)
# root.left.left.left = Node(8)
# root.right.right = Node(27)
# root.right.left = Node(16)

print(solve(root,7,18))