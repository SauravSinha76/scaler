def solve(A):

    curr = A

    while curr:

        if curr.left:
            # set curr node as root.left
            temp = curr.left
            # traverse to the extreme right of curr
            while temp.right:
                temp = temp.right
            # join curr.right to root.right
            temp.right = curr.right
            # put root.left to root.right
            curr.right = curr.left
            # make root.left as None
            curr.left = None
            # now go to the right of the root
        curr = curr.right
    return A