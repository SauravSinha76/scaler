def solve(A,B):
    n = len(A)
    m = len(A[0])

    for i in range(n):
        for j in range(m):
            if B == A[i][j]:
                return (i+1) * 1009 + (j+1)
    return -1


def search(mat, x):
    n = len(A)
    m = len(A[0])
    min_val = (1 << 31)
    i = 0

    # set indexes for top right element
    j = m - 1
    while i < n and j >= 0:

        if mat[i][j] >= x:
            min_val = min(min_val, (i+1) * 1009 + (j+1))
            j -= 1

        # if mat[i][j] >= x:
        #     j -= 1

        # if mat[i][j] < x
        else:
            i += 1
    if min_val == (1 < 31):
        return -1  # if (i == n || j == -1 )
    else:
        return min_val

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# A = [
#   [2, 8, 8, 8],
#   [2, 8, 8, 8],
#   [2, 8, 8, 8]
# ]
B = 2

print(solve(A,B))
print(search(A,B))