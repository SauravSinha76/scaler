from collections import deque

from class58.TreeNode import Node


def solve(A):

    queue = deque()
    dummy = Node(-1)
    queue.append(A)
    queue.append(dummy)
    ans =[]
    row = []
    while len(queue) > 1:
        node = queue.popleft()
        if node == dummy:
            ans.append(row)
            row =[]
            queue.append(node)
        else:
            row.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    ans.append(row)
    return ans

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(solve(root))

