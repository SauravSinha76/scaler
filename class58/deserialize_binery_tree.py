from collections import deque

from class58.TreeNode import Node

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.val, end=" ")
    in_order(root.right)

def solve(A):
    queue = deque()
    root = Node(A[0])
    queue.append(root)
    n = len(A)
    i = 1
    while i < n:
        curr = queue.popleft()
        if A[i] != -1:
            curr.left = Node(A[i])
            queue.append(curr.left)
        i += 1
        if A[i] != -1:
            curr.right = Node(A[i])
            queue.append(curr.right)
        i += 1

    return root

A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
root = solve(A)
in_order(root)


