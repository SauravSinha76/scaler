def solve(A,B):
    tmp = A
    while tmp:
        if B == tmp.val:
            return True
        elif B < tmp.val:
            tmp = tmp.right
        else:
            tmp = tmp.left

    return False

