def check(A,B):
    if not A:
        return False
    if not A.left and not A.right:
        if A.val == B:
            return True
        else:
            return False

    return check(A.left, B - A.val) or check(A.right, B - A.val)

