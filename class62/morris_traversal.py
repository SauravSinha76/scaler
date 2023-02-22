def solve(A):

    curr = A
    ans =[]

    while curr:

        if curr.left is None:
            ans.append(curr.val)
            curr = curr.right
        else:
            temp = curr.left
            while temp.right and temp.right != curr:
                temp = temp.right
            if temp.right is None:
                temp.right = curr
                curr = curr.left
            else:
                temp.right = None
                ans.append(curr.val)
                curr = curr.right
    return ans


