def bsearch(low, high, n, arr):
    mid = (low + high) // 2

    if low <= high:
        if arr[mid] < n:
            return bsearch(mid + 1, high, n, arr)
        return bsearch(low, mid - 1, n, arr)

    return high

def solve(A,B,C):

    for i in range(A):
        C[i].sort()
    print(C)

    ans = (1 << 31) -1

    # For each matrix element
    for i in range(A - 1):
        for j in range(B):
            # Search smallest element in the next row which
            # is greater than or equal to the current element
            p = bsearch(0, B - 1, C[i][j], C[i + 1])
            if p < 0:
                p = 0
            ans = min(ans, abs(C[i + 1][p] - C[i][j]))

            # largest element which is smaller than the current
            # element in the next row must be just before
            # smallest element which is greater than or equal
            # to the current element because rows are sorted.
            if p + 1 < B:
                ans = min(ans, abs(C[i + 1][p + 1] - C[i][j]))
    return ans

A = 2
B = 2
C = [ [8, 4],
      [6, 8] ]
#
# A = 3
# B = 2
# C = [[7, 3],
#      [2, 1],
#      [4, 9]]
print(solve(A,B,C))

