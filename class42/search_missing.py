def solve(A,B):
    l =0
    r = len(A) -1

    while l <= r:
        mid = (l + r) // 2

        if A[mid] == B:
            return mid
        elif A[mid] < B:
            l = mid + 1
        else:
            r = mid -1

    return l

A = [1, 3, 5, 6]
B = 5

A = [1]
B = 1
print(solve(A,B))