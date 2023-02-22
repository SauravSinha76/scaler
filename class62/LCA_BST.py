from class58.TreeNode import Node


def solve(A,B,C):

    curr = A
    while curr:

        if curr.val < B and curr.val < C:
            curr = curr.right
        elif curr.val > B and curr.val > C:
            curr = curr.left
        else:
            return curr.val

    return -1

root = Node(15)
root.left = Node(12)
root.right = Node(20)
root.left.left = Node(10)
root.left.left.left = Node(8)
root.left.right = Node(14)
root.right.right = Node(27)
root.right.left = Node(16)

print(solve(root,16,27))
