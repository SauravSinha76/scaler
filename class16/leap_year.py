def solve(A):
    if A % 400 == 0:
        return 1
    elif A % 4 == 0 and A % 100 != 0:
        return 1
    else:
        return 0


print(solve(1999))