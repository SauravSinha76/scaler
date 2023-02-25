from collections import deque

from class58.TreeNode import Node


class Pair:
    def __init__(self,node,level):
        self.node= node
        self.level = level

def solve(A):
    queue = deque()
    queue.append(Pair(A,0))
    hm ={}
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

    return len(hm) -1


def height(node):
    # Base Case : Tree is empty
    if node is None:
        return 0

    # If tree is not empty then height = 1 + max of left
    # height and right heights
    return 1 + max(height(node.left), height(node.right))


def diameter(root):
    # Base Case when tree is empty
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    # Get the diameter of left and right sub-trees
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))



class Soution:
    def solve_1(self, A):
        # count for max len diameter found
        self.maxans = 0
        self.diameter = 0

        def diameterlen(node):
            if not node: return 0
            lft = diameterlen(node.left)
            rgt = diameterlen(node.right)
            # check for subtree max diameter
            self.maxans = max(self.maxans, lft + rgt)
            # returning parent tree max depth
            return 1 + max(lft, rgt)

        # main tree left and right depth
        lft = diameterlen(A.left)
        rgt = diameterlen(A.right)
        self.maxans = max(self.maxans, lft + rgt)

        return self.maxans


    def solve_2(self,A):
        if A is None:
            return -1
        l = self.solve_2(A.left)
        r = self.solve_2(A.right)
        self.diameter = max(self.diameter, l + r + 2)
        return max(l,r) +1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
# root.left.right = Node(5)
# # root.right.right = Node(7)
# root.right.right = Node(6)
# root.left.left.left = Node(8)

print(solve(root))
sol = Soution()
print(sol.solve_1(root))
sol.solve_2(root)
print(sol.diameter)


