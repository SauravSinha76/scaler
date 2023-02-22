from class58.TreeNode import Node


def inorder(A,arr):
    if A is None:
        return
    inorder(A.left,arr)
    arr.append(A.val)
    inorder(A.right,arr)


def solve(A,B):

    arr =[]
    inorder(A,arr)

    i = 0
    j = len(arr) -1

    while i < j:
        sum = arr[i] + arr[j]
        if sum < B:
            i += 1
        elif sum > B:
            j -= 1
        else:
            return 1
    return 0

root = Node(10)
root.left = Node(9)
root.right = Node(20)
print(solve(root,40))