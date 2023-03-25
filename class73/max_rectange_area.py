def solve(A):
    n = len(A)
    m = len(A[0])

    S = [[0 for _ in range(m)]
         for _ in range(n)]
    for i in range(n):
        S[i][0] = A[i][0]
    for j in range(m):
        S[0][j] = A[0][j]
    for i in range(1,n):
        for j in range(1,m):
            if A[i][j]:
                S[i][j] = min(S[i-1][j-1],S[i-1][j],S[i][j-1]) + A[i][j]

    max_val = S[0][0]
    max_i = 0
    max_j = 0

    for i in range(n):
        for j in range(m):
            if max_val < S[i][j]:
                max_val = S[i][j]
                max_i = i
                max_j = j
    ans = 0
    for i in range(max_i, max_i - max_val ,-1):
        for j in range(max_j, max_j - max_val, -1):
            ans += A[i][j]

    return ans

def solve1(A):
    n = len(A)
    m = len(A[0])
    Area = 0

    for j in range(m):
        for i in range(n):
            if A[i][j] == 1 and j >= 1:
                A[i][j] += A[i][j - 1]
    print(A)

    for i in range(n):
        for j in range(m):
            if A[i][j] != 0:
                w = A[i][j]
                k = i

            while (k >= 0):
                h = i - k + 1
                w = min(w, A[k][j])
                Area = max(Area, w * h)
                k -= 1
    return Area
A = [
       [1, 1, 1],
       [0, 1, 1],
       [1, 0, 0]
     ]
# A= [
#   [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
#   [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#   [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
#   [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
#   [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
# ]
print(solve1(A))