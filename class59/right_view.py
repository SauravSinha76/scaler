from collections import deque

from class58.TreeNode import Node


def solve(A):

    queue = deque()
    ans = []
    dummy = Node(-1)

    queue.append(A)
    queue.append(dummy)
    ans.append(A.val)
    while len(queue) > 1:

        r = queue.popleft()

        if r == dummy:
           ans.append(queue[0].val)
           queue.append(dummy)
        else:
            if r.right:
                queue.append(r.right)
            if r.left:
                queue.append(r.left)

    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)

print(solve(root))
