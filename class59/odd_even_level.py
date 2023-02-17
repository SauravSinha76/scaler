from collections import deque

from class58.TreeNode import Node


def solve(A):
    queue = deque()

    odd_sum =0
    even_sum = 0
    dummy = Node(-1)
    queue.append(A)
    queue.append(dummy)

    even = False

    while len(queue) > 1:
        r = queue.popleft()

        if r == dummy:
            even = not even
            queue.append(dummy)
        else:
            if even:
                even_sum += r.val
            else:
                odd_sum += r.val

            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)

    return odd_sum - even_sum


root = Node(1)
root.left = Node(2)
root.right = Node(10)
# root.left.left = Node(4)
root.left.right = Node(4)
# root.left.left.left = Node(8)
# root.right.left = Node(6)
# root.right.right = Node(7)

print(solve(root))
