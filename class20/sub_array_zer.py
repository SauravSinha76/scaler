def solve(A):
    n = len(A)
    uniq = set()
    psum =0
    for i in range(0,n):
        psum += A[i]
        if psum == 0:
            return 1
        uniq.add(psum)

    if len(uniq) != n:
        return 1
    else:
        return 0

A = [1, 2, 3, 4, 5]
print(solve(A))

