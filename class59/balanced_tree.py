def balance(A):
    if A is None:
        return 1

    lh = balance(A.left)


    if lh == -1:
        return -1

    rh = balance(A.right)
    if rh == -1:
        return -1

    if abs(lh - rh)> 1:
        return -1

    else:
        return max(lh, rh) +1

def isBalanced(A):

    if balance(A) == -1:
        return 0
    else:
        return 1

