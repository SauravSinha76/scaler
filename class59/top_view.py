from collections import deque

from class58.TreeNode import Node


class Pair:
    def __init__(self,node,level):
        self.node= node
        self.level = level

def solve(A):
    queue = deque()
    ans =[]
    queue.append(Pair(A,0))
    hm ={}
    max_level = 0
    min_level = 0
    while len(queue) > 0:

        r = queue.popleft()
        if r.level in hm:
            hm[r.level].append(r.node.val)
        else:
            hm[r.level] = [r.node.val]

        if r.node.left:
            queue.append(Pair(r.node.left,r.level-1))
        if r.node.right:
            queue.append(Pair(r.node.right,r.level+1))

        max_level = max(max_level,r.level)
        min_level = min(min_level,r.level)

    for i in range(min_level,max_level+1):
        ans.append(hm[i][0])

    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
root.right.left = Node(6)
root.left.left.left = Node(8)

print(solve(root))


