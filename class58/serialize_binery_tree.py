from collections import deque

from class58.TreeNode import Node


def solve(A):
    queue = deque()
    dummy = Node(-1)
    queue.append(A)
    ans = []
    while len(queue) > 0:
        node = queue.popleft()
        ans.append(node.val)
        if node != dummy:
            if node.left:
                queue.append(node.left)
            else:
                queue.append(dummy)
            if node.right:
                queue.append(node.right)
            else:
                queue.append(dummy)
    return ans


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(6)

print(solve(root))