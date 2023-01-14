def solve(A,B):
    n = len(A)

    l = 0
    r = n-1
    start = -1
    while l <= r:
        mid = (l+r) // 2
        if A[mid] == B:
            start = mid
            r = mid - 1
        elif A[mid] < B:
            l = mid + 1
        else:
            r = mid - 1

    l = 0
    r = n - 1
    end = -1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == B:
            end = mid
            l = mid + 1
        elif A[mid] < B:
            l = mid + 1
        else:
            r = mid - 1

    return [start,end]

A = [5, 7, 7, 8, 8, 10]
B = 8

A = [5, 17, 100, 111]
B = 3
print(solve(A,B))


