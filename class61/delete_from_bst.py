from class58.TreeNode import Node

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder((root.right))

def solve(A,B):
    tmp = A
    parent = None
    curr = tmp
    while tmp:
        if tmp.val == B:
            curr = tmp
            break
        elif tmp.val <= B:
            parent = tmp
            tmp = tmp.right
        else:
            parent = tmp
            tmp = tmp.left

    if curr.left is None and curr.right is None:
        if parent is None:
            A = None
        elif parent.left == curr:
            parent.left = None
        else:
            parent.right = None
    elif curr.left is None and curr.right is not None:
        if parent is None:
            A = curr.right
        elif parent.left == curr:
            parent.left = curr.right
        else:
            parent.right = curr.right
    elif curr.left is not None and curr.right is None:
        if parent is None:
            A = curr.left
        elif parent.left == curr:
            parent.left = curr.left
        else:
            parent.right = curr.left
    else:
        local_tmp = curr.left
        while local_tmp.right:
            local_tmp = local_tmp.right
        curr.val, local_tmp.val = local_tmp.val, curr.val
        curr.left = solve(curr.left, local_tmp.val)
    return A

root = Node(15)
root.left = Node(12)
# root.left.left = Node(8)
# root.left.right = Node(14)
root.right = Node(20)
# root.right.left = Node(16)
# root.right.right = Node(27)


inorder(root)
root_delete = solve(root,15)
print()
inorder(root_delete)
