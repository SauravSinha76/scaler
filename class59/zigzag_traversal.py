from collections import deque

from class58.TreeNode import Node


def solve(A):

    queue = deque()
    stack =[]
    ans =[]
    dummy = Node(-1)
    queue.append(A)
    queue.append(dummy)
    flag = False
    row =[]
    while len(queue) > 1:
        r = queue.popleft()

        if r == dummy:
            while len(stack) != 0:
                row.append(stack.pop())
            stack =[]
            ans.append(row)
            row =[]
            flag = not flag
            queue.append(dummy)
        else:
            if flag:
                row.append(r.val)
            else:
                stack.append(r.val)

            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)


    while len(stack) != 0:
        row.append(stack.pop())
    ans.append(row)
    return ans

root = Node(1)
root.left = Node(6)
root.right = Node(2)
root.right.left = Node(3)
# root.right.right = Node(7)
print(solve(root))



