from class58.TreeNode import Node


def inorder(A):
    if A is None:
        return
    inorder(A.left)
    print(A.val,end=" ")
    inorder(A.right)

def solve(A):
    if A is None:
        return
    temp = A.left
    A.left = A.right
    A.right = temp
    solve(A.left)
    solve(A.right)


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)

inorder(root)
solve(root)
print()
inorder(root)