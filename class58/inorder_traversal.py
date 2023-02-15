from class58.TreeNode import Node


def solve(A):

    stack =[]
    ans =[]
    curr = A
    while curr or len(stack)!= 0:
        while curr:
            stack.append(curr)
            curr = curr.left
        node = stack[-1]
        stack.pop()
        ans.append(node.val)
        curr = node.right

    return ans

root = Node(1)
root.left = Node(6)
root.right = Node(2)
root.right.left = Node(3)
print(solve(root))


