def solve(A):
    n = len(A)
    A.sort()
    i =0
    while i < n-1:
        A[i],A[i+1] = A[i+1],A[i]
        i += 2

    return A

A = [1, 2, 3, 4]
print(solve(A))