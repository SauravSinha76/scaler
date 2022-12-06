def solve(A,B):
    n = len(A)
    for i in range(n):
        for j in range(1,n):
            A[i][j] += A[i][j-1]

    for i in range(1,n):
        for j in range(n):
            A[i][j] += A[i-1][j]

    max_sum = 0
    if n == B:
        return A[B-1][B-1]

    for i in range(n - B + 1):
        for j in range(n - B + 1):

            sum = A[i+B-1][j+B-1]
            if i > 0:
                sum -= A[i -1][j+B-1]
            if j > 0:
                sum -= A[i+B-1][j-1]
            if i > 0 and j > 0:
                sum += A[i-1][j-1]

            max_sum = max(max_sum, sum)
    return max_sum

A = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
     ]
B = 3

# A = [
#         [2, 2],
#         [2, 2]
#     ]
# B = 2
print(solve(A,B))
