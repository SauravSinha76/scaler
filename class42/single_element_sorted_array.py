def solve(A):

    n = len(A)
    if A[0] != A[1]:
        return A[0]
    if A[n-1] != A[n-2]:
        return A[n-1]

    l = 1
    r = n-2
    while l <= r:
        mid = (l + r) // 2

        if A[mid-1] != A[mid] != A[mid +1]:
            return A[mid]

        first = mid

        if A[mid -1] == A[mid]:
            first = mid -1


        if first % 2 ==0:
            l = first + 2
        else:
            r = first - 1


A = [1, 1, 7]
A = [2, 3, 3]
A = [3,3,1,1,8,8,10,10,9,6,6,2,2]
print(solve(A))
