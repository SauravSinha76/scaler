def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right,arr)


def sum_common(A,B):

    arr_A = []
    inorder(A,arr_A)

    arr_B =[]
    inorder(B,arr_B)

    i = 0
    j = 0

    common_node_sum = 0
    while i < len(arr_A) and j < len(arr_B):
        if arr_A[i] == arr_B[j]:
            common_node_sum += arr_A[i]
            i+= 1
            j += 1
        elif arr_A[i] < arr_B[j]:
            i += 1
        else:
            j += 1

    return common_node_sum