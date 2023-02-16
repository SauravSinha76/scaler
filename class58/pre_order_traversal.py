from class58.TreeNode import Node


def solve(A):

    stack =[]
    ans = []
    curr = A
    while len(stack) !=0  or curr:
        while curr:
            ans.append(curr.val)
            stack.append(curr)
            curr = curr.left

        node = stack[-1]
        stack.pop()
        curr = node.right

    return ans

def solve_recursive(root):
    if root is None:
        return
    print(root.val,end=" ")
    solve_recursive(root.left)
    solve_recursive(root.right)

root = Node(1)
root.left = Node(6)
root.right = Node(2)
root.right.left = Node(3)
print(solve(root))
solve_recursive(root)

