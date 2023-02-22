from class58.TreeNode import Node


def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right,arr)

def solve(A):
    tmp = A
    arr = []
    inorder(tmp,arr)

    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return 0
    return 1

def isBST(root,l,r):
    if root is None:
        return True
    if root.val >= l and root.val <= r:
        x = isBST(root.left, l, root.val -1)
        y = isBST(root.right, root.val + 1, r)
        return x and y
    return False

def solve1(A):
    l = - (1 << 31)
    r = (1 << 31) -1
    res = isBST(A,l,r)
    if res:
        return 1
    else:
        return 0

root = Node(2)
root.left = Node(1)
root.right = Node(3)

print(solve(root))
print(solve1(root))

