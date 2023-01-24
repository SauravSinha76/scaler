def solev(A):
    psum =0
    unique = set()
    for a in A:
        psum += a
        if psum == 0:
            return 1
        unique.add(psum)

    if len(unique) == len(A):
        return 0
    else:
        return 1

A = [1, 2, 3, 4, 5]
A = [-1, 1]
print(solev(A))