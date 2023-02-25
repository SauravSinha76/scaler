from class58.TreeNode import Node


def symmetrical(A,B):
    if not A and not B:
        return True
    if not A or not B:
        return False

    if A.val != B.val:
        return False

    left = symmetrical(A.left, B.right)
    right = symmetrical(A.right, B.left)

    if left and right:
        return 1

    return 0


root = Node(1)
root.left = Node(2)
root.right = Node(2)
print(symmetrical(root,root))