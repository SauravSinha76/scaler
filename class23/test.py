def fun(A):
    if A % 2 == 0:
        return 0

    return fun(A-1) + fun(A//2)
print(fun(23))