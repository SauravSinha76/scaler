from class58.TreeNode import Node

def solve(root):
    stack =[]
    ans =[]
    curr = root
    while curr or len(stack) != 0:
        while curr:
            stack.append(curr)
            stack.append(curr)
            curr = curr.left
        node = stack.pop()
        if len(stack) > 0 and node == stack[-1]:
            curr = node.right
        else:
            ans.append(node.val)
            curr = None
    return ans

def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val,end=" ")


root = Node(1)
root.left = Node(6)
root.right = Node(2)
root.right.left = Node(3)

post_order(root)
print(solve(root))
