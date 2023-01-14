def solve(A):
    n = len(A)
    if n == 1:
        return A[0]

    if A[0] > A[1]:
        return A[0]

    if A[n-1] > A[n-2]:
        return A[n-1]

    l = 1
    r = n-2

    while l <= r:
        mid = (l + r) // 2
        if A[mid-1] <= A[mid] >= A[mid +1]:
            return A[mid]
        elif A[mid+ 1] > A[mid]:
            l = mid +1
        else:
            r = mid - 1

A = [1, 2, 3, 4, 5]
A = [5, 17, 100, 11]
A = [ 1, 1000000000, 1000000000 ]
print(solve(A))