from class57.MyQueue import Node

def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right,arr)

def build_tree(A,start,end):
    if start > end:
        return
    mid = (end + start)// 2
    root = Node(A[mid])
    root.left = build_tree(A,start,mid -1)
    root.right = build_tree(A,mid + 1,end)
    return root

A = [1,2,3,4,5,6,7,8]
root = build_tree(A,0,len(A)-1)
arr =[]
inorder(root,arr)
print(arr)