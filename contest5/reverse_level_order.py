from collections import deque

from class58.TreeNode import Node


def solve(A):

    queue = deque()
    queue.append(A)
    row = []
    while len(queue) > 0:
        node = queue.popleft()
        row.append(node.val)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    row.reverse()
    return row

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(solve(root))

