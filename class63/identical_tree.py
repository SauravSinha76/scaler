from class58.TreeNode import Node


def check(A,B):
    if not A and not B:
        return True
    if not A or not B:
        return False

    if A.val != B.val:
        return False

    left = check(A.left, B.left)
    right = check(A.right, B.right)

    if left and right:
        return 1
    return 0

A = Node(1)
A.left = Node(3)
A.right = Node(3)

B = Node(1)
B.left = Node(2)
B.right = Node(3)

print(check(A,B))